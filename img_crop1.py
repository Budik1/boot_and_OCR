# https://python-scripts.com/pillow-crop
from PIL import Image

collection = [50, 50, 59, 59]
many = [25, 5, 88, 30]


def crop_shoulder_straps():
    name_to_save = 'img/tonelli/loot_gift_box/big/all/colonel.png'
    name_open = 'img/tonelli/loot_gift_box/big/gady/12.png'
    img = Image.open(name_open)
    # img.show()
    #  box=(left, upper, right, lower)
    left = 50
    upper = 50
    right = 59 + left
    lower = 59 + upper
    img_crop = img.crop((left, upper, right, lower))
    img_crop.save(name_to_save)
    return


crop_shoulder_straps()
