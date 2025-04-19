from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_APAC_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-AU", "840353922280"],
            ["GA09563-AU", "840353922334"],
            ["GA09565-AU", "840353922440"],
            ["GA09564-AU", "840353922389"],
            ["GA09566-AU", "840353922495"],
            ["GA09585-AU", "840353922549"],
            ["GA05769-AU-N", "840353922822"],
            ["GA09563-AU-N", "840353922877"],
            ["GA09564-AU-N", "840353922921"],
            ["GA09565-AU-N", "840353922976"]
        ]
        self.static_string = []
        self.starting_string = [
            "SKU",
            "IMEI1",
            "IMEI2",
            "EID",
            "製造日期",
        ]
        self.ignore_string = [
            "進口商：台灣大哥大股份有限公司",
            "地址：110鑫北市信義區煙廠路88號12楼",
            "服務電話：(02)6638-6888",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_APAC_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-AU", "840353923041"],
            ["GA09823-AU", "840353923102"],
        ]
        self.static_string = [
            "DEMO",
        ]
        self.starting_string = [
            "製造日期",
            "IMEI1",
            "IMEI2",
            "EID",
            "SKU",
        ]
        self.ignore_string = [
            "進口商：台灣大哥大股份有限公司",
            "地址：110鑫北市信義區煙廠路88號12楼",
            "服務電話：(02)6638-6888",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
