from abc import ABC, abstractmethod

class BaseLabelAnalyzer(ABC):
    """
    Abstract base class for label analyzers.
    """
    def __init__(self):
        self.project = ""
        self.sku_name = []
        self.static_string = []
        self.starting_string = []
        self.ignore_string = []
    
    @abstractmethod
    def analyze(self, ocr_result):
        """
        Analyze OCR results to extract relevant information.
        
        Args:
            ocr_result: The OCR result to analyze
            
        Returns:
            Analysis result
        """
        pass
