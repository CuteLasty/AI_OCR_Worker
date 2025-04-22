"""
Visualization utilities for OCR results
"""
import logging
import cv2
import numpy as np
from .draw_utils import PILTextDrawer


class Visualizer:
    """Visualization utilities for OCR results"""

    def __init__(self, fontScale=32):
        """Initialize visualizer"""
        self.logger = logging.getLogger(__name__)

        # Define colors for different operations
        self.colors = {
            'bbox': (0, 255, 0),        # Green for bounding boxes
            'text': (255, 0, 0),        # Blue for text
            'index': (0, 0, 255),       # Red for index numbers
            'equal': (0, 255, 0),       # Green for matching text
            'replace': (0, 165, 255),   # Orange for replaced text
            'delete': (0, 0, 255),      # Red for deleted text
            'insert': (255, 0, 0),      # Blue for inserted text
            'error': (0, 0, 255)        # Red for error highlights
        }

        self.fontScale = fontScale

        self.text_drawer = PILTextDrawer(preload_fonts=[
            ("simsun.ttc", int(round(fontScale)))
        ])

    def draw_ocr_results(self, image_path, ocr_results, output_path):
        """
        Draw OCR results on image (bounding boxes and text)

        Args:
            image: Image to draw on
            ocr_results: OCR results from PaddleOCR

        Returns:
            Image with visualizations
        """
        try:
            # 讀取圖像
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"讀取圖像失敗: {image_path}")

            # 創建副本
            result = img.copy()

            for i, item in enumerate(ocr_results):
                # Get bounding box and text
                positions = item['positions']
                text = item['text']

                # 將位置轉換為numpy點數組
                bbox = np.array([[int(p[0]), int(p[1])]
                                 for p in positions], dtype=np.int32)

                # Draw bounding box
                cv2.polylines(result, [bbox], True, self.colors['bbox'], 2)

                # Draw text near top-left corner
                text_pos = (int(bbox[0][0]), int(bbox[0][1]) - 10)
                # cv2.putText(image, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale, self.colors['text'], 1)
                self.text_drawer.putText(
                    result, text, text_pos, "simsun.ttc", self.fontScale, self.colors['text'], 1)

                # Draw index number
                index_pos = (int(bbox[0][0] - 25), int(bbox[0][1]) - 10)
                # cv2.putText(result, f"{i+1}", index_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale+2, self.colors['index'], 2)
                self.text_drawer.putText(
                    result, f"{i+1}", index_pos, "simsun.ttc", self.fontScale, self.colors['index'], 2)

            # 保存結果
            cv2.imwrite(output_path, result)
            self.logger.info(f"OCR可視化保存至 {output_path}")

            return output_path

        except Exception as e:
            self.logger.error(f"繪製OCR結果時出錯: {e}")
            raise

    def draw_analysis_results(self, image_path, analysis_results, output_path):
        """
        Draw analysis results on image (highlighting differences)

        Args:
            image: Image to draw on
            analysis_results: Analysis results with differences

        Returns:
            Image with visualizations
        """
        try:
            # 讀取圖像
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"讀取圖像失敗: {image_path}")

            # 創建副本
            result = img.copy()

            for item in analysis_results.get('results', []):
                # Get bounding box
                bbox = np.array(item['bbox'], dtype=np.int32)

                # Get text and metrics
                text = item['text']
                is_special = item.get('is_special', False)
                distance = item.get('distance', 0)

                # Draw bounding box with color based on match quality
                if is_special or distance == 0:
                    # Perfect match or special text (green)
                    box_color = self.colors['equal']
                elif distance < 3:
                    # Minor differences (orange)
                    box_color = self.colors['replace']
                else:
                    # Major differences (red)
                    box_color = self.colors['error']

                cv2.polylines(result, [bbox], True, box_color, 2)

                # Draw text near top-left corner
                text_pos = (int(bbox[0][0]), int(bbox[0][1]) - 10)
                # cv2.putText(image, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale, self.colors['text'], 1)
                self.text_drawer.putText(
                    result, text, text_pos, "simsun.ttc", self.fontScale, self.colors['text'], 1)

                # For non-special text with differences, draw detailed diff information
                if not is_special and distance > 0 and 'opcodes' in item:
                    self._draw_text_differences(result, item)

            # 保存結果
            cv2.imwrite(output_path, result)
            self.logger.info(f"分析可視化保存至 {output_path}")

            return output_path

        except Exception as e:
            self.logger.error(f"Error drawing analysis results: {str(e)}")
            raise

    def draw_analysis_results_barcode(self, image_path, analysis_results, output_path):
        """
        Draw analysis results on image (highlighting differences)

        Args:
            image: Image to draw on
            analysis_results: Analysis results with differences

        Returns:
            Image with visualizations
        """
        try:
            # 讀取圖像
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"讀取圖像失敗: {image_path}")

            # 創建副本
            result = img.copy()

            for item in analysis_results.get('results', []):
                # Get bounding box
                bbox = np.array(item['bbox'], dtype=np.int32)

                # Get text and metrics
                text = item.get('text', '')
                is_pass = item.get('pass', False)

                # Draw bounding box with color based on match quality
                if is_pass:
                    # Perfect match or special text (green)
                    box_color = self.colors['equal']
                else:
                    # Major differences (red)
                    box_color = self.colors['error']

                cv2.polylines(result, [bbox], True, box_color, 2)

                # Draw text near top-left corner
                text_pos = (int(bbox[0][0]), int(bbox[0][1]) - 10)
                # cv2.putText(image, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale, self.colors['text'], 1)
                self.text_drawer.putText(
                    result, text, text_pos, "simsun.ttc", self.fontScale, self.colors['text'], 1)

                # For non-special text with differences, draw detailed diff information
                if not is_pass:
                    self._draw_text_differences(result, item)

            # 保存結果
            cv2.imwrite(output_path, result)
            self.logger.info(f"分析可視化保存至 {output_path}")

            return output_path

        except Exception as e:
            self.logger.error(f"Error drawing analysis results: {str(e)}")
            raise

    def draw_analysis_results_text(self, image_path, analysis_results, output_path):
        """
        Draw analysis results on image (highlighting differences)

        Args:
            image: Image to draw on
            analysis_results: Analysis results with differences

        Returns:
            Image with visualizations
        """
        try:
            # 讀取圖像
            img = cv2.imread(image_path)
            if img is None:
                raise ValueError(f"讀取圖像失敗: {image_path}")

            # 創建副本
            result = img.copy()

            for item in analysis_results.get('results', []):
                # Get bounding box
                bbox = np.array(item['bbox'], dtype=np.int32)

                # Get text and metrics
                text = item['text']
                is_special = item.get('is_special', False)
                distance = item.get('distance', 0)

                # Draw bounding box with color based on match quality
                if is_special or distance == 0:
                    # Perfect match or special text (green)
                    box_color = self.colors['equal']
                elif distance < 3:
                    # Minor differences (orange)
                    box_color = self.colors['replace']
                else:
                    # Major differences (red)
                    box_color = self.colors['error']

                cv2.polylines(result, [bbox], True, box_color, 2)

                # Draw text near top-left corner
                text_pos = (int(bbox[0][0]), int(bbox[0][1]) - 10)
                # cv2.putText(image, text, text_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale, self.colors['text'], 1)
                self.text_drawer.putText(
                    result, text, text_pos, "simsun.ttc", self.fontScale, self.colors['text'], 1)

                # For non-special text with differences, draw detailed diff information
                if not is_special and distance > 0 and 'opcodes' in item:
                    self._draw_text_differences(result, item)

            # 保存結果
            cv2.imwrite(output_path, result)
            self.logger.info(f"分析可視化保存至 {output_path}")

            return output_path

        except Exception as e:
            self.logger.error(f"Error drawing analysis results: {str(e)}")
            raise

    def _draw_text_differences(self, image, analysis_item):
        """
        Draw detailed text differences on image

        Args:
            image: Image to draw on
            analysis_item: Analysis result item with opcodes
        """
        try:
            bbox = np.array(analysis_item['bbox'], dtype=np.int32)
            text = analysis_item['text']
            template_text = analysis_item.get('template_text', '')
            opcodes = analysis_item.get('opcodes', [])

            if not text or not opcodes:
                return

            # Calculate approximate character width
            text_width = bbox[1][0] - bbox[0][0]
            char_width = text_width / max(len(text), 1)

            # Calculate character height
            char_height = bbox[3][1] - bbox[0][1]

            # Draw each difference according to opcode
            for opcode in opcodes:
                tag = opcode.get('tag')

                # Skip equal tags (matching text)
                if tag == 'equal':
                    continue

                # Get character indices
                j1 = opcode.get('j1', 0)  # Start index in OCR text
                j2 = opcode.get('j2', 0)  # End index in OCR text

                # Skip if indices are invalid
                if j1 >= len(text) or j1 == j2:
                    continue

                # Calculate rectangle coordinates for the difference
                x_start = int(bbox[0][0] + j1 * char_width)
                x_end = int(bbox[0][0] + j2 * char_width)
                y_start = int(bbox[0][1])
                y_end = int(bbox[0][1] + char_height)

                # Get color based on operation type
                if tag == 'replace':
                    color = self.colors['replace']
                elif tag == 'delete':
                    color = self.colors['delete']
                elif tag == 'insert':
                    color = self.colors['insert']
                else:
                    color = self.colors['error']

                # Draw rectangle around the difference
                cv2.rectangle(image, (x_start, y_start),
                              (x_end, y_end), color, 2)

                # Draw small label with expected text for 'replace' and 'delete'
                if tag in ['replace', 'delete'] and 'template_substr' in opcode:
                    expected_text = opcode['template_substr']
                    if expected_text:
                        label_pos = (x_start, y_start - 5)
                        # cv2.putText(image, expected_text, label_pos, cv2.FONT_HERSHEY_SIMPLEX, self.fontScale-0.1, color, 1)
                        self.text_drawer.putText(
                            image, expected_text, label_pos, "simsun.ttc", self.fontScale-0.1, color, 1)

        except Exception as e:
            self.logger.error(f"Error drawing text differences: {str(e)}")
