from colorama import init
from colorama import Fore, Style

init()

# RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN
def text_cyan(text):
    text_cyan_color = Fore.CYAN + text + Style.RESET_ALL
    return text_cyan_color


def text_magenta(text):
    text_magenta_color = Fore.MAGENTA + text + Style.RESET_ALL
    return text_magenta_color


def text_blue(text):
    text_blue_color = Fore.BLUE + text + Style.RESET_ALL
    return text_blue_color


def text_yellow(text):
    text_yellow_color = Fore.YELLOW + text + Style.RESET_ALL
    return text_yellow_color


def text_red(text):
    text_red_color = Fore.RED + text + Style.RESET_ALL
    return text_red_color


def text_green(text):
    text_green_color = Fore.GREEN + text + Style.RESET_ALL
    return text_green_color
