import os
from paddleocr import PaddleOCR
from loguru import logger


class OCRModel:
    def __init__(self,
                 lang='ch',
                 use_gpu=True,
                 det_db_thresh=0.3,
                 det_db_box_thresh=0.4,
                 drop_score=0.5,
                 max_text_length=25):
        """
        初始化PaddleOCR模型

        Args:
            lang (str): 語言代碼
            use_gpu (bool): 是否使用GPU
            det_db_thresh (float): 文字檢測閾值
            det_db_box_thresh (float): 文字檢測框閾值
            drop_score (float): 文字識別的最低分數
            max_text_length (int): 最大文字長度
        """
        try:
            self.lang = lang
            self.use_gpu = use_gpu
            self.det_db_thresh = det_db_thresh
            self.det_db_box_thresh = det_db_box_thresh
            self.drop_score = drop_score
            self.max_text_length = max_text_length

            logger.info("初始化PaddleOCR...")
            # 初始化伺服器PaddleOCR
            self.ocr = PaddleOCR(
                show_log=False,
                lang=self.lang,
                use_gpu=self.use_gpu,
                det_db_thresh=self.det_db_thresh,
                det_db_box_thresh=self.det_db_box_thresh,
                drop_score=self.drop_score,
                max_text_length=self.max_text_length,
                # 高精度伺服器版模型
                det_model_dir="ch_PP-OCRv4_det_server_infer",  # 文字檢測 (高精度)
                rec_model_dir="ch_PP-OCRv4_rec_server_infer",  # 文字識別 (高精度)
                cls_model_dir="ch_ppocr_mobile_v2.0_cls_infer"  # 方向分類 (可選)
                # rec_char_dict_path="c:\\LabelContentCheck\\AI_OCR_Service\\custom_dict.txt"
            )
            logger.info("PaddleOCR初始化成功")

        except Exception as e:
            logger.error(f"初始化PaddleOCR失敗: {e}")
            raise

    def recognize(self, image_path):
        """
        對圖像執行OCR

        Args:
            image_path (str): 圖像路徑

        Returns:
            list: OCR結果，包含文字和位置
        """
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"圖像文件未找到: {image_path}")

            logger.info(f"在 {image_path} 上運行OCR")
            result = self.ocr.ocr(image_path, cls=True)

            # 格式化OCR結果
            ocr_results = []
            if result:
                for idx, line in enumerate(result[0]):
                    positions = line[0]  # [[x1,y1], [x2,y1], [x2,y2], [x1,y2]]
                    text, confidence = line[1]

                    ocr_results.append({
                        'id': idx,
                        'text': text,
                        'confidence': confidence,
                        'positions': positions
                    })

            logger.info(f"OCR完成，發現 {len(ocr_results)} 個文字區域")
            return ocr_results

        except Exception as e:
            logger.error(f"OCR識別過程中出錯: {e}")
            raise
