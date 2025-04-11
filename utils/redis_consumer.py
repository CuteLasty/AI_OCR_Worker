import json
import time
import redis
from loguru import logger

class RedisConsumer:
    def __init__(self, host='localhost', port=6379, db=0, queue_key='label_queue'):
        """
        初始化Redis消費者
        
        Args:
            host (str): Redis主機
            port (int): Redis端口
            db (int): Redis數據庫編號
            queue_key (str): Redis隊列鍵
        """
        try:
            self.queue_key = queue_key
            logger.info(f"連接到Redis {host}:{port}/{db}")
            self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)
            
            # 測試連接
            self.redis.ping()
            logger.info("成功連接到Redis")
            
        except Exception as e:
            logger.error(f"連接到Redis失敗: {e}")
            raise
    
    def consume(self, block=True, timeout=0):
        """
        從Redis隊列消費最舊的消息
        
        Args:
            block (bool): 是否阻塞直到有數據可用
            timeout (int): 超時時間（秒）（0 = 無限）
            
        Returns:
            dict: 消息數據或超時時為None
        """
        try:
            logger.debug(f"等待來自{self.queue_key}的消息")
            
            if block:
                # 使用BLPOP進行阻塞操作
                result = self.redis.blpop(self.queue_key, timeout=timeout)
                if result:
                    _, data = result
                    logger.info("從Redis接收到消息")
                    return json.loads(data)
                else:
                    logger.debug("等待消息超時")
                    return None
            else:
                # 使用LPOP進行非阻塞操作
                data = self.redis.lpop(self.queue_key)
                if data:
                    logger.info("從Redis接收到消息")
                    return json.loads(data)
                else:
                    logger.debug("沒有可用消息")
                    return None
                    
        except json.JSONDecodeError as e:
            logger.error(f"解析JSON數據失敗: {e}")
            # 在錯誤消息的情況下繼續消費
            return None
            
        except Exception as e:
            logger.error(f"從Redis消費時出錯: {e}")
            # 連接問題時短暫睡眠然後重試
            time.sleep(1)
            return None
