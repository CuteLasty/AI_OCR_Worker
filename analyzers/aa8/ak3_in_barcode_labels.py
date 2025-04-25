from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class AK3_IN_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-IN", "840244708115"],
            ["GA05571-IN", "840244708146"],
            ["GA04432-IN-N", "840244710569"],
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
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_IN_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-IN", "840244707750"],
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
                "Obsidian",
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_IN_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-IN", "840244708122"],
            ["GA05572-IN", "840244708153"],
            ["GA04988-IN-N", "840244710576"],
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
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_IN_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-IN", "840244708139"],
            ["GA05573-IN", "840244708160"],
            ["GA05595-IN-N", "840244710583"],
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
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_IN_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-IN", "840244708252"],
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
                "Bay",
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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


class AK3_IN_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-IN", "840244708375"],
            ["GA05596-IN", "840244708382"],
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
                "Aloe"
            ]

            starting_string = [
                "SKU",
                "IMEI1",  # "IMEI2"
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width/5*3)
            date_str_y = int(image_height/2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

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
