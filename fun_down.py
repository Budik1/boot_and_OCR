import pyautogui


def locateCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None, grayscale=None):
    pos_img = pyautogui.locateCenterOnScreen(name_img,
                                             confidence=confidence,
                                             region=region,
                                             grayscale=grayscale)
    return pos_img
