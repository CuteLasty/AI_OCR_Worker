"""
條碼分析相關的獨立功能函數
"""
from loguru import logger

from analyzers.utils import create_analyze_result


def initialize_analysis(customer="aa8", type='barcode'):
    """初始化分析結果字典"""
    return {
        'customer': customer,
        'type': type,
        'results': [],
        'errors': []
    }


def process_date_str(ocr_results: dict, date_str: str, date_str_x: int, date_str_y: int, bbox_index: int, analysis: dict) -> list:
    """處理YMDD日期標籤

    Args:
        ocr_results: OCR 識別結果列表
        date_str: 日期字串
        date_str_x: 日期字串X座標
        date_str_y: 日期字串Y座標
        bbox_index: 邊界角落. 0: 左上, 1: 右上, 2: 右下, 3: 左下
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_ymdd = []
    ocr_results_copy = []

    # 根據位置分離結果
    for ocr_result in ocr_results:
        bbox = ocr_result['positions'][bbox_index]  # OCR bounding box
        if bbox[0] > date_str_x and bbox[1] > date_str_y:
            ocr_results_ymdd.append(ocr_result)
        else:
            ocr_results_copy.append(ocr_result)

    # 處理YMDD結果
    if len(ocr_results_ymdd) == 1:
        text = ocr_results_ymdd[0]['text']
        bbox = ocr_results_ymdd[0]['positions']
        confidence = ocr_results_ymdd[0]['confidence']

        analyze_result = create_analyze_result(
            bbox, text, confidence, (text == date_str))
        analysis['results'].append(analyze_result)
    else:
        ocr_results_copy.extend(ocr_results_ymdd)

    return ocr_results_copy


def process_date_str2(ocr_results: dict, date_str: str, date_str_x: int, date_str_y: int, bbox_index: int, analysis: dict) -> list:
    """處理YMDD日期標籤

    Args:
        ocr_results: OCR 識別結果列表
        date_str: 日期字串
        date_str_x: 日期字串X座標
        date_str_y: 日期字串Y座標
        bbox_index: 邊界角落. 0: 左上, 1: 右上, 2: 右下, 3: 左下
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_ymdd = []
    ocr_results_copy = []

    # 根據位置分離結果
    for ocr_result in ocr_results:
        bbox = ocr_result['positions'][bbox_index]  # OCR bounding box
        if bbox[0] > date_str_x and bbox[1] < date_str_y:
            ocr_results_ymdd.append(ocr_result)
        else:
            ocr_results_copy.append(ocr_result)

    # 處理YMDD結果
    if len(ocr_results_ymdd) == 1:
        text = ocr_results_ymdd[0]['text']
        bbox = ocr_results_ymdd[0]['positions']
        confidence = ocr_results_ymdd[0]['confidence']

        analyze_result = create_analyze_result(
            bbox, text, confidence, (text == date_str))
        analysis['results'].append(analyze_result)
    else:
        ocr_results_copy.extend(ocr_results_ymdd)

    return ocr_results_copy


def find_text_and_process_date_str(ocr_results: dict, text: str, date_str: str, analysis: dict) -> list:
    """處理YMDD日期標籤

    Args:
        ocr_results: OCR 識別結果列表
        text: 搜尋文字
        date_str: 日期字串
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_yymm = []
    ocr_results_copy = []

    # 根據特定文字分離結果
    for ocr_result in ocr_results:
        if ocr_result['text'].startswith(text):
            ocr_results_yymm.append(ocr_result)
        else:
            ocr_results_copy.append(ocr_result)

    # 處理YMDD結果
    if len(ocr_results_yymm) == 1:
        text = ocr_results_yymm[0]['text']
        bbox = ocr_results_yymm[0]['positions']
        confidence = ocr_results_yymm[0]['confidence']

        analyze_result = create_analyze_result(
            bbox, text, confidence, (text == date_str))
        analysis['results'].append(analyze_result)
    else:
        ocr_results_copy.extend(ocr_results_yymm)

    return ocr_results_copy


def process_static_strings(ocr_results, static_strings, analysis):
    """處理固定字串

    Args:
        ocr_results: OCR 識別結果列表
        static_strings: 要檢查的靜態字串列表
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_copy = []

    for ocr_result in ocr_results:
        bbox = ocr_result['positions']
        text = ocr_result['text']
        confidence = ocr_result['confidence']

        found = False
        for static_text in static_strings[:]:  # 使用切片創建副本進行遍歷
            if text == static_text:
                analyze_result = create_analyze_result(
                    bbox, text, confidence, True)
                analysis['results'].append(analyze_result)
                found = True
                static_strings.remove(static_text)
                break

        if not found:
            ocr_results_copy.append(ocr_result)

    return ocr_results_copy


