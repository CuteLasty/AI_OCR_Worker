from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_US_VZW_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05394-US", "840353922259"],
            ["GA09572-US", "840353922419"],
            ["IQGA05394-US", "840353922570"],
            ["IQGA09572-US", "840353922587"],
            ["IQGA09816-US", "840353923003"],
            ["IQGA09817-US", "840353923072"],
        ]
        self.static_string = []
        self.starting_string = [
            "Software Version:",
            "SKU",
            "EID",
            "SN",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
