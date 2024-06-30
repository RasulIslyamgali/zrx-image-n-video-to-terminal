import os
from subprocess import call
from typing import Optional

from colorama import Fore

BLACK_HEX = '#000000'
REDUCE_FONT_SIZE_COMMAND = 'ctrl+minus'
INCREASE_FONT_SIZE_COMMAND = 'ctrl+shift+plus'


def minimize_terminal_font_size(cycle_count: int = 20):
    for i in range(cycle_count):
        call(["xdotool", "key", REDUCE_FONT_SIZE_COMMAND])


def increase_terminal_font_size(cycle_count: int = 8):
    for i in range(cycle_count):
        call(["xdotool", "key", INCREASE_FONT_SIZE_COMMAND])


def change_terminal_background_color(colour_hex: str = BLACK_HEX):
    os.system(fr"echo -ne '\e]11;{colour_hex}\e\\'")


def get_colorama_colour_object(colour_str: Optional[str]) -> str:
    if colour_str is None:
        return Fore.LIGHTGREEN_EX

    if hasattr(Fore, colour_str):
        return getattr(Fore, colour_str)

    raise ValueError(f'colour name not found on {type(Fore)}')