def process_one_static_strings(ocr_results, static_string, analysis):
    """處理固定字串

    Args:
        ocr_results: OCR 識別結果列表
        static_string: 要檢查的靜態字串
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_copy = []

    for ocr_result in ocr_results:
        bbox = ocr_result['positions']
        text = ocr_result['text']
        confidence = ocr_result['confidence']

        found = False
        if text == static_string:  # 使用切片創建副本進行遍歷
            analyze_result = create_analyze_result(
                bbox, text, confidence, True)
            analysis['results'].append(analyze_result)
            found = True

        if not found:
            ocr_results_copy.append(ocr_result)

    return ocr_results_copy


def process_starting_strings_and_digits(ocr_results, starting_string, text_matcher, analysis):
    """處理開頭字串和數字

    Args:
        ocr_results: OCR 識別結果列表
        starting_string: 要檢查的起始字串列表
        text_matcher: TextMatcher 實例
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_copy = []

    for ocr_result in ocr_results:
        bbox = ocr_result['positions']
        text = ocr_result['text']
        confidence = ocr_result['confidence']

        found = False
        for starting_text in starting_string[:]:  # 使用切片創建副本進行遍歷
            if text_matcher.is_special_text(text, starting_text):
                analyze_result = create_analyze_result(
                    bbox, text, confidence, True)
                analysis['results'].append(analyze_result)
                found = True
                starting_string.remove(starting_text)
                break

        if found:
            continue

        if text.isdigit():
            analyze_result = create_analyze_result(
                bbox, text, confidence, True)
            analysis['results'].append(analyze_result)
            continue

        ocr_results_copy.append(ocr_result)

    return ocr_results_copy


def process_ignore_str_type1(ocr_results: dict, ignore_x: int, ignore_y: int, bbox_index: int) -> list:
    """處理忽略區域的字串

    Args:
        ocr_results: OCR 識別結果列表
        ignore_x: 忽略區域X座標
        ignore_y: 忽略區域Y座標
        bbox_index: 邊界角落. 0: 左上, 1: 右上, 2: 右下, 3: 左下
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_copy = []

    # 忽略所有印刷區域文字
    for ocr_result in ocr_results:
        bbox = ocr_result['positions'][bbox_index]  # OCR bounding box
        if not (bbox[0] > ignore_x and bbox[1] > ignore_y):
            ocr_results_copy.append(ocr_result)

    return ocr_results_copy


def process_ignore_str_type2(ocr_results: dict, ignore_x: int, ignore_y: int, bbox_index: int) -> list:
    """處理忽略區域的字串

    Args:
        ocr_results: OCR 識別結果列表
        ignore_x: 忽略區域X座標
        ignore_y: 忽略區域Y座標
        bbox_index: 邊界角落. 0: 左上, 1: 右上, 2: 右下, 3: 左下
        analysis: 分析結果字典

    Returns:
        list: 未處理的 OCR 結果
    """
    ocr_results_copy = []

    # 忽略所有印刷區域文字
    for ocr_result in ocr_results:
        bbox = ocr_result['positions'][bbox_index]  # OCR bounding box
        if not (bbox[0] > ignore_x and bbox[1] < ignore_y):
            ocr_results_copy.append(ocr_result)

    return ocr_results_copy


def sort_multicolumn(ocr_results, width):
    """
    Process multi-column text, arranging OCR results in reading order
    Args:
        ocr_results: OCR results from PaddleOCR
        width: Image width
        height: Image height
    Returns:
        Sorted OCR results
    """
    if not ocr_results:
        return []
    # Split image into left and right columns
    half_width = (width / 2) - 100  # Offset to handle overlap
    # Group results by column
    left_column = []
    right_column = []
    for result in ocr_results:
        # Check if the first point (top-left) is in left or right half
        min_x = min(int(p[0]) for p in result['positions'])
        if min_x < half_width:
            left_column.append(result)
        else:
            right_column.append(result)
    # Sort each column by vertical position (y-coordinate)
    # Sort by y-coordinate of top-left point
    left_column.sort(key=lambda x: min(int(p[1]) for p in x['positions']))
    right_column.sort(key=lambda x: min(int(p[1]) for p in x['positions']))
    # Combine left and right columns (read left column first, then right)
    return left_column, right_column


def process_column(column_results, template_texts, text_matcher, analysis):
    """
    Process a column of OCR results against a set of template texts
    Args:
        column_results: List of OCR results for a column
        template_texts: List of template texts to match against
        text_matcher: TextMatcher instance
        analysis: Analysis dictionary to update with results
    """
    for ocr_result in column_results:
        bbox = ocr_result['positions']  # OCR bounding box
        text = ocr_result['text'].strip()  # OCR text
        confidence = ocr_result['confidence']  # OCR confidence
        # Find closest matching template text
        distance, closest_idx = text_matcher.find_closest_text(
            text, template_texts)
        # Get matching template text
        template_text = template_texts[closest_idx]
        # Get detailed differences
        opcodes = text_matcher.get_difference_opcodes(
            template_text, text)
        analysis['results'].append({
            "bbox": bbox,
            "text": text,
            "confidence": confidence,
            "distance": distance,
            "template_text": template_text,
            "opcodes": opcodes
        })


def get_y_pos_by_text(ocr_results, text):
    """在OCR結果中查找特定文字"""
    for ocr_result in ocr_results:
        if ocr_result['text'].startswith(text):
            bbox = ocr_result['positions']
            y_pos = bbox[0][1] + ((bbox[3][1] - bbox[0][1])/2)
            return int(y_pos)
    return None
