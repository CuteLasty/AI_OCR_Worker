import numpy as np
from loguru import logger

class TextAnalyzer:
    def __init__(self):
        """
        初始化文字分析器
        """
        logger.info("初始化TextAnalyzer")
    
    def analyze(self, ocr_results, template):
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
                
            # 提取模板規則
            rules = template.get('rules', [])
            if not rules:
                analysis['errors'].append("模板中未找到規則")
                return analysis
                
            # 處理每條規則
            matches = []
            for rule in rules:
                rule_type = rule.get('type')
                expected_text = rule.get('text', '')
                position = rule.get('position', {})
                
                # 尋找位置上最匹配的OCR結果
                best_match = None
                if position:
                    best_match = self._find_best_match_by_position(ocr_results, position)
                
                # 如果找到了位置匹配，驗證文字內容
                if best_match:
                    match_result = self._validate_text(best_match['text'], rule_type, expected_text)
                    
                    analysis['results'].append({
                        'rule': rule,
                        'text': best_match['text'],
                        'match': match_result['match'],
                        'details': match_result['details'],
                        'position': best_match['positions']
                    })
                    
                    matches.append(match_result['match'])
                else:
                    # 沒有找到位置匹配，但仍然檢查是否有文字匹配
                    any_text_match = False
                    for ocr_item in ocr_results:
                        match_result = self._validate_text(ocr_item['text'], rule_type, expected_text)
                        if match_result['match']:
                            any_text_match = True
                            analysis['results'].append({
                                'rule': rule,
                                'text': ocr_item['text'],
                                'match': True,
                                'details': match_result['details'],
                                'position': ocr_item['positions']
                            })
                            break
                    
                    if not any_text_match:
                        analysis['results'].append({
                            'rule': rule,
                            'text': '',
                            'match': False,
                            'details': f"未找到匹配的文本位置和內容",
                            'position': None
                        })
                        
                        matches.append(False)
            
            # 確定整體匹配
            analysis['match'] = all(matches) if matches else False
            
            logger.info(f"文字分析完成，整體匹配: {analysis['match']}")
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
            distance = np.sqrt((center_x - expected_center_x)**2 + (center_y - expected_center_y)**2)
            
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
