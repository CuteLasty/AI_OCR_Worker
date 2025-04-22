from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import generate_MMDDYYYY
from analyzers.aa8.analyzer_utils import *


class AK3_US_TMO_CL1_128G_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05564-US", "840244707750"],
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
                "Pixel 8a",
                "Obsidian",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL1_128G_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-US", "840244710811"],
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
                "Pixel 8a DEMO",
                "Obsidian",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05565-US", "840244707767"],
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
                "Pixel 8a",
                "Porcelain",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05566-US", "840244707774"],
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
                "Pixel 8a",
                "Bay",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-US", "840244710804"],
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
                "Pixel 8a DEMO",
                "Bay",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05591-US", "840244708252"],
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
                "Pixel 8a",
                "Aloe",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class AK3_US_TMO_CL1_256G_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05581-US", "840244707781"],
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
                "Pixel 8a",
                "Obsidian",
                "5G Sub-6* | 256 GB**",
                "Phone made in Vietnam",
                "Accessories made in China",
            ]

            starting_string = [
                "S/W",
                "H/W",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
                "EID",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.7)
            # date_str_y = int(image_height/2)
            date_str_y = 0
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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
