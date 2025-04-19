from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_US_GSTORE_CA_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-US", "840244707873"],
            ["GA05571-US", "840244707903"],
            ["GA04432-US-N", "840244710347"],
            ["GA04432-US-Q", "840244710453"]
        ]
        self.static_string = [
            "Obsidian",
            "Noir",
            "volcanique",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_GSTORE_CA_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-CA", "840244710293"]
        ]
        self.static_string = [
            "Obsidian",
            "Noir",
            "volcanique",
            "DEMO",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_GSTORE_CA_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-CA", "840244710439"]
        ]
        self.static_string = [
            "Bay",
            "Baie",
            "DEMO",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_GSTORE_CA_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-US", "840244707880"],
            ["GA05572-US", "840244707910"],
            ["GA04988-US-N", "840244710187"]
        ]
        self.static_string = [
            "Porcelain",
            "Porcelaine",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_GSTORE_CA_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-US", "840244707897"],
            ["GA05573-US", "840244707927"],
            ["GA05595-US-N", "840244710194"]
        ]
        self.static_string = [
            "Bay",
            "Baie",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_US_GSTORE_CA_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-US", "840244708290"],
            ["GA05596-US", "840244708306"],
            ["GA06025-US-N", "840244710590"]
        ]
        self.static_string = [
            "Aloe",
            "Aloès",
        ]
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
