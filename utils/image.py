import numpy as np
from PIL import Image

from config import MAX_HEIGHT, MAX_WIDTH
from utils.types import PathType
from utils.common import write_to_terminal, clear_terminal, pause, convert_array_to_text


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


def print_images_to_terminal(images: list[Image], fps: float = 3) -> None:
    for img in images:
        resized_img = resize_image(img)
        img_array = convert_img_to_array(resized_img)
        text = convert_array_to_text(img_array)
        write_to_terminal(text)

        pause(fps)
        clear_terminal()


def convert_img_to_array(image):
    return np.array(image)
