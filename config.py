import os
import pathlib


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)


MAX_HEIGHT, MAX_WIDTH = get_terminal_size()

BASE_DIR = pathlib.Path(__file__).parent
MEDIA_DIR = BASE_DIR / 'media'
AUDIO_DIR = MEDIA_DIR / 'audio'
VIDEO_DIR = MEDIA_DIR / 'videos'
IMG_DIR = MEDIA_DIR / 'img'
FPS = 0.095
FRAME_RATE = 3
CACHE_FILE_NAME = 'cache.json'
CACHE_FILE_PATH = BASE_DIR / CACHE_FILE_NAME
