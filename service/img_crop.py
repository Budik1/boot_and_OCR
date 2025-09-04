from PIL import Image


def crop_shoulder_straps():
    name_to_save = '..img/kv/result_all_round/p/2.png'
    name_open = 'D:\\bot in br\\testOCR\\service\\27.png'
    img = Image.open(name_open)
    img_crop = img.crop(((108 + 4), (182 + 4), (220 - 24), (294 - 25)))
    img_crop.save(name_to_save)
    return

crop_shoulder_straps()