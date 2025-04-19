from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_US_ATnT_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05567-US", "840244707811", "6074E"],
            ["GA05584-US", "840244707842", "6074E"]
        ]
        self.static_string = [
            "Pixel 8a | Obsidian | 128G*",
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

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


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

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
