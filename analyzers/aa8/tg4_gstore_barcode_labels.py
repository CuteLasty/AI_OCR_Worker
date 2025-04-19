from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_GSTORE_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-US", "840353922266"],
            ["GA09563-US", "840353922310"],
            ["GA09565-US", "840353922426"],
            ["GA09564-US", "840353922365"],
            ["GA09566-US", "840353922471"],
            ["GA09585-US", "840353922525"],
            ["GA05769-US-Q", "840353922792"],
            ["GA05769-US-N", "840353922808"],
            ["GA09563-US-N", "840353922853"],
            ["GA09564-US-N", "840353922907"],
            ["GA09565-US-N", "840353922952"],
        ]
        self.static_string = []
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


class TG4_DEMO_GSTORE_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-US", "840353923027"],
            ["GA09823-US", "840353923089"],
        ]
        self.static_string = [
            "DEMO",
        ]
        self.starting_string = [
            "IMEI1",
            "IMEI2",
            "EID",
            "SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
