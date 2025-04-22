from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import generate_YMDD
from analyzers.aa8.analyzer_utils import *


class AK3_US_ATnT_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05567-US", "840244707811", "6074E"],
            # ["GA05584-US", "840244707842", "6074E"]
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
                "Pixel 8a | Obsidian | 128G*",
                "*Actual formatted",
                "storage capacity less",
                date_str_YMDD
            ]
            starting_strings = [
                "OS ver",
                "ICCID",
                "IMEI1",
                "IMEI2",
                "AT&T SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            # date_str_x = int(image_width/5*3)
            # date_str_y = int(image_height/2)
            # date_str_YMDD = generate_YMDD()
            # ocr_results_copy = process_date_str(
            #    ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results, static_strings, analysis)

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


class AK3_US_ATnT_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05695-US", "840244710743", "D074E",]
        ]
        self.static_string = [
            "DEMO",
            "Pixel 8a",
            "Obsidian | 128G*",
            "*Actual formatted",
            "storage capacity less",
        ]
        self.starting_string = [
            "OS ver: Android 15 | SW",
            "ICCID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
            "EID",
        ]
        self.ignore_string = []

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
                "Pixel 8a",
                "Obsidian | 128G*",
                "*Actual formatted",
                "storage capacity less",
                date_str_YMDD
            ]
            starting_strings = [
                "OS ver",
                "ICCID",
                "IMEI1",
                "IMEI2",
                "AT&T SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            # date_str_x = int(image_width/5*3)
            # date_str_y = int(image_height/2)
            # date_str_YMDD = generate_YMDD()
            # ocr_results_copy = process_date_str(
            #    ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理固定字串
            ocr_results_copy2 = process_static_strings(
                ocr_results, static_strings, analysis)

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
