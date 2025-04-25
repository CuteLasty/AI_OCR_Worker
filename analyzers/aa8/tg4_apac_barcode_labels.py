from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_APAC_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-AU", "840353922280"],
            ["GA09563-AU", "840353922334"],
            ["GA09565-AU", "840353922440"],
            ["GA09564-AU", "840353922389"],
            ["GA09566-AU", "840353922495"],
            ["GA09585-AU", "840353922549"],
            ["GA05769-AU-N", "840353922822"],
            ["GA09563-AU-N", "840353922877"],
            ["GA09564-AU-N", "840353922921"],
            ["GA09565-AU-N", "840353922976"]
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
                "進口商：台灣大哥大股份有限公司",
                "地址：110鑫北市信義區煙廠路88號12楼",
                "服務電話：(02)6638-6888",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.5)
            ignore_y = int(image_height*0.4)
            ocr_results_copy = process_ignore_str_type2(
                ocr_results, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.2)
            # date_str_y = int(image_height*0.2)
            date_str_y = get_y_pos_by_text(ocr_results, '地址')
            date_str_YMDD = generate_YMDD()
            ocr_results_copy1 = process_date_str2(
                ocr_results_copy, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理CHT_YYMM日期標籤
            date_str_x = int(image_width*0.6)
            date_str_y = int(image_height*0.8)
            date_str_CHT_YMMM = generate_CHT_YYMM()
            ocr_results_copy2 = find_text_and_process_date_str(
                ocr_results_copy1, '製造日期', date_str_CHT_YMMM, analysis)

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


class TG4_DEMO_APAC_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-AU", "840353923041"],
            ["GA09823-AU", "840353923102"],
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

            starting_strings = [
                "SKU",
                "EID",
                "IMEI1",  # "IMEI2"
            ]

            ignore_string = [
                "進口商：台灣大哥大股份有限公司",
                "地址：110鑫北市信義區煙廠路88號12楼",
                "服務電話：(02)6638-6888",
            ]

            # 處理忽略區域
            ignore_x = int(image_width*0.5)
            ignore_y = int(image_height*0.35)
            ocr_results_copy = process_ignore_str_type2(
                ocr_results, ignore_x, ignore_y, 0)

            # 處理YMDD日期標籤
            date_str_x = int(image_width*0.2)
            date_str_y = get_y_pos_by_text(ocr_results, '地址')
            date_str_YMDD = generate_YMDD()
            ocr_results_copy1 = process_date_str2(
                ocr_results_copy, date_str_YMDD, date_str_x, date_str_y, 0, analysis)

            # 處理CHT_YYMM日期標籤
            date_str_x = int(image_width*0.6)
            date_str_y = int(image_height*0.8)
            date_str_CHT_YMMM = generate_CHT_YYMM()
            ocr_results_copy2 = find_text_and_process_date_str(
                ocr_results_copy1, '製造日期', date_str_CHT_YMMM, analysis)

            # 處理固定字串
            ocr_results_copy3 = process_static_strings(
                ocr_results_copy2, static_strings, analysis)

            # 處理開頭字串和數字
            remaining_results = process_starting_strings_and_digits(
                ocr_results_copy3, starting_strings, text_matcher, analysis)

            # 如果需要進一步處理剩餘結果，可以在這裡添加

            # 確定整體匹配
            # analysis['match'] = all(result['match'] for result in analysis['results'])
            # logger.info(f"條碼分析完成，整體匹配: {analysis['match']}")

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise
