from typing import Optional

import numpy as np
from PIL import Image
from colorama import Fore
from colorama.ansi import AnsiFore

from config import MAX_HEIGHT, MAX_WIDTH
from utils.common import write_to_terminal, clear_terminal, convert_array_to_text
from utils.types import PathType


def get_image(path: PathType) -> Image:
    return Image.open(path)


def resize_image(img: Image) -> Image:
    smaller_img = img.resize((MAX_WIDTH, MAX_HEIGHT))
    smaller_img_black_and_white = smaller_img.convert('1')

    return smaller_img_black_and_white


def get_images(paths: list[PathType]) -> list[Image]:
    images = []
    for path in paths:
        img = get_image(path)
        images.append(img)

    return images


def print_images_to_terminal(images: list[Image], ) -> None:
    clear_terminal()

    for img in images:
        print_img_to_terminal(img)


def print_img_to_terminal(
        img: Image,
        font_colour: Optional[AnsiFore] = Fore.LIGHTGREEN_EX,
) -> None:
    resized_img = resize_image(img)
    img_array = convert_img_to_array(resized_img)
    text = convert_array_to_text(img_array)

    write_to_terminal(text, font_colour)
    input('Press Ctrl+C for exit')


def convert_img_to_array(image):
    return np.array(image)
