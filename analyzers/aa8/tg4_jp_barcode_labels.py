from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_JP_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-JP", "840353922303"],
            ["GA09563-JP", "840353922358"],
            ["GA09565-JP", "840353922464"],
            ["GA09564-JP", "840353922402"],
            ["GA09566-JP", "840353922518"],
            ["GA09585-JP", "840353922563"],
            ["GA09584-JP", "840353923317"],
            ["GA09563-JP-N", "840353922891"],
            ["GA09564-JP-N", "840353922945"],
            ["GA09565-JP-N", "840353922990"],
            ["GA05769-JP-N", "840353922846"],
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

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            ignore_string = [
                "紙",
                "包裝",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.7)
            ignore_y = int(image_height*0.5)
            # ocr_results_copy = process_ignore_str_type1(
            #    ocr_results, ignore_x, ignore_y, 0)
            ocr_results_copy = process_region_str(
                ocr_results, ignore_string, ignore_x, ignore_y, Direction.LOWER_RIGHT, 0, analysis)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.3)
            date_str_y = int(image_height*0.2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy1 = process_date_str2(
                ocr_results_copy, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理開頭字串和數字
            remaining_results = process_starting_strings_and_digits(
                ocr_results_copy1, starting_string, text_matcher, analysis)

            # 如果需要進一步處理剩餘結果，可以在這裡添加

            # 確定整體匹配
            # analysis['match'] = all(result['match'] for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise


class TG4_DEMO_JP_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-JP", "840353923065"],
            ["GA09823-JP", "840353923126"],
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
                "DEMO",
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            ignore_string = [
                "紙",
                "包裝",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.7)
            ignore_y = int(image_height*0.5)
            # ocr_results_copy = process_ignore_str_type1(
            #    ocr_results, ignore_x, ignore_y, 0)
            ocr_results_copy = process_region_str(
                ocr_results, ignore_string, ignore_x, ignore_y, Direction.LOWER_RIGHT, 0, analysis)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.3)
            date_str_y = int(image_height*0.2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy1 = process_date_str2(
                ocr_results_copy, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results_copy1, static_strings, analysis)

            # 處理開頭字串和數字
            remaining_results = process_starting_strings_and_digits(
                ocr_results_copy2, starting_string, text_matcher, analysis)

            # 如果需要進一步處理剩餘結果，可以在這裡添加

            # 確定整體匹配
            # analysis['match'] = all(result['match'] for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise
