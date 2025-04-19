from analyzers.base_label_analyzer import BaseLabelAnalyzer


class TG4_IN_MRP_TEXT_Label(BaseLabelAnalyzer):
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
            ["GA09824-IN", "840353923775"],
            ["GA09825-IN", "840353923782"]
        ]
        self.static_string = [
            "Commodity: Cellular Phone",
            "Quantity:      1N      (Pixel 9a, Charging Cable, SIM Tool,",
            "Safety/Regulatory Booklet)",
            "Manufactured by: Google LLC 1600 Amphitheatre",
            "Parkway, Mountain View, CA 94043, USA",
            "Country of Origin: Phone made in Vietnam.",
            "Accessories made in China.",
            "Imported by: Google Information Services India Private",
            "Limited. Registered Address: Unit No. 204, 2nd Floor,",
            "Signature Tower-II, Tower A, Sector-15, Part-II, Village",
            "Silokhera, Gurgaon, Haryana, 122001, India.",
            "#####",
            "Packed by: Compal (Vietnam) Co., Ltd / Công Ty Tnhh",
            "Compal (Việt Nam) Ba Thien Industrial Zone, Ba Hien Town,",
            "Binh Xuyen District, Vinh Phuc Province, Vietnam-15800",
            "Customer Care: For all product-related complaints/",
            "assistance: visit g.co/pixel/support, or call our",
            "Google Support toll free number: 1-800-419-0655",
            "(Mon to Sun 9:00am to 9:00pm) or email us at",
            "googleapac-devicesupport@google.com. Repair partner:",
            "F1 Info Solutions & Services Pvt. Ltd., D-245, D Block,",
            "Sector 63, Noida, Uttar Pradesh, 201301, India.",
            "M.R.P.: ₹ 49,999 (inclusive of all taxes)",
            "Month & Year of Manufacture: January, 2024",
        ]
        self.starting_string = []
        self.ignore_string = []

    def analyze(self, ocr_result):
        # Implementation for specific analysis
        pass
