from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_EMEA_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA05769-GB", "0840353922273"],
            ["GA09563-GB", "0840353922327"],
            ["GA09565-GB", "0840353922433"],
            ["GA09564-GB", "0840353922372"],
            ["GA09566-GB", "0840353922488"],
            ["GA09585-GB", "0840353922532"],
            ["GA05769-GB-N", "0840353922815"],
            ["GA09563-GB-N", "0840353922860"],
            ["GA09564-GB-N", "0840353922914"],
            ["GA09565-GB-N", "0840353922969"]
        ]
        self.static_string = []
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
        ]
        self.ignore_string = [
            "AT,BE,BG,CY,CZ,DE,DK,EE,EL,ES,FI,FR,HR,HU,IE,IT,LT,",
            "LU,LV,MT,NL,PL,PT,RO,SE,SI,SK,UK(NI),CH,IS,LI,NO,TR.",
            "g.co/envinfo",
            "PAP",
            "UK",
            "CA",
            "CE",
            "FR",
            "ELEMENTS",
            "D'EMBALLAGE",
            "+ NOTIOE",
            "BAD",
            "DE",
            "TRI",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass


class TG4_DEMO_EMEA_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "TG4"
        self.sku_name = [
            ["GA09822-GB", "0840353923034"],
            ["GA09823-GB", "0840353923096"],
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
        self.ignore_string = [
            "AT,BE,BG,CY,CZ,DE,DK,EE,EL,ES,FI,"
            "FR,HR,HU,IE,IT,LT,LU,LV,MT,NL,PL,PT,"
            "RO,SE,SI,SK,UK(NI),CH,IS,LI,NO,TR.",
            "g.co/envinfo",
            "PAP",
            "UK",
            "CA",
            "CE",
            "FR",
            "ELEMENTS",
            "D'EMBALLAGE",
            "+ NOTIOE",
            "BAD",
            "DE",
            "TRI",
        ]

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
