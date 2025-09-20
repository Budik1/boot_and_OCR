from colorama import Fore, Style
from colorama import init

init()


def tc_cyan(text):
    """голубой"""
    text_cyan_color = Fore.CYAN + text + Style.RESET_ALL
    return text_cyan_color


def tc_magenta(text):
    """фиолетовый"""
    text_magenta_color = Fore.MAGENTA + text + Style.RESET_ALL
    return text_magenta_color


def tc_blue(text):
    """синий"""
    text_blue_color = Fore.BLUE + text + Style.RESET_ALL
    return text_blue_color


def tc_yellow(text):
    """желтый"""
    text_yellow_color = Fore.YELLOW + text + Style.RESET_ALL
    return text_yellow_color


def tc_red(text):
    """красный"""
    text_red_color = Fore.RED + text + Style.RESET_ALL
    return text_red_color


def tc_green(text):
    """зеленый"""
    text_green_color = Fore.GREEN + text + Style.RESET_ALL
    return text_green_color
