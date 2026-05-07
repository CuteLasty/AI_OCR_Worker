import cv2
import numpy as np
from loguru import logger
# from .text_drawer import PILTextDrawer
from .draw_utils import PILTextDrawer


def crop_image(image_path, bbox, output_path):
    """
    根據邊界框裁剪圖像

    Args:
        image_path (str): 圖像路徑
        bbox (list): 邊界框 [x1, y1, x2, y2]
        output_path (str): 保存裁剪圖像的路徑

    Returns:
        str: 裁剪圖像的路徑
    """
    try:
        # 讀取圖像
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"讀取圖像失敗: {image_path}")

        # 裁剪圖像
        x1, y1, x2, y2 = [int(coord) for coord in bbox]
        cropped = img[y1:y2, x1:x2]

        # 保存裁剪圖像
        cv2.imwrite(output_path, cropped)
        logger.info(f"裁剪圖像保存至 {output_path}")

        return output_path

    except Exception as e:
        logger.error(f"裁剪圖像時出錯: {e}")
        raise


def preprocess_image(image_path, output_path, method='otsu'):
    """
    預處理OCR的圖像

    Args:
        image_path (str): 圖像路徑
        output_path (str): 保存預處理圖像的路徑

    Returns:
        str: 預處理圖像的路徑
    """
    try:
        # 讀取圖像
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"讀取圖像失敗: {image_path}")

        # 轉換為灰度
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if method == 'otsu':
            # Otsu's thresholding
            _, result = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        elif method == 'adaptive':
            # Adaptive thresholding for images with uneven lighting
            result = cv2.adaptiveThreshold(
                gray,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,  # Block size
                2    # Constant subtracted from mean
            )
        else:
            # 應用高斯模糊
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # 應用自適應閾值處理
            thresh = cv2.adaptiveThreshold(
                blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV, 11, 2
            )

            # 應用形態學操作
            kernel = np.ones((3, 3), np.uint8)
            opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

            # 反轉回黑色文字在白色背景上
            result = cv2.bitwise_not(opening)

            # 保存預處理圖像
        cv2.imwrite(output_path, result)
        logger.info(f"預處理圖像保存至 {output_path}")
        return output_path

    except Exception as e:
        logger.error(f"預處理圖像時出錯: {e}")
        raise


def preprocess_image_(image_path, output_path):
    """
    預處理OCR的圖像

    Args:
        image_path (str): 圖像路徑
        output_path (str): 保存預處理圖像的路徑

    Returns:
        str: 預處理圖像的路徑
    """
    try:
        # 讀取圖像
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"讀取圖像失敗: {image_path}")

        # 轉換為灰度
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 應用高斯模糊
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # 應用自適應閾值處理
        thresh = cv2.adaptiveThreshold(
            blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV, 11, 2
        )

        # 應用形態學操作
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # 反轉回黑色文字在白色背景上
        result = cv2.bitwise_not(opening)

        # 保存預處理圖像
        cv2.imwrite(output_path, result)
        logger.info(f"預處理圖像保存至 {output_path}")

        return output_path

    except Exception as e:
        logger.error(f"預處理圖像時出錯: {e}")
        raise


