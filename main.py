#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import signal
import argparse
from datetime import datetime
from loguru import logger

# 導入本地模塊
from models import LabelProcessor
from utils import RedisConsumer
import config

# 配置日誌
def setup_logger():
    """配置應用程式日誌"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, "label_processor.log")
    
    # 移除默認處理器
    logger.remove()
    
    # 添加控制台處理器
    logger.add(sys.stderr, level="INFO")
    
    # 添加文件處理器，每天輪換，保留30天
    logger.add(
        log_file,
        rotation="00:00",  # 每天午夜
        retention="30 days",
        level="DEBUG",
        encoding="utf-8"
    )
    
    logger.info("日誌系統初始化")

# 處理信號
def signal_handler(sig, frame):
    """處理退出信號"""
    logger.info("接收到終止信號，正在優雅退出...")
    sys.exit(0)

# 主函數
def main():
    """主處理循環"""
    # 解析命令行參數
    parser = argparse.ArgumentParser(description="標籤處理系統")
    parser.add_argument("--redis-host", default=config.REDIS_HOST, help="Redis主機")
    parser.add_argument("--redis-port", type=int, default=config.REDIS_PORT, help="Redis端口")
    parser.add_argument("--redis-db", type=int, default=config.REDIS_DB, help="Redis數據庫")
    parser.add_argument("--redis-queue", default=config.REDIS_QUEUE, help="Redis隊列鍵")
    parser.add_argument("--yolo-model", default=config.YOLO_MODEL_PATH, help="YOLO模型路徑")
    parser.add_argument("--backup-dir", default=config.BACKUP_BASE, help="備份目錄")
    parser.add_argument("--result-dir", default=config.RESULT_BASE, help="結果目錄")
    parser.add_argument("--template-dir", default=config.TEMPLATE_DIR, help="模板目錄")
    parser.add_argument("--use-gpu", action="store_true", default=config.USE_GPU, help="是否使用GPU")
    
    args = parser.parse_args()
    
    # 設置日誌
    setup_logger()
    
    # 註冊信號處理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    logger.info("標籤處理系統啟動")
    logger.info(f"Redis連接: {args.redis_host}:{args.redis_port}/{args.redis_db}")
    logger.info(f"Redis隊列: {args.redis_queue}")
    logger.info(f"YOLO模型: {args.yolo_model}")
    logger.info(f"備份目錄: {args.backup_dir}")
    logger.info(f"結果目錄: {args.result_dir}")
    logger.info(f"模板目錄: {args.template_dir}")
    logger.info(f"使用GPU: {args.use_gpu}")
    
    try:
        # 初始化標籤處理器
        processor = LabelProcessor(
            yolo_model_path=args.yolo_model,
            backup_base=args.backup_dir,
            result_base=args.result_dir,
            template_dir=args.template_dir,
            use_gpu=args.use_gpu
        )
        
        # 初始化Redis消費者
        consumer = RedisConsumer(
            host=args.redis_host,
            port=args.redis_port,
            db=args.redis_db,
            queue_key=args.redis_queue
        )
        
        logger.info("進入主處理循環")
        
        # 主處理循環
        while True:
            try:
                # 從Redis消費數據
                data = consumer.consume(block=True)
                
                if data:
                    logger.info(f"收到任務: {json.dumps(data)}")
                    
                    # 處理數據
                    result = processor.process(data)
                    
                    if result['success']:
                        logger.info(f"處理成功: {result['image_path']}")
                    else:
                        logger.error(f"處理失敗: {result.get('error', 'Unknown error')}")
                
            except Exception as e:
                logger.error(f"處理任務時發生錯誤: {e}")
                # 短暫休眠以避免在發生錯誤時快速循環
                time.sleep(1)
    
    except Exception as e:
        logger.critical(f"系統初始化失敗: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
