from loguru import logger

from utils.text_utils import TextMatcher


class BarcodeAnalyzer:
    def __init__(self):
        """
        初始化條碼分析器
        """
        logger.info("初始化BarcodeAnalyzer")

        # Initialize components
        self.text_matcher = TextMatcher()

    def analyze(self, ocr_results, template):
        """
        根據模板分析條碼OCR結果

        Args:
            ocr_results (list): OCR結果
            template (dict): 模板規格

        Returns:
            dict: 分析結果
        """
        try:
            logger.info("分析條碼OCR結果")

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
######
            template_texts = template[1]  # Static template texts
            # Special template texts (barcodes, etc.)
            special_texts = template[2]
            ignore_texts = template[3]  # Texts to ignore

            ocr_results_copy = []
            for line in ocr_results:
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
######
            # 確定整體匹配
            # analysis['match'] = all(result['match']
            #                        for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")
            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise

    def _validate_text(self, text, rule_type, pattern):
        """
        根據規則驗證文字

        Args:
            text (str): 要驗證的文字
            rule_type (str): 規則類型
            pattern (str): 匹配模式

        Returns:
            dict: 驗證結果
        """
        # 這將為實際驗證邏輯擴展
        if rule_type == "contains":
            return {
                'match': pattern in text,
                'details': f"檢查 '{pattern}' 是否在 '{text}' 中"
            }
        elif rule_type == "exact":
            return {
                'match': pattern == text,
                'details': f"檢查 '{pattern}' 是否等於 '{text}'"
            }
        elif rule_type == "startswith":
            return {
                'match': text.startswith(pattern),
                'details': f"檢查 '{text}' 是否以 '{pattern}' 開頭"
            }
        else:
            return {
                'match': False,
                'details': f"未知規則類型: {rule_type}"
            }
