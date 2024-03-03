import pyautogui
from fun import foto, move_to_click
from time import sleep

def cr_img():
    reg = 156,262, 80, 38
    foto("img/test/fol/folder_test_blue.png", reg)

# 127,191

# pyautogui.mouseInfo()
# cr_img()
folder_test_black = pyautogui.locateCenterOnScreen("img/test/fol/folder_test_black.png", confidence=0.99)
folder_test_blue = pyautogui.locateCenterOnScreen("img/test/fol/folder_test_blue.png", confidence=0.99)
folder_test_gray = pyautogui.locateCenterOnScreen("img/test/fol/folder_test_gray.png", confidence=0.99)
if not folder_test_black or not folder_test_blue or not folder_test_gray:
    folder_img_black = pyautogui.locateCenterOnScreen("img/test/fol/folder_img_black.png", confidence=0.99)
    folder_img_blue = pyautogui.locateCenterOnScreen("img/test/fol/folder_img_blue.png", confidence=0.99)
    folder_img_gray = pyautogui.locateCenterOnScreen("img/test/fol/folder_img_gray.png", confidence=0.99)


folder_black = pyautogui.locateCenterOnScreen("img/test/fol/folder_black.png", confidence=0.99)
folder_blue = pyautogui.locateCenterOnScreen("img/test/fol/folder_blue.png", confidence=0.99)
folder_gray = pyautogui.locateCenterOnScreen("img/test/fol/folder_gray.png", confidence=0.99)
if folder_black:
    print("black")
    move_to_click(folder_black, 0.3)
elif folder_blue or folder_gray:
    print("blue or gray")





