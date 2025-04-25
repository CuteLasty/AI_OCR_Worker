from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_IN_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09566-IN", "840353922501"],
            ["GA09585-IN", "840353922556"],
            ["GA09584-IN", "840353923324"],
            ["GA09566-IN-N", "840353923751"],
            ["GA09584-IN-N", "840353923737"],
            ["GA09585-IN-N", "840353923768"],
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

            date_str_YMDD = generate_YMDD()
            static_strings = [
                date_str_YMDD
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            ignore_string = [
                "IS 13252(Part 1)/",
                "IEC 60950-1",
                "IS 16333 (Part 3)",
                "R-41583212",
                "www.bis.gov.in",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.45)
            ignore_y = 0
            ocr_results_copy = process_ignore_str_type1(
                ocr_results, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            # date_str_x = int(image_width/5*3)
            # date_str_y = int(image_height/2)
            # date_str_YMDD = generate_YMDD()
            # ocr_results_copy = process_date_str(
            #    ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results_copy, static_strings, analysis)

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


class TG4_DEMO_IN_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09824-IN", "840353923775"],
            ["GA09825-IN", "840353923782"]
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

            date_str_YMDD = generate_YMDD()
            static_strings = [
                "DEMO",
                date_str_YMDD
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            ignore_string = [
                "IS 13252(Part 1)/",
                "IEC 60950-1",
                "IS 16333 (Part 3)",
                "R-41583212",
                "www.bis.gov.in",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.45)
            ignore_y = 0
            ocr_results_copy = process_ignore_str_type1(
                ocr_results, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            # date_str_x = int(image_width/5*3)
            # date_str_y = int(image_height/2)
            # date_str_YMDD = generate_YMDD()
            # ocr_results_copy = process_date_str(
            #    ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results_copy, static_strings, analysis)

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
