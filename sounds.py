from playsound3 import playsound
import pyttsx3


def say_txt(phrase):
    tts = pyttsx3.init()
    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru')
    # tts.save_to_file(phrase, 'name.mp3')
    tts.say(phrase)
    tts.runAndWait()


def click_mouse():
    playsound('sound/mouse-click.wav')
    return


def sound_vic(block: bool = True):
    playsound('sound/success.mp3')
    return


def sound_victory():
    playsound('sound/victory.mp3')
