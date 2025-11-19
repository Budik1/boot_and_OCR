# https://python-scripts.com/pillow-crop
from PIL import Image


#D:\bot in br\testOCR\img\kv\result_round\result_round_loot\2025-09-06 08-01-27.png
def crop_shoulder_straps():
    name_to_save = 'D:/bot in br/testOCR/img/kv/result_round/result_round_loot/p5.png'
    name_open = 'D:/bot in br/testOCR/img/kv/result_round/result_round_loot/2025-09-06 08-01-27.png'
    img = Image.open(name_open)
    # img.show()
    #  box=(left, upper, right, lower)
    left = 25
    upper = 61
    right = 79 + left
    lower = 79 + upper
    img_crop = img.crop((left, upper, right, lower))
    img_crop.save(name_to_save)
    return

crop_shoulder_straps()