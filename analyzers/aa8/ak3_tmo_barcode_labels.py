from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_US_TMO_CL1_128G_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05564-US", "840244707750"],
        ]
        self.static_string = [
            "Pixel 8a",
            "Obsidian",
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        T-Mobile 特有的標籤分析方法

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

        # 檢查 T-Mobile 特有的標記
        if "tmo" in ocr_text or "t-mobile" in ocr_text:
            base_result["match_score"] += 5
            base_result["extracted_data"]["carrier"] = "T-Mobile"

        # 尋找 T-Mobile 特有的 UPC 條碼格式
        # T-Mobile 通常使用 UPC 而不是 SKU
        if "upc" in ocr_text:
            try:
                index = ocr_text.index("upc")
                end_index = ocr_text.find('\n', index)
                if end_index == -1:
                    end_index = len(ocr_text)

                upc = ocr_text[index + len("upc"):end_index].strip(": ")
                if upc and upc.isdigit() and len(upc) >= 12:  # UPC 通常是 12 位數
                    base_result["extracted_data"]["UPC"] = upc
            except:
                pass

        # 檢查 5G Sub-6 特有描述
        if "5g sub-6" in ocr_text:
            base_result["match_score"] += 2
            base_result["extracted_data"]["network"] = "5G Sub-6"

        return base_result


class AK3_US_TMO_CL1_128G_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-US", "840244710811"],
        ]
        self.static_string = [
            "Pixel 8a DEMO",
            "Obsidian",
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_TMO_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05565-US", "840244707767"],
        ]
        self.static_string = [
            "Pixel 8a",
            "Porcelain",
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_TMO_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05566-US", "840244707774"],
        ]
        self.static_string = [
            "Pixel 8a",
            "Bay",
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_TMO_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-US", "840244710804"],
        ]
        self.static_string = [
            "Pixel 8a DEMO",
            "Bay"
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_TMO_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05591-US", "840244708252"],
        ]
        self.static_string = [
            "Pixel 8a",
            "Aloe",
            "5G Sub-6* | 128 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_TMO_CL1_256G_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05581-US", "840244707781"],
        ]
        self.static_string = [
            "Pixel 8a",
            "Obsidian",
            "5G Sub-6* | 256 GB**",
            "Phone made in Vietnam",
            "Accessories made in China",
        ]
        self.starting_string = [
            "SW",
            "HW",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
