import numpy as np
from loguru import logger

from utils.text_utils import TextMatcher


class TextAnalyzer:
    def __init__(self):
        """
        初始化文字分析器
        """
        logger.info("初始化TextAnalyzer")

        # Initialize components
        self.text_matcher = TextMatcher()

    def analyze(self, data, ocr_results, template):
        """
        根據模板分析文字OCR結果

        Args:
            ocr_results (list): OCR結果
            template (dict): 模板規格

        Returns:
            dict: 分析結果
        """
        try:
            logger.info("分析文字OCR結果")

            # 初始化結果
            analysis = {
                'match': False,
                'results': [],
                'errors': []
            }

            # 檢查空結果
            if not ocr_results:
                analysis['errors'].append("未找到OCR結果")
                return analysis

            # Process multi-column text
            left_results, right_results = self._process_multicolumn(
                ocr_results, data['image_width'])

            self._calc_size(left_results, right_results)

            sorted_results = left_results + right_results
######
            template_texts = template[1]  # Static template texts
            # Special template texts (barcodes, etc.)
            special_texts = template[2]
            ignore_texts = template[3]  # Texts to ignore

            ocr_results_copy = []
            for line in sorted_results:
                bbox = line['positions']  # OCR bounding box
                text = line['text']  # OCR text
                confidence = line['confidence']  # OCR confidence

                if (text.isdigit() or
                    self.text_matcher.is_string_list_equal_fuzz(text, special_texts) or
                        self.text_matcher.is_string_equal(text, ignore_texts)):
                    text_len = len(text)
                    analysis['results'].append({
                        "bbox": bbox,
                        "text": text,
                        "confidence": confidence,
                        "distance": 0,
                        "template_text": text,
                        "is_special": True,
                        "opcodes": [{
                            "tag": "equal",
                            "i1": 0,
                            "i2": text_len,
                            "j1": 0,
                            "j2": text_len
                        }]
                    })
                    continue
                ocr_results_copy.append(line)

            for line in ocr_results_copy:
                bbox = line['positions']  # OCR bounding box
                text = line['text']  # OCR text
                confidence = line['confidence']  # OCR confidence

                # Find closest matching template text
                opcodes = []
                distance, closest_idx = self.text_matcher.find_closest_text(
                    text, template_texts)
                # if distance < 2 and closest_idx < len(template_texts):
                template_text = template_texts[closest_idx]
                # Get detailed differences
                opcodes = self.text_matcher.get_difference_opcodes(
                    template_text, text)

                analysis['results'].append({
                    "bbox": bbox,
                    "text": text,
                    "confidence": confidence,
                    "distance": distance,
                    "template_text": template_text,
                    # "is_special": False,
                    # "closest_idx": closest_idx,
                    "opcodes": opcodes
                })

            analysis['text'] = []
            for text in template[1]:
                analysis['text'].append(text)
