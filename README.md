# 標籤處理系統

這個專案提供了一個系統，用於使用YOLO物件檢測和PaddleOCR文字識別來處理和分析標籤圖像。

## 功能特點

- 使用YOLO檢測圖像中的標籤
- 使用PaddleOCR從標籤中提取文字
- 處理條碼(barcode)和文字(text)標籤
- 根據模板分析標籤
- 視覺化OCR和分析結果
- 基於Redis的處理請求隊列

## 專案結構

專案組織為多個模組：

- `main.py`: 應用程式的主要入口點
- `models/`: 包含核心處理類
- `analyzers/`: 包含不同標籤類型的分析邏輯
- `utils/`: 包含檔案、圖像和Redis操作的實用函數
- `templates/`: 包含用於分析的標籤模板
- `logs/`: 包含應用程式日誌
- `backups/`: 包含處理過的圖像備份
- `results/`: 包含處理結果

詳細的目錄結構請查看`project_structure.md`文件。

## 需求

- Python 3.11或更高版本
- PaddlePaddle和PaddleOCR
- YOLOv8 (通過Ultralytics)
- Redis伺服器
- OpenCV
- 其他依賴列在`requirements.txt`中

## 安裝

1. 克隆存儲庫：
   ```bash
   git clone https://github.com/yourusername/label-processor.git
   cd label-processor
   ```

2. 創建虛擬環境(建議)：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在Windows上: venv\Scripts\activate
   ```

3. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

4. 下載PaddleOCR模型文件：
   ```bash
   mkdir -p ch_PP-OCRv4_det_server_infer ch_PP-OCRv4_rec_server_infer ch_ppocr_mobile_v2.0_cls_infer
   paddleocr --download_dir ./ ch_PP-OCRv4_det_server_infer ch_PP-OCRv4_rec_server_infer ch_ppocr_mobile_v2.0_cls_infer
   ```

5. 將您的YOLO模型文件(`best.pt`)放在專案根目錄或在`config.py`中更新路徑。

## 使用方法

1. 如果尚未運行，啟動Redis伺服器：
   ```bash
   redis-server
   ```

2. 通過編輯`config.py`配置應用程式。

3. 啟動標籤處理器：
   ```bash
   python main.py
   ```

4. 以JSON格式向Redis隊列發送任務：

   對於條碼標籤：
   ```json
   {
       "image_path": "path/to/image/01.jpg",
       "timestamp": "YYYYMMDD_HHMMSS",
       "type": "barcode"
   }
   ```

   對於文字標籤：
   ```json
   {
       "image_path": "path/to/image/02.jpg",
       "timestamp": "YYYYMMDD_HHMMSS",
       "type": "text",
       "sku_name": "SKU-123456"
   }
   ```

5. 結果將保存到配置的結果目錄中。

## 模板格式

模板以JSON文件形式存儲在`templates`目錄中，按標籤類型組織。

條碼模板示例 (`templates/barcode/SKU-123456.json`):
```json
{
    "sku_name": "SKU-123456",
    "rules": [
        {
            "type": "contains",
            "pattern": "123456"
        },
        {
            "type": "contains",
            "pattern": "產品名稱"
        }
    ]
}
```

文字模板示例 (`templates/text/SKU-123456.json`):
```json
{
    "sku_name": "SKU-123456",
    "rules": [
        {
            "type": "exact",
            "text": "產品名稱",
            "position": {
                "x": 100,
                "y": 100,
                "width": 200,
                "height": 50
            }
        }
    ]
}
```

## 許可證

本專案根據MIT許可證授權 - 詳見LICENSE文件。