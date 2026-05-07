from loguru import logger

from utils.text_utils import TextMatcher
from analyzers.base_label_analyzer import BaseLabelAnalyzer
from analyzers.utils import create_analyze_result
from analyzers.aa8.date_str_utils import *
from analyzers.aa8.analyzer_utils import *


class TG4_IN_MRP_TEXT_Label(BaseLabelAnalyzer):
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
            ["GA09824-IN", "840353923775"],
            ["GA09825-IN", "840353923782"]
        ]

    def analyze(self, ocr_results, image_width, image_height):
        # Implementation for specific analysis
        try:
            logger.info("分析條碼OCR結果")

            # 初始化結果
            analysis = initialize_analysis('aa8', 'text')

            # 檢查空結果
            if not ocr_results:
                analysis['errors'].append("未找到OCR結果")
                return analysis

            text_matcher = TextMatcher()

            static_string_left = [
                "Commodity: Cellular Phone",
                "Quantity:",
                "1N",
                "(Pixel 9a, Charging Cable, SIM Tool,",
                "Safety/Regulatory Booklet)",
                "Manufactured by: Google LLC 1600 Amphitheatre",
                "Parkway, Mountain View, CA 94043, USA",
                "Country of Origin: Phone made in Vietnam.",
                "Accessories made in China.",
                "Imported by: Google Information Services India Private",
                "Limited. Registered Address: Unit No. 204, 2nd Floor,",
                "Signature Tower-II, Tower A, Sector-15, Part-II, Village",
                "Silokhera, Gurgaon, Haryana, 122001, India.",

            ]
            static_string_right = [
                "Packed by: Compal (Vietnam) Co., Ltd / Công Ty Tnhh",
                "Compal (Việt Nam) Ba Thien Industrial Zone, Ba Hien Town,",
                "Binh Xuyen District, Vinh Phuc Province, Vietnam-15800",
                "Customer Care: For all product-related complaints/",
                "assistance: visit g.co/pixel/support, or call our",
                "Google Support toll free number: 1-800-419-0655",
                "(Mon to Sun 9:00am to 9:00pm) or email us at",
                "googleapac-devicesupport@google.com. Repair partner:",
                "F1 Info Solutions & Services Pvt. Ltd., D-245, D Block,",
                "Sector 63, Noida, Uttar Pradesh, 201301, India.",
                "M.R.P.: ₹ 49,999 (inclusive of all taxes)",
                f"Month & Year of Manufacture: {generate_month_year()}"
            ]

            left_column, right_column = sort_multicolumn(
                ocr_results, image_width)

            process_column(left_column, static_string_left,
                           text_matcher, analysis)

            process_column(right_column, static_string_right,
                           text_matcher, analysis)

            analysis['text'] = {
                'left': static_string_left,
                'right': static_string_right,
            }

            return analysis

        except Exception as e:
            logger.error(f"條碼分析過程中出錯: {e}")
            raise