######

            # 確定整體匹配
            # analysis['match'] = all(matches) if matches else False
            #
            # logger.info(f"文字分析完成，整體匹配: {analysis['match']}")
            return analysis

        except Exception as e:
            logger.error(f"文字分析過程中出錯: {e}")
            raise

    def _find_best_match_by_position(self, ocr_results, position):
        """
        根據位置找到最佳匹配的OCR結果

        Args:
            ocr_results (list): OCR結果
            position (dict): 期望位置 {x, y, width, height}

        Returns:
            dict: 最佳匹配的OCR結果或None
        """
        expected_x = position.get('x', 0)
        expected_y = position.get('y', 0)
        expected_w = position.get('width', 0)
        expected_h = position.get('height', 0)

        # 計算期望的中心點
        expected_center_x = expected_x + expected_w / 2
        expected_center_y = expected_y + expected_h / 2

        best_match = None
        min_distance = float('inf')

        for ocr_item in ocr_results:
            positions = ocr_item['positions']

            # 計算OCR結果框的邊界
            x_vals = [p[0] for p in positions]
            y_vals = [p[1] for p in positions]

            min_x, max_x = min(x_vals), max(x_vals)
            min_y, max_y = min(y_vals), max(y_vals)
            width = max_x - min_x
            height = max_y - min_y

            # 計算OCR結果的中心點
            center_x = min_x + width / 2
            center_y = min_y + height / 2

            # 計算中心點之間的距離
            distance = np.sqrt((center_x - expected_center_x)
                               ** 2 + (center_y - expected_center_y)**2)

            # 更新最佳匹配
            if distance < min_distance:
                min_distance = distance
                best_match = ocr_item

        # 如果距離太遠，則認為沒有匹配
        if min_distance > (expected_w + expected_h) / 2:
            return None

        return best_match

    def _validate_text(self, text, rule_type, expected_text):
        """
        根據規則驗證文字

        Args:
            text (str): 要驗證的文字
            rule_type (str): 規則類型
            expected_text (str): 期望的文字

        Returns:
            dict: 驗證結果
        """
        if rule_type == "exact":
            return {
                'match': text == expected_text,
                'details': f"檢查 '{text}' 是否等於 '{expected_text}'"
            }
        elif rule_type == "contains":
            return {
                'match': expected_text in text,
                'details': f"檢查 '{expected_text}' 是否包含在 '{text}' 中"
            }
        elif rule_type == "startswith":
            return {
                'match': text.startswith(expected_text),
                'details': f"檢查 '{text}' 是否以 '{expected_text}' 開頭"
            }
        elif rule_type == "endswith":
            return {
                'match': text.endswith(expected_text),
                'details': f"檢查 '{text}' 是否以 '{expected_text}' 結尾"
            }
        else:
            return {
                'match': False,
                'details': f"未知規則類型: {rule_type}"
            }

    def _process_multicolumn(self, ocr_results, width):
        """
        Process multi-column text, arranging OCR results in reading order

        Args:
            ocr_results: OCR results from PaddleOCR
            width: Image width
            height: Image height

        Returns:
            Sorted OCR results
        """
        if not ocr_results:
            return []

        # Split image into left and right columns
        half_width = (width / 2) - 100  # Offset to handle overlap

        # Group results by column
        left_column = []
        right_column = []

        for result in ocr_results:
            # Check if the first point (top-left) is in left or right half
            min_x = min(int(p[0]) for p in result['positions'])
            if min_x < half_width:
                left_column.append(result)
            else:
                right_column.append(result)

        # Sort each column by vertical position (y-coordinate)
        # Sort by y-coordinate of top-left point
        left_column.sort(key=lambda x: min(int(p[1]) for p in x['positions']))
        right_column.sort(key=lambda x: min(int(p[1]) for p in x['positions']))

        # Combine left and right columns (read left column first, then right)
        return left_column, right_column

    def _find_max_right_EdgeX(self, left_column_results):
        max_x = -float('inf')
        max_x_column_data = None
        for column in left_column_results:
            if 'positions' in column and column['positions']:
                for x, _ in column['positions']:
                    if int(x) > max_x:
                        max_x = int(x)
                        max_x_column_data = column
        return max_x, max_x_column_data

    def _find_min_left_EdgeX_by_y_range(self, right_column_results, y_min, y_max):
        min_x = float('inf')
        for column in right_column_results:
            if 'positions' in column and column['positions']:
                bbox = column['positions']
                if (bbox[0][1] >= y_min and bbox[0][1] <= y_max):
                    min_x = int(bbox[0][0])
                    break
        return min_x

    def _calc_size(self, left_column_results, right_column_results):
        center_min_x, max_x_item = self._find_max_right_EdgeX(
            left_column_results)
        center_max_x = self._find_min_left_EdgeX_by_y_range(
            right_column_results, max_x_item['positions'][1][1], max_x_item['positions'][2][1])

        center_size = (center_max_x - center_min_x) * 0.027
        return center_size
