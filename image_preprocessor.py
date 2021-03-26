from PIL import Image, ImageOps

def preprocess(src, width, height):
    gray_img = src.convert("L")
    resized_img = gray_img.resize((width, height))
    res = ImageOps.invert(resized_img)#색상 반전
    return res