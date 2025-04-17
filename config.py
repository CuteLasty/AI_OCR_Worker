# Redis配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_QUEUE = 'label_queue'

# 路徑配置
BACKUP_BASE = 'backup'
RESULT_BASE = 'results'
TEMPLATE_DIR = 'template'
YOLO_MODEL_PATH = 'best.pt'

# OCR配置
OCR_LANG = 'ch'
USE_GPU = True
DET_DB_THRESH = 0.3
DET_DB_BOX_THRESH = 0.5
DROP_SCORE = 0.5
MAX_TEXT_LENGTH = 25
