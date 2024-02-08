import os
import time


def save_to_file(image, file_name: str = 'media/test.png') -> None:
    with open(file_name, 'wb') as f:
        image.save(f)


def write_to_terminal(text: str) -> None:
    print(text, end='')


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
