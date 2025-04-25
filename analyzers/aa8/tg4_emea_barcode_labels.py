from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_EMEA_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-GB", "0840353922273"],
            ["GA09563-GB", "0840353922327"],
            ["GA09565-GB", "0840353922433"],
            ["GA09564-GB", "0840353922372"],
            ["GA09566-GB", "0840353922488"],
            ["GA09585-GB", "0840353922532"],
            ["GA05769-GB-N", "0840353922815"],
            ["GA09563-GB-N", "0840353922860"],
            ["GA09564-GB-N", "0840353922914"],
            ["GA09565-GB-N", "0840353922969"]
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
                "EID",
                "IMEI1",  # "IMEI2"
            ]

            ignore_string = [
                "AT,BE,BG,CY,CZ,DE,DK,EE,EL,ES,FI,FR,HR,HU,IE,IT,LT,",
                "LU,LV,MT,NL,PL,PT,RO,SE,SI,SK,UK(NI),CH,IS,LI,NO,TR.",
                "g.co/envinfo",
                "PAP",
                "UK",
                "CA",
                "CE",
                "FR",
                "ELEMENTS",
                "D'EMBALLAGE",
                "+ NOTIOE",
                "BAD",
                "DE",
                "TRI",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.45)
            ignore_y = 0
            ocr_results_copy = process_ignore_str_type1(
                ocr_results, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.2)
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


class TG4_DEMO_EMEA_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-GB", "0840353923034"],
            ["GA09823-GB", "0840353923096"],
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
                "EID",
                "IMEI1",  # "IMEI2"
            ]

            ignore_string = [
                "AT,BE,BG,CY,CZ,DE,DK,EE,EL,ES,FI,FR,HR,HU,IE,IT,LT,",
                "LU,LV,MT,NL,PL,PT,RO,SE,SI,SK,UK(NI),CH,IS,LI,NO,TR.",
                "g.co/envinfo",
                "PAP",
                "UK",
                "CA",
                "CE",
                "FR",
                "ELEMENTS",
                "D'EMBALLAGE",
                "+ NOTIOE",
                "BAD",
                "DE",
                "TRI",
            ]

            # 處理固定字串
            ocr_results_copy = process_one_static_strings(
                ocr_results, static_strings[0], analysis)

            # 處理忽略區域
            ignore_x = int(image_width*0.45)
            ignore_y = 0
            ocr_results_copy1 = process_ignore_str_type1(
                ocr_results_copy, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.2)
            date_str_y = int(image_height*0.2)
            date_str_YMDD = generate_YMDD()
            ocr_results_copy2 = process_date_str2(
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
