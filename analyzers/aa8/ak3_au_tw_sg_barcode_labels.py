from analyzers.base_label_analyzer import BaseLabelAnalyzer


class AK3_AU_TW_SG_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04432-AU", "840244707996"],
            ["GA05571-AU", "840244708023"],
            ["GA04432-AU-N", "840244710507"],
        ]
        self.static_string = [
            "Obsidian",
            "曜石黑",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_AU_TW_SG_CL1_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05696-AU", "840244710330"]
        ]
        self.static_string = [
            "DEMO",
            "Obsidian",
            "曜石黑",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_AU_TW_SG_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04988-AU", "840244708009"],
            ["GA05572-AU", "840244708030"],
            ["GA04988-AU-N", "840244710286"],
        ]
        self.static_string = [
            "Porcelain",
            "陶瓷米",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_AU_TW_SG_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05570-AU", "840244708016"],
            ["GA05573-AU", "840244708047"],
            ["GA05595-AU-N", "840244710224"],
        ]
        self.static_string = [
            "Bay",
            "海灣藍",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_AU_TW_SG_CL3_Demo_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05697-AU", "840244710491"]
        ]
        self.static_string = [
            "DEMO",
            "Bay",
            "海灣藍",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class AK3_AU_TW_SG_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05595-AU", "840244708337"],
            ["GA05596-AU", "840244708344"],
            ["GA06025-AU-N", "840244710637"]
        ]
        self.static_string = [
            "Aloe",
            "蘆薈綠",
        ]
        self.starting_string = [
            "SKU",
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
