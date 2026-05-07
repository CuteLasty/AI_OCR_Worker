"""
Text processing utilities for OCR
"""
import re
import logging
import difflib
import Levenshtein


class TextMatcher:
    """Text matching and comparison utilities"""

    def __init__(self):
        """Initialize text matcher"""
        self.logger = logging.getLogger(__name__)

    def find_closest_text(self, ocr_text, template_texts):
        """
        Find the closest matching text in templates using Levenshtein distance

        Args:
            ocr_text: OCR recognized text
            template_texts: List of template texts to compare against

        Returns:
            Tuple of (minimum_distance, closest_text_index)
        """
        if not template_texts:
            return 999, -1

        # Normalize OCR text
        normalized_ocr = self.normalize_text(ocr_text)

        min_distance = float('inf')
        min_index = -1

        # Find closest matching template text
        for index, template in enumerate(template_texts):
            # Normalize template text
            normalized_template = self.normalize_text(template)

            # Calculate Levenshtein distance
            distance = Levenshtein.distance(
                normalized_ocr, normalized_template)

            # Update minimum if this is better
            if distance < min_distance:
                min_distance = distance
                min_index = index

            # Early termination if exact match found
            if min_distance == 0:
                break

        return min_distance, min_index

    def get_difference_opcodes(self, template_text, ocr_text):
        """
        Get detailed difference information between template and OCR text

        Args:
            template_text: Template text
            ocr_text: OCR recognized text

        Returns:
            List of opcodes (tag, i1, i2, j1, j2)
        """
        # Use SequenceMatcher to calculate differences
        matcher = difflib.SequenceMatcher(None, template_text, ocr_text)
        opcodes = matcher.get_opcodes()

        # Convert opcodes to serializable format (tuples to lists)
        serializable_opcodes = []
        for tag, i1, i2, j1, j2 in opcodes:
            serializable_opcodes.append({
                "tag": tag,      # 'equal', 'replace', 'delete', or 'insert'
                "i1": i1,        # Start index in template text
                "i2": i2,        # End index in template text
                "j1": j1,        # Start index in OCR text
                "j2": j2,        # End index in OCR text
                # "template_substr": template_text[i1:i2],
                # "ocr_substr": ocr_text[j1:j2]
            })

        return serializable_opcodes

    def normalize_text(self, text):
        """
        Normalize text for comparison (remove extra spaces, standardize punctuation)

        Args:
            text: Text to normalize

        Returns:
            Normalized text
        """
        if not text:
            return ""

        # Convert to string if not already
        text = str(text)

        # Remove extra spaces around punctuation
        normalized = re.sub(r'\s*([.,!?;:()/&])\s*', r'\1', text)

        # Normalize multiple spaces to single space
        normalized = re.sub(r'\s+', ' ', normalized)

        # Strip leading and trailing whitespace
        normalized = normalized.strip()

        return normalized

    def is_special_text(self, text, special_texts):
        """
        Check if text matches any of the special text patterns (e.g., SKU, IMEI)

        Args:
            text: Text to check
            special_texts: List of special text patterns

        Returns:
            True if text is a special text
        """
        if not text or not special_texts:
            return False

        # Check if text starts with any special text pattern
        text_lower = text.lower()
        for special in special_texts:
            if text_lower.startswith(special.lower()):
                return True

        return False

    def is_string_equal_fuzz(self, template_str, ocr_str):
        """
        Compare strings with fuzzy matching for common OCR errors

        Args:
            template_str: Template string
            ocr_str: OCR recognized string

        Returns:
            True if strings match with fuzzy rules
        """
        if template_str == ocr_str:
            return True

        # Define character equivalence groups
        same_chars_group1 = {'1', 'I', 'l', '|'}
        same_chars_group2 = {'O', '0'}
        same_chars_group3 = {'S', '5'}

        # Compare character by character
        for c1, c2 in zip(template_str, ocr_str):
            # Exact match
            if c1 == c2:
                continue

            # Group 1: 1, I, l, |
            if c1 in same_chars_group1 and c2 in same_chars_group1:
                continue

            # Group 2: O, 0
            if c1 in same_chars_group2 and c2 in same_chars_group2:
                continue

            # Group 3: S, 5
            if c1 in same_chars_group3 and c2 in same_chars_group3:
                continue

            # No match found for this character
            return False

        # All characters matched
        return True

    def is_string_list_equal_fuzz(self, text: str, special_texts: list) -> bool:
        result = False
        for special in special_texts:
            result = self.is_string_equal_fuzz(special, text)
            if result:
                break
        return result

    def is_string_list_equal(self, text: str, ignore_texts: list) -> bool:
        result = False
        for ignore_text in ignore_texts:
            result = text == ignore_text
            if result:
                break
        return result
