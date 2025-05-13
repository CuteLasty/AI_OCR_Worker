from datetime import datetime

from analyzers.utils import create_analyze_result


def generate_YMDD(date=None):
    """
    將日期轉換為YMDD格式的標籤
    Y: 年份的最後一位數字 (2023=3, 2024=4)
    M: 月份 (Jan=1, Feb=2...Oct=A, Nov=B, Dec=C)
    DD: 月份中的日期（兩位數）

    Args:
        date (datetime): 要轉換的日期對象

    Returns:
        str: YMDD格式的字串
    """

    if date is None:
        date = datetime.now()

    # 獲取年份的最後一位數字
    last_digit_of_year = date.year % 10

    # 使用陣列進行月份轉換
    month_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']
    month_char = month_chars[date.month - 1]  # 月份索引從0開始

    # 獲取日期並轉換為兩位數格式
    day_str = f"{date.day:02d}"

    # 組合成YMDD格式
    return f"{last_digit_of_year}{month_char}{day_str}"


def generate_month_year(date=None):
    """
    根據日期返回月份全名和年份

    Args:
        date (datetime, optional): 輸入的日期，如果不提供，則使用當前日期

    Returns:
        str: 格式為 'Month, Year' 的字串，例如 'February, 2024'
    """
    # 月份全名列表
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # 處理輸入參數
    if date is None:
        date = datetime.now()

    month = date.month
    year = date.year

    # 返回月份全名和年份
    return f"{month_names[month-1]}, {year}"


def generate_MMDDYYYY(date=None):
    """
    Args:
        date (datetime, optional): 輸入的日期，如果不提供，則使用當前日期
    """
    # 處理輸入參數
    if date is None:
        date = datetime.now()

    # Format as MM/DD/YYYY
    date_string = date.strftime("%m/%d/%Y")

    return date_string


def generate_CHT_YYMM(date=None):
    """
    生成当前日期的"製造日期：YY年MM月"格式字串

    Args:
        date (datetime, optional): 輸入的日期，如果不提供，則使用當前日期

    返回:
        str: 格式化的当前日期字串
    """
    # 處理輸入參數
    if date is None:
        date = datetime.now()
    yy = str(date.year)[-2:]
    mm = f"{date.month:02d}"

    return f"製造日期：{yy}年{mm}月"
