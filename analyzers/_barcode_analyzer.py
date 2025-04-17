from loguru import logger


class BarcodeAnalyzer:
    def __init__(self):
        """
        初始化條碼分析器
        """
        logger.info("初始化BarcodeAnalyzer")

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

            # 提取模板規則
            rules = template.get('rules', [])
            if not rules:
                analysis['errors'].append("模板中未找到規則")
                return analysis

            # 處理每條規則
            for rule in rules:
                rule_type = rule.get('type')
                rule_pattern = rule.get('pattern')

                # 根據規則模式檢查文字內容
                for ocr_item in ocr_results:
                    text = ocr_item['text']

                    # 執行特定規則驗證
                    match_result = self._validate_text(
                        text, rule_type, rule_pattern)

                    analysis['results'].append({
                        'rule': rule,
                        'text': text,
                        'match': match_result['match'],
                        'details': match_result['details']
                    })

            # 確定整體匹配
            analysis['match'] = all(result['match']
                                    for result in analysis['results'])

            logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")
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
