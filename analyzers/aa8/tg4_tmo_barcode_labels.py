from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_CLR1_128GB_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09567-US", "840353921986"]
        ]
        self.static_string = [
            "Pixel 9a | Obsidian",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR1_256GB_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09579-US", "840353922006"]
        ]
        self.static_string = [
            "Pixel 9a | Obsidian",
            "5G Sub-6* | 256GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR2_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09570-US", "840353921993"]
        ]
        self.static_string = [
            "Pixel 9a | Porcelain",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR3_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09573-US", "840353922013"]
        ]
        self.static_string = [
            "Pixel 9a | Iris",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_CLR4_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []
        self.static_string = [
            "Pixel 9a | Peony",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_CLR1_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09820-US", "840353922068"]]
        self.static_string = [
            "Pixel 9a Demo | Obsidian",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_CLR1_TMO_HQ_Units_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09824-US", "840353923010"]
        ]
        self.static_string = [
            "Pixel 9a Demo | Obsidian",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_CLR3_TMO_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = []
        self.static_string = [
            "Pixel 9a Demo | Iris",
            "5G Sub-6* | 128GB**",
            "Phone made in Vietnam."
            "Accessories made in China."
        ]
        self.starting_string = [
            "S/W",
            "H/W",
            "EID",
            "IMEI1",
            "IMEI2",
            "TMO SKU",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
