from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_JP_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-JP", "840244708054"],
            ["GA05571-JP", "840244708085"],
            ["GA04432-JP-N", "840244710354"],
        ]
        self.static_string = [
            "Obsidian",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_JP_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-JP", "840244710262"],
        ]
        self.static_string = [
            "DEMO",
            "Obsidian",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_JP_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-JP", "840244708061"],
            ["GA05572-JP", "840244708092"],
            ["GA04988-JP-N", "840244710231"],
        ]
        self.static_string = [
            "Porcelain",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_JP_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-JP", "840244708078"],
            ["GA05573-JP", "840244708108"],
            ["GA05595-JP-N", "840244710392"],
        ]
        self.static_string = [
            "Bay",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_JP_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-JP", "840244710385"],
        ]
        self.static_string = [
            "DEMO",
            "Bay",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_JP_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-JP", "840244708351"],
            ["GA05596-JP", "840244708368"],
            ["GA06025-JP-N", "840244710613"],
        ]
        self.static_string = [
            "Aloe",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
