import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os
import sys

class PILTextDrawer:
    """
    用於高效繪製多個文字的類
    - 智能字體管理：可以只預加載字體文件，動態生成不同大小
    - 避免在循環中重複加載字體
    - 適合用於API服務，字體管理與圖像處理分離
    - 針對 cv2.imread() 返回的 numpy 陣列進行優化
    """
    def __init__(self, preload_fonts=None):
        """
        初始化文字繪製器

        參數:
        preload_fonts -- 支持以下幾種格式：
                1. 字體文件路徑列表：["simsun.ttc", "arial.ttf"]
                2. 字體和大小元組列表：[("simsun.ttc", 30), ("arial.ttf", 24)]
                3. 字體和大小範圍字典：{"simsun.ttc": (20, 40, 2)} - 從20到40，間隔2
        """
        # 字體緩存 - 使用嵌套字典：{font_path: {size: font_obj}}
        self.fonts = {}

        # 預加載字體
        if preload_fonts:
            self._preload_fonts(preload_fonts)

    def _preload_fonts(self, preload_fonts):
        """根據不同格式預加載字體"""
        if not preload_fonts:
            return

        if isinstance(preload_fonts, list):
            if len(preload_fonts) > 0:
                if isinstance(preload_fonts[0], str):
                    # 格式1: 只有字體路徑列表
                    for font_path in preload_fonts:
                        if font_path not in self.fonts:
                            self.fonts[font_path] = {}

                elif isinstance(preload_fonts[0], tuple) and len(preload_fonts[0]) == 2:
                    # 格式2: (字體路徑, 大小) 元組列表
                    for font_path, size in preload_fonts:
                        self._get_font(font_path, size)

        elif isinstance(preload_fonts, dict):
            # 格式3: {字體路徑: (最小大小, 最大大小, 間隔)}
            for font_path, size_range in preload_fonts.items():
                if len(size_range) >= 2:
                    min_size, max_size = size_range[0], size_range[1]
                    step = size_range[2] if len(size_range) > 2 else 1

                    for size in range(min_size, max_size + 1, step):
                        self._get_font(font_path, size)

    def _get_font(self, font_path, size):
        """獲取字體，優先從緩存中獲取"""
        # 確保size為整數
        size = int(size)

        # 初始化字體路徑對應的字典
        if font_path not in self.fonts:
            self.fonts[font_path] = {}

        # 檢查這個大小的字體是否已經加載
        full_font_path = font_path
        if size not in self.fonts[font_path]:
            try:
                # 如果font_path是字串，假定為字體文件路徑
                if isinstance(font_path, str):
                    if sys.platform.startswith('linux'):
                        core_dir = os.path.dirname(os.path.abspath(__file__))
                        fonts_dir = os.path.abspath(os.path.join(core_dir, "..", "fonts"))
                        full_font_path = os.path.join(fonts_dir, font_path)

                    font = ImageFont.truetype(full_font_path, size)
                # 如果font_path是OpenCV字體常數，使用默認字體
                else:
                    try:
                        # 嘗試使用系統默認字體
                        default_font = "arial.ttf" if "nt" in os.name else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
                        font = ImageFont.truetype(default_font, size)
                    except OSError:
                        # 如果找不到系統字體，使用PIL默認字體
                        font = ImageFont.load_default()
            except Exception as e:
                print(f"字體加載錯誤: {e}")
                # 使用PIL默認字體
                font = ImageFont.load_default()

            self.fonts[font_path][size] = font

        return self.fonts[font_path][size]

    def putText(self, img, text, org, font_face, font_size, color, thickness=1):
        """
        在圖像上繪製文字

        參數:
        img -- OpenCV圖像（numpy陣列，cv2.imread()的返回值），將被直接修改
        text -- 要繪製的文字
        org -- 文字起始位置 (x, y)
        font_face -- 字體路徑或OpenCV字體常數
        font_size -- 字體大小
        color -- 顏色 (B, G, R)
        thickness -- 字體粗細

        返回:
        img -- 修改後的圖像
        """
        # 檢查圖像是否有效
        if img is None or img.size == 0:
            print("錯誤: 無效的圖像")
            return img

        # 轉換為PIL格式
        if len(img.shape) == 3:  # 彩色圖像
            pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            is_color = True
        else:  # 灰度圖像
            pil_img = Image.fromarray(img)
            is_color = False

        # 創建繪圖對象
        draw = ImageDraw.Draw(pil_img)

        # 獲取字體
        font = self._get_font(font_face, font_size)

        # 顏色從BGR轉換為RGB
        color_rgb = (color[2], color[1], color[0])

        # 獲取文字尺寸並調整座標
        try:
            # 針對較新版本的Pillow (>=8.0.0)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            # 針對舊版本的Pillow
            _, text_height = draw.textsize(text, font=font)

        adjusted_org = (org[0], org[1] - text_height)

        # 處理文字粗細
        if thickness > 1:
            for dx in range(-thickness+1, thickness):
                for dy in range(-thickness+1, thickness):
                    if dx*dx + dy*dy <= thickness*thickness:
                        draw.text((adjusted_org[0] + dx, adjusted_org[1] + dy), text, font=font, fill=color_rgb)
        else:
            # 使用stroke_width參數（Pillow 8.0.0+）
            try:
                draw.text(adjusted_org, text, font=font, fill=color_rgb, stroke_width=thickness, stroke_fill=color_rgb)
            except TypeError:
                draw.text(adjusted_org, text, font=font, fill=color_rgb)

        # 轉換回OpenCV格式
        result = np.array(pil_img)
        if is_color:
            result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

        # 直接修改原圖像
        img_shape = img.shape
        result_shape = result.shape

        # 確保尺寸匹配
        if img_shape == result_shape:
            np.copyto(img, result)
        else:
            print(f"警告: 圖像尺寸不匹配。原始尺寸: {img_shape}, 結果尺寸: {result_shape}")
            # 如果尺寸不匹配，嘗試調整大小
            try:
                resized_result = cv2.resize(result, (img.shape[1], img.shape[0]))
                np.copyto(img, resized_result)
            except Exception as e:
                print(f"調整大小錯誤: {e}")
                # 作為最後的選擇，不修改原圖像，只返回新圖像
                return result

        # 返回修改後的圖像引用
        return img

# 使用範例
if __name__ == "__main__":
    # 方式1: 只預加載字體文件，不指定大小
    text_drawer1 = PILTextDrawer(preload_fonts=["simsun.ttc", "msyh.ttc"])

    # 方式2: 預加載特定字體和大小組合
    text_drawer2 = PILTextDrawer(preload_fonts=[
        ("simsun.ttc", 30),
        ("msyh.ttc", 36)
    ])

    # 方式3: 預加載字體大小範圍
    text_drawer3 = PILTextDrawer(preload_fonts={
        "simsun.ttc": (20, 40, 4),  # 20, 24, 28, 32, 36, 40
        "msyh.ttc": (24, 36, 6)     # 24, 30, 36
    })

    # 讀取圖像
    img = cv2.imread('input.jpg')  # 使用 cv2.imread() 讀取圖像

    # 在圖像上添加文字
    text_drawer3.putText(img, "CV2讀取的圖像", (50, 100), "simsun.ttc", 30, (255, 0, 0), 2)

    # 保存或顯示圖像
    cv2.imwrite('output.jpg', img)
    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()