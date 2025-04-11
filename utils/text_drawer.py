import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from loguru import logger

class PILTextDrawer:
    def __init__(self, font_path="fonts/simsun.ttc"):
        """
        初始化文字繪製器
        
        Args:
            font_path (str): 字體文件路徑
        """
        try:
            self.font_path = font_path
            logger.info(f"初始化PILTextDrawer，字體路徑: {font_path}")
        except Exception as e:
            logger.error(f"PILTextDrawer初始化失敗: {e}")
            raise
    
    def putText(self, img, text, org, font_face, font_size, color, thickness=1):
        """
        在圖像上繪製文字
        
        Args:
            img: OpenCV圖像（numpy陣列）
            text: 要繪製的文字
            org: 文字起始位置 (x, y)
            font_face: 字體路徑或OpenCV字體常數
            font_size: 字體大小
            color: 顏色 (B, G, R)
            thickness: 字體粗細
            
        Returns:
            img: 修改後的圖像
        """
        try:
            # 如果font_face是字串，則使用該路徑作為字體文件
            if isinstance(font_face, str):
                font_path = font_face
            else:
                # 否則使用預設字體
                font_path = self.font_path
                
            # 創建PIL圖像
            pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)
            
            # 創建字體
            font = ImageFont.truetype(font_path, font_size)
            
            # 在PIL圖像上繪製文字
            # 注意：PIL的color是RGB格式，而OpenCV是BGR格式
            draw.text(org, text, font=font, fill=(color[2], color[1], color[0]), width=thickness)
            
            # 將PIL圖像轉換回OpenCV格式
            result_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            
            # 複製結果到原始圖像
            np.copyto(img, result_img)
            
            return img
            
        except Exception as e:
            logger.error(f"putText出錯: {e}")
            return img
