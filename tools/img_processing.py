# https://python-scripts.com/pillow-crop
from PIL import Image
import baza.paths_img

def crop_shoulder_straps(*, name_to_save, name_open, shift_left, shift_upper, shift_right, shift_lower):
    # name_to_save = 'C:/python/bot_ocr1/img/kv/result_round/loot/p2.png'
    # name_open = 'C:/python/bot_ocr1/img/kv/result_round/p/2025-12-03 19-56-28.png'
    img = Image.open(name_open)
    # img.show()
    #  box=(left, upper, right, lower)
    left = shift_left
    upper = shift_upper
    right = shift_right + left
    lower = shift_lower + upper
    img_crop = img.crop((left, upper, right, lower))
    ask = input(f'Создать {name_to_save}(y) или token.png(t) :')
    if ask == 'y':
        img_crop.save(name_to_save)
        print(f'{name_to_save} создан')
    elif ask == 't':
        img_crop.save(baza.paths_img.token_png)
        print(f'{baza.paths_img.token_png} создан')
    else:
        print('Выход без создания')


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
