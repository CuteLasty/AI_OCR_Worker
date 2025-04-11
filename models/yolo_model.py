import os
import torch
from ultralytics import YOLO
from loguru import logger

class YoloModel:
    def __init__(self, model_path="best.pt", device=None):
        """
        初始化YOLO模型
        
        Args:
            model_path (str): YOLO模型權重路徑
            device (str, optional): 運行模型的設備 ('cpu', '0', 等)
        """
        try:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"YOLO模型文件未找到: {model_path}")
                
            # 如果未提供，自動設置設備
            if device is None:
                self.device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
            else:
                self.device = device
                
            logger.info(f"從 {model_path} 加載YOLO模型到 {self.device}")
            self.model = YOLO(model_path)
            self.model.to(self.device)
            logger.info("YOLO模型成功加載")
        
        except Exception as e:
            logger.error(f"初始化YOLO模型失敗: {e}")
            raise
    
    def detect(self, image_path):
        """
        檢測圖像中的物體
        
        Args:
            image_path (str): 圖像路徑
            
        Returns:
            list: 檢測到的物體列表，帶有邊界框
        """
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"圖像文件未找到: {image_path}")
                
            logger.info(f"在 {image_path} 上運行YOLO檢測")
            results = self.model(image_path)
            
            # 提取檢測結果
            detections = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    conf = box.conf[0].item()
                    cls = int(box.cls[0].item())
                    cls_name = result.names[cls]
                    
                    detections.append({
                        'xyxy': [x1, y1, x2, y2],
                        'confidence': conf,
                        'class': cls,
                        'class_name': cls_name
                    })
            
            logger.info(f"YOLO檢測完成，發現 {len(detections)} 個物體")
            return detections
            
        except Exception as e:
            logger.error(f"YOLO檢測過程中出錯: {e}")
            raise
    
    def find_largest_box(self, detections):
        """
        從檢測結果中找到最大的邊界框
        
        Args:
            detections (list): 檢測結果列表
            
        Returns:
            dict: 最大的邊界框，如果沒有檢測到則為None
        """
        if not detections:
            return None
            
        largest_box = None
        max_area = 0
        
        for det in detections:
            x1, y1, x2, y2 = det['xyxy']
            area = (x2 - x1) * (y2 - y1)
            
            if area > max_area:
                max_area = area
                largest_box = det
                
        return largest_box
