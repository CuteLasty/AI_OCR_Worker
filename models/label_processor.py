import os
import json
import shutil
from pathlib import Path
from loguru import logger

from .ocr_model import OCRModel
from .yolo_model import YoloModel
# from analyzers.barcode_analyzer import BarcodeAnalyzer
# from analyzers.text_analyzer import TextAnalyzer

from analyzers.label_analyzer_factory import LabelAnalyzerFactory

from utils.file_utils import ensure_dir, get_timestamp_dir, backup_file
from utils.image_utils import crop_image, preprocess_image, draw_analysis_results
from templates.label_templates import TemplateManager
from utils.visualization import Visualizer


class LabelProcessor:
    def __init__(self,
                 yolo_model_path="best.pt",
                 backup_base="backups",
                 result_base="results",
                 template_dir="templates",
                 ocr_lang='ch',
                 use_gpu=True,
                 det_db_thresh=0.3,
                 det_db_box_thresh=0.5,
                 drop_score=0.5,
                 max_text_length=25):
        """
        初始化標籤處理器

        Args:
            yolo_model_path (str): YOLO模型路徑
            backup_base (str): 備份基礎目錄
            result_base (str): 結果基礎目錄
            template_dir (str): 模板目錄
            ocr_lang (str): OCR語言代碼
            use_gpu (bool): 是否使用GPU
            det_db_thresh (float): 文字檢測閾值
            det_db_box_thresh (float): 文字檢測框閾值
            drop_score (float): 文字識別的最低分數
            max_text_length (int): 最大文字長度
        """
        try:
            backup_dir = os.path.abspath(os.path.join(
                '..', 'AI_OCR_Service', backup_base))
            result_dir = os.path.abspath(os.path.join(
                '..', 'AI_OCR_Service', result_base))

            # 保存配置
            self.backup_base = backup_dir
            self.result_base = result_dir
            # self.template_dir = template_dir
            self.lang = ocr_lang
            self.use_gpu = use_gpu
            self.det_db_thresh = det_db_thresh
            self.det_db_box_thresh = det_db_box_thresh
            self.drop_score = drop_score
            self.max_text_length = max_text_length

            # 確保目錄存在
            ensure_dir(backup_dir)
            ensure_dir(result_dir)
            # ensure_dir(template_dir)
            # ensure_dir(os.path.join(template_dir, 'barcode'))
            # ensure_dir(os.path.join(template_dir, 'text'))

            # 初始化YOLO
            logger.info("初始化YOLO...")
            self.yolo = YoloModel(model_path=yolo_model_path)

            # 初始化OCR
            logger.info("初始化OCR...")
            self.ocr = OCRModel(
                lang=self.lang,
                use_gpu=self.use_gpu,
                det_db_thresh=self.det_db_thresh,
                det_db_box_thresh=self.det_db_box_thresh,
                drop_score=self.drop_score,
                max_text_length=self.max_text_length
            )

            # 初始化分析器
            # self.barcode_analyzer = BarcodeAnalyzer()
            # self.text_analyzer = TextAnalyzer()
            self.analyzer_factory = LabelAnalyzerFactory()
            self.template_manager = TemplateManager()
            self.visualizer = Visualizer()

            logger.info("LabelProcessor初始化成功")

        except Exception as e:
            logger.error(f"初始化LabelProcessor失敗: {e}")
            raise

    def process(self, data):
        """
        處理標籤任務

        Args:
            data (dict): 標籤任務數據

        Returns:
            dict: 處理結果
        """
        try:
            # 驗證輸入數據
            self._validate_input(data)

            image_path = data['image_path']
            timestamp = data['timestamp']
            label_type = data['type'].lower()  # 轉換為小寫以處理大小寫不一致

            logger.info(f"開始處理 {image_path}, 類型: {label_type}")

            # 創建結果
            result = {
                'success': False,
                'image_path': image_path,
                'timestamp': timestamp,
                'type': label_type,
                # 'backup_path': None,
                'raw_image_path': None,
                'preprocessed_image_path': None,
                'ocr_results': None,
                'ocr_image_path': None,
                'analysis_results': None,
                'analysis_image_path': None,
                'error': None
            }

            # 1. 備份圖像
            # result['backup_path'] = self._backup_image(image_path, timestamp)

            # 2. YOLO檢測並切割
            largest_box, raw_image_path = self._detect_and_crop(
                image_path, timestamp)
            result['raw_image_path'] = raw_image_path

            # 3. 預處理圖像
            pp_image_path = self._preprocess_image(raw_image_path, timestamp)
            result['preprocessed_image_path'] = pp_image_path

            # 4. OCR識別
            ocr_results = self._recognize_text(pp_image_path)
            result['ocr_results'] = ocr_results

            # 5. 保存OCR結果並可視化
            ocr_results_path, ocr_image_path = self._save_ocr_results(
                ocr_results, raw_image_path, timestamp)
            result['ocr_image_path'] = ocr_image_path

            # 6. 根據類型分析
            if label_type == 'barcode':
                analysis_results = self._analyze_barcode(ocr_results, data)
            elif label_type == 'text':
                data['image_width'], data['image_height'] = self._calculate_bounding_box_dimensions(
                    largest_box)
                analysis_results = self._analyze_text(ocr_results, data)
            else:
                raise ValueError(f"不支持的標籤類型: {label_type}")

            analyzer = self.analyzer_factory.create_analyzer(
                data['type'], sku_name)
            analysis_results = analyzer.analyze(ocr_results)

            result['analysis_results'] = analysis_results

            # 7. 可視化分析結果
            analysis_image_path = self._visualize_analysis(
                analysis_results, raw_image_path, timestamp)
            result['analysis_image_path'] = analysis_image_path

            # 設置處理成功
            result['success'] = True
            logger.info(f"成功處理 {image_path}")

            return result

        except Exception as e:
            logger.error(f"處理標籤時出錯: {e}")
            # 如果我們已經有了一個結果對象，更新它
            if 'result' in locals():
                result['success'] = False
                result['error'] = str(e)
                return result
            # 否則創建一個新的錯誤結果
            return {
                'success': False,
                'error': str(e)
            }

    def _validate_input(self, data):
        """
        驗證輸入數據

        Args:
            data (dict): 輸入數據

        Raises:
            ValueError: 當輸入數據無效時
        """
        required_fields = ['image_path', 'timestamp', 'type']

        # 檢查所有必要字段
        for field in required_fields:
            if field not in data:
                raise ValueError(f"缺少必要字段: {field}")

        # 檢查圖像路徑
        if not os.path.exists(data['image_path']):
            raise FileNotFoundError(f"圖像文件未找到: {data['image_path']}")

        # 檢查時間戳格式
        timestamp = data['timestamp']
        if '_' not in timestamp or len(timestamp) != 22:
            raise ValueError(
                f"時間戳格式無效，應為'YYYYMMDD_HHMMSS_ffffff': {timestamp}")

        # 檢查類型
        label_type = data['type'].lower()
        if label_type not in ['barcode', 'text']:
            raise ValueError(f"不支持的標籤類型: {label_type}")

        # 如果是文字類型，檢查SKU名稱
        if label_type == 'text' and 'sku_name' not in data:
            raise ValueError("文字標籤需要'sku_name'字段")

    def _backup_image(self, image_path, timestamp):
        """
        備份圖像

        Args:
            image_path (str): 圖像路徑
            timestamp (str): 時間戳

        Returns:
            str: 備份路徑
        """
        return backup_file(image_path, self.backup_base, timestamp)

    def _detect_and_crop(self, image_path, timestamp):
        """
        用YOLO檢測並裁剪標籤

        Args:
            image_path (str): 圖像路徑
            timestamp (str): 時間戳

        Returns:
            tuple: (最大的標籤框, 裁剪圖像的路徑)
        """
        # 運行YOLO檢測
        detections = self.yolo.detect(image_path)

        # 找到最大的框
        largest_box = self.yolo.find_largest_box(detections)
        if not largest_box:
            raise ValueError(f"未在 {image_path} 中檢測到標籤")

        # 提取邊界框
        x1, y1, x2, y2 = largest_box['xyxy']

        # 準備目標路徑
        result_dir = get_timestamp_dir(self.result_base, timestamp)
        image_name = Path(image_path).stem
        raw_image_path = os.path.join(result_dir, f"raw_{image_name}.jpg")

        # 裁剪圖像
        crop_image(image_path, [x1, y1, x2, y2], raw_image_path)

        return largest_box, raw_image_path

    def _preprocess_image(self, raw_image_path, timestamp):
        """
        預處理圖像用於OCR

        Args:
            raw_image_path (str): 原始圖像路徑
            timestamp (str): 時間戳

        Returns:
            str: 預處理圖像的路徑
        """
        # 準備目標路徑
        result_dir = os.path.dirname(raw_image_path)
        image_name = Path(raw_image_path).stem.replace('raw_', '')
        pp_image_path = os.path.join(result_dir, f"pp_{image_name}.jpg")

        # 預處理圖像
        preprocess_image(raw_image_path, pp_image_path)

        return pp_image_path

    def _recognize_text(self, pp_image_path):
        """
        用OCR識別文字

        Args:
            pp_image_path (str): 預處理圖像路徑

        Returns:
            list: OCR結果
        """
        return self.ocr.recognize(pp_image_path)

    def _save_ocr_results(self, ocr_results, raw_image_path, timestamp):
        """
        保存OCR結果並創建可視化

        Args:
            ocr_results (list): OCR結果
            raw_image_path (str): 原始圖像路徑
            timestamp (str): 時間戳

        Returns:
            tuple: (OCR結果路徑, OCR可視化圖像路徑)
        """
        # 準備目標路徑
        result_dir = os.path.dirname(raw_image_path)
        image_name = Path(raw_image_path).stem.replace('raw_', '')
        ocr_results_path = os.path.join(
            result_dir, f"ocr_results_{image_name}.json")
        ocr_image_path = os.path.join(result_dir, f"text_{image_name}.jpg")

        # 保存OCR結果
        with open(ocr_results_path, 'w', encoding='utf-8') as f:
            json.dump(ocr_results, f, ensure_ascii=False, indent=2)

        # 創建OCR可視化
        # draw_ocr_results(raw_image_path, ocr_results, ocr_image_path)
        self.visualizer.draw_ocr_results(
            raw_image_path, ocr_results, ocr_image_path)

        return ocr_results_path, ocr_image_path

    def _get_template(self, template_type, sku_name):
        """
        獲取模板

        Args:
            template_type (str): 模板類型 ('barcode' 或 'text')
            sku_name (str): SKU名稱

        Returns:
            dict: 模板數據或None
        """
        # 構建模板路徑
        template_path = os.path.join(
            self.template_dir, template_type, f"{sku_name}.json")

        # 檢查模板是否存在
        if not os.path.exists(template_path):
            logger.warning(f"模板未找到: {template_path}")
            return None

        # 讀取模板
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template = json.load(f)
            return template
        except Exception as e:
            logger.error(f"讀取模板 {template_path} 失敗: {e}")
            return None

    def _analyze_barcode(self, ocr_results, data):
        """
        分析條碼標籤

        Args:
            ocr_results (list): OCR結果
            data (dict): 任務數據

        Returns:
            dict: 分析結果
        """
        # 首先，從OCR結果中找到sku_name
        # 這裡我們假設第一個OCR結果包含SKU名稱
        sku_name = None
        if data:
            # 可以根據特定規則或格式來查找SKU名稱
            # 這裡簡化為使用第一個OCR結果
            sku_name = data['sku_name']

        if not sku_name:
            return {
                'match': False,
                'errors': ["未能從data中確定SKU名稱"]
            }

        # 獲取模板
        template = self.template_manager.find_barcode_label_template(
            sku_name)
        # - template = self._get_template('barcode', sku_name)
        # - if not template:
        # -    return {
        # -        'match': False,
        # -        'errors': [f"未找到SKU {sku_name} 的條碼模板"]
        # -    }

        # 使用條碼分析器分析
        return self.barcode_analyzer.analyze(ocr_results, template)

    def _analyze_text(self, ocr_results, data):
        """
        分析文字標籤

        Args:
            ocr_results (list): OCR結果
            data (dict): 任務數據

        Returns:
            dict: 分析結果
        """
        # 從數據中獲取SKU名稱
        sku_name = data.get('sku_name')
        if not sku_name:
            return {
                'match': False,
                'errors': ["數據中缺少SKU名稱"]
            }

        # 獲取模板
        template = self.template_manager.find_text_label_template(
            sku_name)
        # template = self._get_template('text', sku_name)
        # if not template:
        #    return {
        #        'match': False,
        #        'errors': [f"未找到SKU {sku_name} 的文字模板"]
        #    }

        # 使用文字分析器分析
        return self.text_analyzer.analyze(data, ocr_results, template)

    def _visualize_analysis(self, analysis_results, raw_image_path, timestamp):
        """
        可視化分析結果

        Args:
            analysis_results (dict): 分析結果
            raw_image_path (str): 原始圖像路徑
            timestamp (str): 時間戳

        Returns:
            str: 分析可視化圖像路徑
        """
        # 準備目標路徑
        result_dir = os.path.dirname(raw_image_path)
        image_name = Path(raw_image_path).stem.replace('raw_', '')
        analysis_image_path = os.path.join(result_dir, f"tag_{image_name}.jpg")

        # 保存分析結果
        analysis_results_path = os.path.join(
            result_dir, f"analysis_results_{image_name}.json")
        with open(analysis_results_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_results, f, ensure_ascii=False, indent=2)

        # 創建分析可視化
        # draw_analysis_results(raw_image_path, analysis_results, analysis_image_path)
        self.visualizer.draw_analysis_results(
            raw_image_path, analysis_results, analysis_image_path)

        return analysis_image_path

    def _calculate_bounding_box_dimensions(self, xyxy1):
        """
        Calculates the width and height of a bounding box from its xyxy coordinates.

        Args:
            xyxy: A list or tuple of four floats representing the bounding box coordinates
                  in the format [x_min, y_min, x_max, y_max].

        Returns:
            A tuple of two integers: (width, height).
            Returns (0, 0) if the input is invalid.
        """
        xyxy = xyxy1['xyxy']
        if not isinstance(xyxy, (list, tuple)) or len(xyxy) != 4:
            print("Error: Invalid input.  xyxy must be a list or tuple of length 4.")
            return 0, 0  # Return (0, 0) to indicate an error

        try:
            x_min, y_min, x_max, y_max = map(
                float, xyxy)  # Convert to float first
        except ValueError:
            print("Error: Invalid input.  Coordinates must be numeric.")
            return 0, 0

        width = int(x_max - x_min)
        height = int(y_max - y_min)
        return width, height
