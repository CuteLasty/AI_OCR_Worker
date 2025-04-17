# 專案目錄結構

```
label-processor/
├── main.py                    # 主要入口點
├── config.py                  # 配置設定
├── requirements.txt           # 依賴項
├── README.md                  # 專案文檔
├── project_structure.md       # 目錄結構文檔
├── fonts/
│   └── simsun.ttc             # 中文字體檔案
├── models/
│   ├── __init__.py            # 套件初始化
│   ├── label_processor.py     # 主要LabelProcessor類
│   ├── ocr_model.py           # OCR模型包裝器
│   └── yolo_model.py          # YOLO模型包裝器
├── analyzers/
│   ├── __init__.py            # 套件初始化
│   ├── barcode_analyzer.py    # 條碼分析
│   └── text_analyzer.py       # 文字分析
├── utils/
│   ├── __init__.py            # 套件初始化
│   ├── file_utils.py          # 檔案操作工具
│   ├── image_utils.py         # 圖像處理工具
│   ├── text_drawer.py         # PIL文字繪製工具
│   └── redis_consumer.py      # Redis消費者實現
├── templates/                 # 模板目錄
│   ├── barcode/               # 條碼模板
│   │   └── SKU-123456.json    # 範例條碼模板
│   └── text/                  # 文字模板
│       └── SKU-123456.json    # 範例文字模板
├── logs/                      # 日誌目錄
│   └── label_processor.log    # 應用程式日誌文件
├── backups/                   # 備份目錄
│   └── YYYYMMDD/              # 基於日期的目錄
│       └── HHMMSS/            # 基於時間的目錄
└── results/                   # 結果目錄
    └── YYYYMMDD/              # 基於日期的目錄
        └── HHMMSS/            # 基於時間的目錄
            ├── raw_image.jpg  # 裁剪的原始圖像
            ├── pp_image.jpg   # 預處理圖像
            ├── text_image.jpg # 帶OCR可視化的圖像
            ├── tag_image.jpg  # 帶分析可視化的圖像
            ├── ocr_results_image.json # OCR結果
            └── analysis_results_image.json # 分析結果
```