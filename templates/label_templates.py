"""
Template manager for label templates
"""
import logging
import re

class TemplateManager:
    """
    Manages label templates for barcode and text labels
    """

    def __init__(self):
        """Initialize template manager"""
        self.logger = logging.getLogger(__name__)

        # Initialize template lists
        self.barcode_templates = self._init_barcode_templates()
        self.text_templates = self._init_text_templates()

    def extract_sku_name(self, ocr_results):
        """
        Extract SKU name from OCR results

        Args:
            ocr_results: OCR results from barcode label

        Returns:
            SKU name or None if not found
        """
        for line in ocr_results:
            text = line[1][0].lower()  # OCR text

            # Look for SKU, AT&T SKU, or TMO SKU
            if "at&t sku" in text or "tmo sku" in text or "sku" in text:
                # Extract text after colon
                parts = text.split(":", 1)
                if len(parts) > 1:
                    sku = parts[1].strip().upper()
                    self.logger.info(f"Found SKU: {sku}")
                    return sku

        self.logger.warning("No SKU found in OCR results")
        return None

    def find_barcode_label_template(self, sku_name):
        """
        Find matching barcode label template for a SKU

        Args:
            sku_name: SKU name to match

        Returns:
            Template or None if not found
        """
        if not sku_name:
            return None

        # Look through all templates
        for template in self.barcode_templates:
            sku_list = template[0]  # SKU names in this template

            # Check if sku_name is in the template's sku_list
            if sku_name in sku_list:
                self.logger.info(f"Found barcode template for SKU: {sku_name}")
                return template

        self.logger.warning(f"No barcode template found for SKU: {sku_name}")
        return None

    def find_text_label_template(self, sku_name):
        """
        Find matching text label template for a SKU

        Args:
            sku_name: SKU name to match

        Returns:
            Template or None if not found
        """
        if not sku_name:
            return None

        # Look through all templates
        for template in self.text_templates:
            sku_list = template[0]  # SKU names in this template

            # Check if sku_name is in the template's sku_list
            if sku_name in sku_list:
                self.logger.info(f"Found text template for SKU: {sku_name}")
                return template

        self.logger.warning(f"No text template found for SKU: {sku_name}")
        return None

    def _init_barcode_templates(self):
        """
        Initialize barcode label templates

        Returns:
            List of barcode templates
        """
        from .barcode_templates import BARCODE_LABEL_TEMPLATE_LIST
        return BARCODE_LABEL_TEMPLATE_LIST

    def _init_text_templates(self):
        """
        Initialize text label templates

        Returns:
            List of text templates
        """
        from .text_templates import TEXT_LABEL_TEMPLATE_LIST
        return TEXT_LABEL_TEMPLATE_LIST