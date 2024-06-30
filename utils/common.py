import json
import os
import time
from typing import Optional, Any

import colorama
from colorama import Fore

from config import CACHE_FILE_PATH
from utils.types import PathType

colorama.init()


def save_to_file(image, file_name: str = 'media/test.png') -> None:
    with open(file_name, 'wb') as f:
        image.save(f)


def write_to_terminal(text: str, colour: Fore = Fore.LIGHTGREEN_EX) -> None:
    print(colour + text, end='')


def clear_terminal():
    os.system('clear')


def pause(seconds: float) -> None:
    time.sleep(seconds)


def convert_array_to_text(img_array, symbol='\u2592') -> str:
    text_img = ''

    for one_dimension_array in img_array:
        line = ''.join([symbol if x else ' ' for x in one_dimension_array])
        text_img += line + '\n'

    return text_img


def is_file_exists(path: PathType) -> bool:
    return os.path.exists(path)


def add_to_cache(key: str, value: str):
    data = {}

    if is_file_exists(CACHE_FILE_PATH):
        with open(CACHE_FILE_PATH, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                pass

    data[key] = str(value)

    with open(CACHE_FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_in_cache(key: str) -> Optional[Any]:
    if is_file_exists(CACHE_FILE_PATH):
        with open(CACHE_FILE_PATH, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return None

            if key in data:
                return data[key]

    return None
