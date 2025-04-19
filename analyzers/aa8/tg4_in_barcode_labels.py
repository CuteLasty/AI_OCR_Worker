from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_IN_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09566-IN", "840353922501"],
            ["GA09585-IN", "840353922556"],
            ["GA09584-IN", "840353923324"],
            ["GA09566-IN-N", "840353923751"],
            ["GA09584-IN-N", "840353923737"],
            ["GA09585-IN-N", "840353923768"],
        ]
        self.static_string = []
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = [
            "IS 13252(Part 1)/",
            "IEC 60950-1",
            "IS 16333 (Part 3)",
            "R-41583212",
            "www.bis.gov.in",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_IN_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09824-IN", "840353923775"],
            ["GA09825-IN", "840353923782"]
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
            "IS 13252(Part 1)/",
            "IEC 60950-1",
            "IS 16333 (Part 3)",
            "R-41583212",
            "www.bis.gov.in",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
