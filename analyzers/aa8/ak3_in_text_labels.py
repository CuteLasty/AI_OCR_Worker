from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_IN_MRP_128G_TEXT_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-IN", "840244708115"],
            ["GA04988-IN", "840244708122"],
            ["GA05570-IN", "840244708139"],
            ["GA05595-IN", "840244708375"],
            ["GA05696-IN", "840244707750"],
            ["GA05697-IN", "840244708252"],
        ]
        self.static_string = [
            "Commodity: Cellular Phone",
            "Quantity: 1N",
            "(Pixel 8a, Charging Cable, Quick Switch Adapter,",
            "Warranty Booklet, SIM Tool, Quick Start Guide)",
            "Manufactured by: Google LLC, 1600 Amphitheatre Parkway,",
            "Mountain View, CA 94043, United States.",
            "Packed by: Compal (Vietnam) Co., Ltd / Công Ty Tnhh Compal",
            "(Việt Nam) Ba Thien Industrial Zone, Ba Hien Town, Binh Xuyen",
            "District, Vinh Phuc Province, Vietnam-15800.",
            "Imported by: Google Information Services India Private Limited,",
            "Unit No. 204, 2nd Floor Signature Tower-II, Tower A, Sector-15,",
            "Part-II, Village Silokhera, Gurgaon, Haryana, 122001, India.",
            "#####",
            "Customer Care: For all product-related",
            "complaints/assistance: visit g.co/pixel/support, or",
            "call our Google Support toll free number:",
            "1-800-419-0655 (Mon to Sun 9:00am to 9:00pm) or",
            "email us at googleapac-devicesupport@google.com.",
            "Repair partner: F1 Info Solutions & Services Pvt. Ltd.,",
            "D-245, D Block, Sector 63, Noida, Uttar Pradesh,",
            "201301, India.",
            "Country of Origin: Phone made in Vietnam.",
            "Accessories made in China.",
            "MRP: ₹52,999 (inclusive of all taxes)",
            "Month & Year of Manufacture: June, 2024",
        ]
        self.starting_string = []
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        印度零售價格標籤特有的分析方法

        Args:
            ocr_result: OCR 文本結果

        Returns:
            字典，包含匹配分數和提取的數據
        """
        # 首先調用基類的分析方法獲取基本結果
        base_result = super().analyze(ocr_result)

        if not ocr_result:
            return base_result

        ocr_text = ocr_result.lower()

        # 檢查印度特有標記
        if "mrp" in ocr_text or "₹" in ocr_text:
            base_result["match_score"] += 5
            base_result["extracted_data"]["region"] = "India"

        # 提取 MRP (最高零售價格) 信息
        if "mrp" in ocr_text or "₹" in ocr_text:
            try:
                # 尋找價格
                index = ocr_text.find("₹")
                if index == -1:
                    index = ocr_text.find("mrp")
                    if index != -1:
                        index = ocr_text.find(":", index) + 1

                if index != -1:
                    end_index = ocr_text.find("\n", index)
                    if end_index == -1:
                        end_index = ocr_text.find("(", index)
                    if end_index == -1:
                        end_index = len(ocr_text)

                    price = ocr_text[index:end_index].strip()
                    base_result["extracted_data"]["MRP"] = price
            except:
                pass

        # 提取製造日期
        if "manufacture" in ocr_text:
            try:
                index = ocr_text.find("manufacture")
                if index != -1:
                    index = ocr_text.find(":", index) + 1
                    end_index = ocr_text.find("\n", index)
                    if end_index == -1:
                        end_index = len(ocr_text)

                    mfg_date = ocr_text[index:end_index].strip()
                    base_result["extracted_data"]["Manufacture Date"] = mfg_date
            except:
                pass

        # 檢查存儲容量特徵
        if "128" in ocr_text and "gb" in ocr_text:
            base_result["match_score"] += 2
            base_result["extracted_data"]["storage"] = "128GB"

        return base_result


class AK3_IN_MRP_256G_TEXT_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05571-IN", "840244708146"],
            ["GA05696-IN", "840244707750"],
            ["GA05697-IN", "840244708252"]
        ]
        self.static_string = [
            "Commodity: Cellular Phone",
            "Quantity: 1N",
            "(Pixel 8a, Charging Cable, Quick Switch Adapter,",
            "Warranty Booklet, SIM Tool, Quick Start Guide)",
            "Manufactured by: Google LLC, 1600 Amphitheatre Parkway,",
            "Mountain View, CA 94043, United States.",
            "Packed by: Compal (Vietnam) Co., Ltd / Công Ty Tnhh Compal",
            "(Việt Nam) Ba Thien Industrial Zone, Ba Hien Town, Binh Xuyen",
            "District, Vinh Phuc Province, Vietnam-15800.",
            "Imported by: Google Information Services India Private Limited,",
            "Unit No. 204, 2nd Floor Signature Tower-II, Tower A, Sector-15,",
            "Part-II, Village Silokhera, Gurgaon, Haryana, 122001, India.",
            "#####",
            "Customer Care: For all product-related",
            "complaints/assistance: visit g.co/pixel/support, or",
            "call our Google Support toll free number:",
            "1-800-419-0655 (Mon to Sun 9:00am to 9:00pm) or",
            "email us at googleapac-devicesupport@google.com.",
            "Repair partner: F1 Info Solutions & Services Pvt. Ltd.,",
            "D-245, D Block, Sector 63, Noida, Uttar Pradesh,",
            "201301, India.",
            "Country of Origin: Phone made in Vietnam.",
            "Accessories made in China.",
            "MRP: ₹59,999 (inclusive of all taxes)",
            "Month & Year of Manufacture: June, 2024",
        ]
        self.starting_string = []
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