def draw_ocr_results(image_path, ocr_results, output_path):
    """
    在圖像上繪製OCR結果

    Args:
        image_path (str): 圖像路徑
        ocr_results (list): 包含位置和文字的OCR結果
        output_path (str): 保存註釋圖像的路徑

    Returns:
        str: 註釋圖像的路徑
    """
    try:
        # 讀取圖像
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"讀取圖像失敗: {image_path}")

        fontScale = 32
        text_drawer = PILTextDrawer(preload_fonts=[
            ("simsun.ttc", int(round(fontScale)))
        ])

        # Define colors for different operations
        colors = {
            'bbox': (0, 255, 0),        # Green for bounding boxes
            'text': (255, 0, 0),        # Blue for text
            'index': (0, 0, 255),       # Red for index numbers
            'equal': (0, 255, 0),       # Green for matching text
            'replace': (0, 165, 255),   # Orange for replaced text
            'delete': (0, 0, 255),      # Red for deleted text
            'insert': (255, 0, 0),      # Blue for inserted text
            'error': (0, 0, 255)        # Red for error highlights
        }

        # 創建副本
        result = img.copy()

        # 繪製OCR結果
        for item in ocr_results:
            positions = item['positions']
            text = item['text']

            # 將位置轉換為numpy點數組
            points = np.array([[int(p[0]), int(p[1])]
                              for p in positions], dtype=np.int32)

            # 在文字周圍繪製多邊形
            cv2.polylines(result, [points], True, (0, 255, 0), 2)

            # 在框上方繪製文字
            x, y = int(positions[0][0]), int(positions[0][1] - 10)
            # cv2.putText(result, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            text_drawer.putText(result, text, (x, y), "simsun.ttc",
                                fontScale, colors['text'], 1)

        # 保存結果
        cv2.imwrite(output_path, result)
        logger.info(f"OCR可視化保存至 {output_path}")

        return output_path

    except Exception as e:
        logger.error(f"繪製OCR結果時出錯: {e}")
        raise


def draw_analysis_results(image_path, analysis_results, output_path):
    """
    在圖像上繪製分析結果

    Args:
        image_path (str): 圖像路徑
        analysis_results (dict): 分析結果
        output_path (str): 保存註釋圖像的路徑

    Returns:
        str: 註釋圖像的路徑
    """
    try:
        # 讀取圖像
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"讀取圖像失敗: {image_path}")

        fontScale = 32
        text_drawer = PILTextDrawer(preload_fonts=[
            ("simsun.ttc", int(round(fontScale)))
        ])

        # Define colors for different operations
        colors = {
            'bbox': (0, 255, 0),        # Green for bounding boxes
            'text': (255, 0, 0),        # Blue for text
            'index': (0, 0, 255),       # Red for index numbers
            'equal': (0, 255, 0),       # Green for matching text
            'replace': (0, 165, 255),   # Orange for replaced text
            'delete': (0, 0, 255),      # Red for deleted text
            'insert': (255, 0, 0),      # Blue for inserted text
            'error': (0, 0, 255)        # Red for error highlights
        }

        # 創建副本
        result = img.copy()

        # 繪製整體結果
        # match = analysis_results.get('match', False)
        # status_text = "通過" if match else "失敗"
        # color = (0, 255, 0) if match else (0, 0, 255)  # 通過為綠色，失敗為紅色

        # 在頂部繪製狀態
        # cv2.putText(result, status_text, (20, 50),
        #            cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)

        # 繪製詳細結果
        y_offset = 100
        for idx, res in enumerate(analysis_results.get('results', [])):
            text = res.get('text', '')
            res_match = res.get('match', False)
            rule = res.get('rule', {})
            rule_text = rule.get('text', '') or rule.get('pattern', '')

            # 繪製狀態
            status = "✓" if res_match else "✗"
            color = colors['equal'] if res_match else colors['error']

            # 顯示結果信息
            info_text = f"{status} 規則 {idx+1}: 發現 '{text}'"
            # cv2.putText(result, info_text, (20, y_offset),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            text_drawer.putText(result, text, (20, y_offset), "simsun.ttc",
                                fontScale, color, 1)

            y_offset += 30

            # 顯示預期文字
            expected_text = f"    預期: '{rule_text}'"
            # cv2.putText(result, expected_text, (20, y_offset),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 1)
            text_drawer.putText(result, text, (20, y_offset), "simsun.ttc",
                                fontScale, (255, 0, 255), 1)

            y_offset += 40

        # 保存結果
        cv2.imwrite(output_path, result)
        logger.info(f"分析可視化保存至 {output_path}")

        return output_path

    except Exception as e:
        logger.error(f"繪製分析結果時出錯: {e}")
        raise
