from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_US_VZW_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05394-US", "840353922259"],
            ["GA09572-US", "840353922419"],
            ["IQGA05394-US", "840353922570"],
            ["IQGA09572-US", "840353922587"],
            ["IQGA09816-US", "840353923003"],
            ["IQGA09817-US", "840353923072"],
        ]

    def analyze(self, ocr_results, image_width, image_height):
        # Implementation for specific analysis
        try:
            logger.info("分析條碼OCR結果")

            # 初始化結果
            analysis = initialize_analysis()

            # 檢查空結果
            if not ocr_results:
                analysis['errors'].append("未找到OCR結果")
                return analysis

            text_matcher = TextMatcher()

            starting_strings = [
                "Software Version",
                "SKU",
                "EID",
                "SN",
                "IMEI1",
                "IMEI2",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.75)
            date_str_y = int(image_height*0.8)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理開頭字串和數字
            remaining_results = process_starting_strings_and_digits(
                ocr_results_copy, starting_strings, text_matcher, analysis)

            # 如果需要進一步處理剩餘結果，可以在這裡添加

            # 確定整體匹配
            # analysis['match'] = all(result['match'] for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise
