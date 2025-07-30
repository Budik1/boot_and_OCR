from colorama import init
from colorama import Fore, Style

init()

# RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN
def tc_cyan(text):
    text_cyan_color = Fore.CYAN + text + Style.RESET_ALL
    return text_cyan_color


def tc_magenta(text):
    text_magenta_color = Fore.MAGENTA + text + Style.RESET_ALL
    return text_magenta_color


def tc_blue(text):
    text_blue_color = Fore.BLUE + text + Style.RESET_ALL
    return text_blue_color


def tc_yellow(text):
    text_yellow_color = Fore.YELLOW + text + Style.RESET_ALL
    return text_yellow_color


def tc_red(text):
    text_red_color = Fore.RED + text + Style.RESET_ALL
    return text_red_color


def tc_green(text):
    text_green_color = Fore.GREEN + text + Style.RESET_ALL
    return text_green_color
