from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_IN_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-IN", "840244708115"],
            ["GA05571-IN", "840244708146"],
            ["GA04432-IN-N - 840244710569"],
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


class AK3_IN_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-IN", "840244707750"],
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


class AK3_IN_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-IN", "840244708122"],
            ["GA05572-IN", "840244708153"],
            ["GA04988-IN-N", "840244710576"],
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


class AK3_IN_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-IN", "840244708139"],
            ["GA05573-IN", "840244708160"],
            ["GA05595-IN-N", "840244710583"],
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


class AK3_IN_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-IN", "840244708252"],
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


class AK3_IN_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-IN", "840244708375"],
            ["GA05596-IN", "840244708382"],
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
