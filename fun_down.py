import pyautogui


def locateCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None):
    pos_img = pyautogui.locateCenterOnScreen(name_img,
                                             confidence=confidence,
                                             region=region)
    return pos_img
