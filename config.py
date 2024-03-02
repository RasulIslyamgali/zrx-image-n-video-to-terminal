import os
import pathlib


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)


if os.path.exists('/.dockerenv'):
    MAX_HEIGHT = int(os.getenv('max_height'))
    MAX_WIDTH = int(os.getenv('max_width'))
    MAX_WIDTH, MAX_HEIGHT = MAX_HEIGHT, MAX_WIDTH
else:
    MAX_HEIGHT, MAX_WIDTH = get_terminal_size()
    MAX_HEIGHT = int(MAX_HEIGHT * 0.95)

BASE_DIR = pathlib.Path(__file__).parent
MEDIA_DIR = BASE_DIR / 'media'
AUDIO_DIR = MEDIA_DIR / 'audio'
VIDEO_DIR = MEDIA_DIR / 'videos'
IMG_DIR = MEDIA_DIR / 'img'
FPS = 0.095
FRAME_RATE = 3
CACHE_FILE_NAME = 'cache.json'
CACHE_FILE_PATH = BASE_DIR / CACHE_FILE_NAME
