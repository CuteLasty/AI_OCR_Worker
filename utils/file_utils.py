import os
import shutil
from datetime import datetime
from loguru import logger


def ensure_dir(directory):
    """
    確保目錄存在，如有必要創建它

    Args:
        directory (str): 目錄路徑
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"創建目錄: {directory}")
        except Exception as e:
            logger.error(f"創建目錄 {directory} 失敗: {e}")
            raise


def get_timestamp_dir(base_dir, timestamp):
    """
    根據時間戳獲取目錄

    Args:
        base_dir (str): 基礎目錄
        timestamp (str): 格式為'YYYYMMDD_HHMMSS'的時間戳

    Returns:
        str: 目錄路徑
    """
    try:
        # 解析時間戳
        date_part = timestamp[:8]
        time_part = timestamp[9:]

        # 創建目錄
        date_dir = os.path.join(base_dir, date_part)
        time_dir = os.path.join(date_dir, time_part)

        # 確保目錄存在
        ensure_dir(date_dir)
        ensure_dir(time_dir)

        return time_dir

    except Exception as e:
        logger.error(f"創建時間戳目錄時出錯: {e}")
        raise


def backup_file(file_path, backup_base, timestamp):
    """
    備份文件到時間戳目錄

    Args:
        file_path (str): 文件路徑
        backup_base (str): 基礎備份目錄
        timestamp (str): 格式為'YYYYMMDD_HHMMSS'的時間戳

    Returns:
        str: 備份文件的路徑
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件未找到: {file_path}")

        # 獲取時間戳目錄
        backup_dir = get_timestamp_dir(backup_base, timestamp)

        # 獲取文件名
        filename = os.path.basename(file_path)

        # 創建備份路徑
        backup_path = os.path.join(backup_dir, filename)

        # 複製文件
        shutil.copy2(file_path, backup_path)
        logger.info(f"備份 {file_path} 至 {backup_path}")

        return backup_path

    except Exception as e:
        logger.error(f"備份文件時出錯: {e}")
        raise
