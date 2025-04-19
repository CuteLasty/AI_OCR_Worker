from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_JP_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-JP", "840353922303"],
            ["GA09563-JP", "840353922358"],
            ["GA09565-JP", "840353922464"],
            ["GA09564-JP", "840353922402"],
            ["GA09566-JP", "840353922518"],
            ["GA09585-JP", "840353922563"],
            ["GA09584-JP", "840353923317"],
            ["GA09563-JP-N", "840353922891"],
            ["GA09564-JP-N", "840353922945"],
            ["GA09565-JP-N", "840353922990"],
            ["GA05769-JP-N", "840353922846"],
        ]
        self.static_string = []
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = [
            "紙",
            "包裝",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_JP_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-JP", "840353923065"],
            ["GA09823-JP", "840353923126"],
        ]
        self.static_string = [
            "DEMO",
        ]
        self.starting_string = [
            "EID",
            "IMEI1",
            "IMEI2",
            "SKU",
        ]
        self.ignore_string = [
            "紙",
            "包裝",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
