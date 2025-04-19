from analyzers.base_label_analyzer import BaseLabelAnalyzer
# from analyze_utils import get_base_score, extract_specific_field, has_any_keyword


class AK3_US_VZW_CL1_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA04385-US", "840244707699"],
            ["GA05578-US", "840244707729"],
            ["IQGA04385-US", "840244708177"],
            ["IQGA05578-US", "840244708207"],
            ["IQGA05696-US", "840244711368 "],
        ]
        self.static_string = [
            "Obsidian",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
            "SN",
            "Software Version",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        Verizon 特有的標籤分析方法

        Args:
            ocr_result: OCR 文本結果

        Returns:
            字典，包含匹配分數和提取的數據
        """
        if not ocr_result:
            return {"match_score": 0, "extracted_data": {}}

        ocr_text = ocr_result.lower()

        # 使用工具類獲取基本分數和提取的數據
        result = get_base_score(
            ocr_text,
            self.sku_name,
            self.static_string,
            self.starting_string,
            self.ignore_string
        )

        # 檢查 Verizon 特有的標記
        if has_any_keyword(ocr_text, ["vzw", "verizon"]):
            result["match_score"] += 5
            result["extracted_data"]["carrier"] = "Verizon"

        # 尋找 Verizon 特有的軟件版本格式
        software_version = extract_specific_field(
            ocr_text, "software version", ":", ["\n"])
        if software_version:
            result["extracted_data"]["Software Version"] = software_version

        return result


class AK3_US_VZW_CL2_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05562-US", "840244707705"],
            ["GA05579-US", "840244707736"],
            ["IQGA05562-US", "840244708184"],
            ["IQGA05579-US", "840244708214"],
        ]
        self.static_string = [
            "Porcelain",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
            "SN",
            "Software Version",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        Verizon Porcelain 標籤分析方法

        Args:
            ocr_result: OCR 文本結果

        Returns:
            字典，包含匹配分數和提取的數據
        """
        if not ocr_result:
            return {"match_score": 0, "extracted_data": {}}

        ocr_text = ocr_result.lower()

        # 使用工具類獲取基本分數和提取的數據
        result = get_base_score(
            ocr_text,
            self.sku_name,
            self.static_string,
            self.starting_string,
            self.ignore_string
        )

        # 檢查 Verizon 特有的標記
        if has_any_keyword(ocr_text, ["vzw", "verizon"]):
            result["match_score"] += 5
            result["extracted_data"]["carrier"] = "Verizon"

        # 檢查是否為 Porcelain 顏色
        if "porcelain" in ocr_text:
            result["match_score"] += 3
            result["extracted_data"]["color"] = "Porcelain"

        # 尋找 Verizon 特有的軟件版本格式
        software_version = extract_specific_field(
            ocr_text, "software version", ":", ["\n"])
        if software_version:
            result["extracted_data"]["Software Version"] = software_version

        return result


class AK3_US_VZW_CL3_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05563-US", "840244707712"],
            ["GA05580-US", "840244707743"],
            ["IQGA05563-US", "840244708191"],
            ["IQGA05580-US", "840244708221"],
            ["IQGA05697-US", "840244711375"],
        ]
        self.static_string = [
            "Bay",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
            "SN",
            "Software Version",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        Verizon Bay 標籤分析方法

        Args:
            ocr_result: OCR 文本結果

        Returns:
            字典，包含匹配分數和提取的數據
        """
        if not ocr_result:
            return {"match_score": 0, "extracted_data": {}}

        ocr_text = ocr_result.lower()

        # 使用工具類獲取基本分數和提取的數據
        result = get_base_score(
            ocr_text,
            self.sku_name,
            self.static_string,
            self.starting_string,
            self.ignore_string
        )

        # 檢查 Verizon 特有的標記
        if has_any_keyword(ocr_text, ["vzw", "verizon"]):
            result["match_score"] += 5
            result["extracted_data"]["carrier"] = "Verizon"

        # 檢查是否為 Bay 顏色
        if "bay" in ocr_text:
            result["match_score"] += 3
            result["extracted_data"]["color"] = "Bay"

        # 尋找 Verizon 特有的軟件版本格式
        software_version = extract_specific_field(
            ocr_text, "software version", ":", ["\n"])
        if software_version:
            result["extracted_data"]["Software Version"] = software_version

        return result


class AK3_US_VZW_CL4_Retail_Label(BaseLabelAnalyzer):
    def __init__(self):
        super().__init__()
        self.project = "AK3"
        self.sku_name = [
            ["GA05589-US", "840244708238"],
            ["GA05590-US", "840244708245"],
            ["IQGA05589-US", "840244708399"],
            ["IQGA05590-US", "840244708405"],
        ]
        self.static_string = [
            "Aloe",
        ]
        self.starting_string = [
            "SKU",
            "EID",
            "IMEI1",
            "IMEI2",
            "SN",
            "Software Version",
        ]
        self.ignore_string = []

    def analyze(self, ocr_result):
        """
        Verizon Aloe 標籤分析方法

        Args:
            ocr_result: OCR 文本結果

        Returns:
            字典，包含匹配分數和提取的數據
        """
        if not ocr_result:
            return {"match_score": 0, "extracted_data": {}}

        ocr_text = ocr_result.lower()

        # 使用工具類獲取基本分數和提取的數據
        result = get_base_score(
            ocr_text,
            self.sku_name,
            self.static_string,
            self.starting_string,
            self.ignore_string
        )

        # 檢查 Verizon 特有的標記
        if has_any_keyword(ocr_text, ["vzw", "verizon"]):
            result["match_score"] += 5
            result["extracted_data"]["carrier"] = "Verizon"

        # 檢查是否為 Aloe 顏色
        if "aloe" in ocr_text:
            result["match_score"] += 3
            result["extracted_data"]["color"] = "Aloe"

        # 尋找 Verizon 特有的軟件版本格式
        software_version = extract_specific_field(
            ocr_text, "software version", ":", ["\n"])
        if software_version:
            result["extracted_data"]["Software Version"] = software_version

        return result
