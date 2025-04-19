from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_EMEA_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-GB", "0840244707934"],
            ["GA05571-GB", "0840244707965"],
            ["GA04432-GB-N", "0840244710446"]
        ]
        self.static_string = [
            "Obsidian",
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


class AK3_EMEA_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-GB", "0840244710309"],
        ]
        self.static_string = [
            "DEMO",
            "Obsidian",
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


class AK3_EMEA_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-GB", "0840244707941"],
            ["GA05572-GB", "0840244707972"],
            ["GA04988-GB-N", "0840244710200"]
        ]
        self.static_string = [
            "Porcelain",
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


class AK3_EMEA_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-GB", "0840244707958"],
            ["GA05573-GB", "0840244707989"],
            ["GA05595-GB-N", "0840244710408"]
        ]
        self.static_string = [
            "Bay",
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


class AK3_EMEA_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-GB", "0840244710248"],
        ]
        self.static_string = [
            "DEMO",
            "Bay",
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


class AK3_EMEA_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-GB", "0840244708313"],
            ["GA05596-GB", "0840244708320"],
            ["GA06025-GB-N", "0840244710606"]
        ]
        self.static_string = [
            "Aloe",
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
