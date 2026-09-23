# https://python-scripts.com/pillow-crop
from PIL import Image


def crop_shoulder_straps(*, name_to_save, name_open):
    # name_to_save = 'C:/python/bot_ocr1/img/kv/result_round/loot/p2.png'
    # name_open = 'C:/python/bot_ocr1/img/kv/result_round/p/2025-12-03 19-56-28.png'
    img = Image.open(name_open)
    # img.show()
    #  box=(left, upper, right, lower)
    left = 72
    upper = 240
    right = 80 + left
    lower = 80 + upper
    img_crop = img.crop((left, upper, right, lower))
    img_crop.save(name_to_save)
    return


def get_size_img(*, name_img):
    """
    Получение размеров картинки.
    :param name_img: Путь/имя картинки.
    :return: Ширина, высота.
    """
    img = Image.open(name_img)
    width, height = img.size
    return width, height
