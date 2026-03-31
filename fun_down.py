import pyautogui


def locateCenterImg(img: str, confidence=0.9, region: tuple[int, int, int, int] | None = None, grayscale=None):
    try:
        pos_img = pyautogui.locateCenterOnScreen(img,
                                                 confidence=confidence,
                                                 region=region,
                                                 grayscale=grayscale)
    except IOError:
        path_list = img.split(sep='/')
        fold = path_list[1]
        name_file = path_list[-1]
        print(f'Видимо в масштабе {fold} файла "{name_file}" ещё нет')
        print()
        pos_img = None
    except Exception as kod:
        print(kod)
        pos_img = None
    return pos_img
