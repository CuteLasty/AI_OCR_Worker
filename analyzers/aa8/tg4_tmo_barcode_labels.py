from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import generate_MMDDYYYY
from analyzers.aa8.analyzer_utils import *

class TG4_CLR1_128GB_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09567-US", "840353921986"]
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
                "Pixel 9a | Obsidian",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_CLR1_256GB_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09579-US", "840353922006"]
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
                "Pixel 9a | Obsidian",
                "5G Sub-6* | 256GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_CLR2_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09570-US", "840353921993"]
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
                "Pixel 9a | Porcelain",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_CLR3_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09573-US", "840353922013"]
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
                "Pixel 9a | Iris",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_CLR4_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []

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
                "Pixel 9a | Peony",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_DEMO_CLR1_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09820-US", "840353922068"]]

    def analyze(self, ocr_results, image_width, image_height):
        # "Pixel 9a Demo | Obsidian",
        # "S/W: RD1A.200810.022.A4",
        # "I H/W: MP1.0",
        # "5G Sub-6* | 128 GB**",
        # " Phone made in Vietnam.",
        # " Accessories made in China.",
        # "EID: 00000000000000000000000000000002",
        # "000000840353922068",
        # "IMEi1: 000000000012345",
        # "01/03/2025",
        # "TMO SKU: 840353922068",
        # "IMEI2: 123450000000000",

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
                "Pixel 9a Demo | Obsidian",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_strings = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
            date_str_MMDDYYYY = generate_MMDDYYYY()
            ocr_results_copy = process_date_str(
                ocr_results, date_str_MMDDYYYY, date_str_x, date_str_y, 0, analysis)

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


class TG4_DEMO_CLR1_TMO_HQ_Units_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09824-US", "840353923010"]
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
                "Pixel 9a Demo SUO | Obsidian",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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


class TG4_DEMO_CLR3_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []

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
                "Pixel 9a Demo | Iris",
                "5G Sub-6* | 128 GB**",
                "Phone made in Vietnam.",
                "Accessories made in China."
            ]

            starting_string = [
                "S/W",
                "H/W",
                "EID",
                "IMEI1",
                "IMEI2",
                "TMO SKU",
            ]

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.8)
            date_str_y = int(image_height*0.5)
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
