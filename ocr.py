from paddleocr import PaddleOCR

# OCR识别模块
class OCRDetector:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=False, lang="ch")

    def predict(self, img):
        result = self.ocr.ocr(img, cls=True)

        max_line = 5
        ingredients = []
        for result in result:
            for line in result:
                text = line[1][0]  # 获取识别出来的文本

                ingredients.append(text.replace('配料', '').replace(':', '').replace('：', ''))
                if len(ingredients) >= max_line or text.endswith('。'):
                    break

        # 多行配料合成1行
        res = ''.join(ingredients)
        res = res.replace('。', '')

        return res
