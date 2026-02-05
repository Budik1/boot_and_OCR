# https://python-scripts.com/pillow-crop
from PIL import Image


# D:\bot in br\testOCR\img\kv\result_round\result_round_loot\2025-09-06 08-01-27.png
def crop_shoulder_straps():
    name_to_save = 'C:/python/bot_ocr1/img/kv/result_round/loot/p2.png'
    name_open = 'C:/python/bot_ocr1/img/kv/result_round/p/2025-12-03 19-56-28.png'
    img = Image.open(name_open)
    # img.show()
    #  box=(left, upper, right, lower)
    left = 25 + 45
    upper = 61 + 60 + 37
    right = 79 + 3 + left
    lower = 79 + 3 + upper
    img_crop = img.crop((left, upper, right, lower))
    img_crop.save(name_to_save)
    return


# crop_shoulder_straps()
