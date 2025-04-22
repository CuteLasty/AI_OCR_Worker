from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import generate_YMDD
from analyzers.aa8.analyzer_utils import *


class TG4_GSTORE_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-US", "840353922266"],
            ["GA09563-US", "840353922310"],
            ["GA09565-US", "840353922426"],
            ["GA09564-US", "840353922365"],
            ["GA09566-US", "840353922471"],
            ["GA09585-US", "840353922525"],
            ["GA05769-US-Q", "840353922792"],
            ["GA05769-US-N", "840353922808"],
            ["GA09563-US-N", "840353922853"],
            ["GA09564-US-N", "840353922907"],
            ["GA09565-US-N", "840353922952"],
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
                "SKU",
                "EID",
                "IMEI1",  # "IMEI2"
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


class TG4_DEMO_GSTORE_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-US", "840353923027"],
            ["GA09823-US", "840353923089"],
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

            static_strings = [
                "DEMO"
            ]

            starting_strings = [
                "SKU",
                "EID",
                "IMEI1",  # "IMEI2"
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.75)
            date_str_y = int(image_height*0.8)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results_copy, static_strings, analysis)

            # 處理開頭字串和數字
            remaining_results = process_starting_strings_and_digits(
                ocr_results_copy2, starting_strings, text_matcher, analysis)

            # 如果需要進一步處理剩餘結果，可以在這裡添加

            # 確定整體匹配
            # analysis['match'] = all(result['match'] for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise
