from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import generate_YMDD
from analyzers.aa8.analyzer_utils import *


class AK3_US_VZW_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04385-US", "840244707699"],
            ["GA05578-US", "840244707729"],
            ["IQGA04385-US", "840244708177"],
            ["IQGA05578-US", "840244708207"],
            ["IQGA05696-US", "840244711368 "],
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
                "Obsidian"
            ]

            starting_string = [
                "SKU",
                "EID",
                "IMEI1",
                "IMEI2",
                "SN",
                "Software Version",
            ]

            # 處理固定字串
            ocr_results_copy1 = process_static_strings(
                ocr_results, static_strings, analysis)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            # date_str_y = int(image_height*0.4)  # fix: add a check callback for process_date_str()
            date_str_y = 0
            date_str_YMDD = generate_YMDD()
            ocr_results_copy2 = process_date_str(
                ocr_results_copy1, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_VZW_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05562-US", "840244707705"],
            ["GA05579-US", "840244707736"],
            ["IQGA05562-US", "840244708184"],
            ["IQGA05579-US", "840244708214"],
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
                "Porcelain"
            ]

            starting_string = [
                "SKU",
                "EID",
                "IMEI1",
                "IMEI2",
                "SN",
                "Software Version",
            ]

            # 處理固定字串
            ocr_results_copy1 = process_static_strings(
                ocr_results, static_strings, analysis)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            # date_str_y = int(image_height*0.4)  # fix: add a check callback for process_date_str()
            date_str_y = 0
            date_str_YMDD = generate_YMDD()
            ocr_results_copy2 = process_date_str(
                ocr_results_copy1, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_VZW_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05563-US", "840244707712"],
            ["GA05580-US", "840244707743"],
            ["IQGA05563-US", "840244708191"],
            ["IQGA05580-US", "840244708221"],
            ["IQGA05697-US", "840244711375"],
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
                "Bay"
            ]

            starting_string = [
                "SKU",
                "EID",
                "IMEI1",
                "IMEI2",
                "SN",
                "Software Version",
            ]

            # 處理固定字串
            ocr_results_copy1 = process_static_strings(
                ocr_results, static_strings, analysis)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            # date_str_y = int(image_height*0.4)  # fix: add a check callback for process_date_str()
            date_str_y = 0
            date_str_YMDD = generate_YMDD()
            ocr_results_copy2 = process_date_str(
                ocr_results_copy1, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_VZW_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05589-US", "840244708238"],
            ["GA05590-US", "840244708245"],
            ["IQGA05589-US", "840244708399"],
            ["IQGA05590-US", "840244708405"],
        ]
        self.static_string = [
            "Aloe",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
            "SN",
            "Software Version",
        ]
        self.ignore_string = []

    def analyze(self, ocr_results, image_width, image_height):
        pass
