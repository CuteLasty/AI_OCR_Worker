from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_CLR1_128_ATT_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09568-US", "840353921818", "6792E"]
        ]
        self.static_string = [
            "Pixel 9a | 128 GB** | Obsidian",
        ]
        self.starting_string = [
            "OS ver.: Android 15 | S/W: RD1A.200810.022.A4 | H/W: MP1.0",
            "EID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR2_128_ATT_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []
        self.static_string = [
            "Pixel 9a | 128GB** | Porcelain",
        ]
        self.starting_string = [
            "OS ver.: Android 15 | S/W: RD1A.200810.022.A4 | H/W: MP1.0",
            "EID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR3_128_ATT_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []
        self.static_string = [
            "Pixel 9a | 128GB** | Iris",
        ]
        self.starting_string = [
            "OS ver.: Android 15 | S/W: RD1A.200810.022.A4 | H/W: MP1.0",
            "EID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_CLR1_128_ATT_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09818-US", "840353921870", "D792E"]
        ]
        self.static_string = [
            "DEMO Pixel 9a | 128GB** | Obsidian",
        ]
        self.starting_string = [
            "OS ver.: Android",
            "EID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_CLR3_128_ATT_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []
        self.static_string = [
            "DEMO Pixel 9a | 128GB** | Iris",
        ]
        self.starting_string = [
            "OS ver.: Android 15 | S/W: RD1A.200810.022.A4 | H/W: MP1.0",
            "EID",
            "IMEI1",
            "IMEI2",
            "AT&T SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
