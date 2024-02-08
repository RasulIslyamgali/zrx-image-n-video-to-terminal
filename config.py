import pathlib

WITH_MONITOR = False

MAX_HEIGHT = 90
MAX_WIDTH = 280

if WITH_MONITOR:  # font size 5
    pass
else:
    MAX_HEIGHT *= 2.6
    MAX_HEIGHT = int(MAX_HEIGHT)
    MAX_WIDTH *= 4.5
    MAX_WIDTH = int(MAX_WIDTH)

BASE_DIR = pathlib.Path(__file__).parent
MEDIA_DIR = BASE_DIR / 'media'
AUDIO_DIR = MEDIA_DIR / 'audio'
VIDEO_DIR = MEDIA_DIR / 'videos'
IMG_DIR = MEDIA_DIR / 'img'
PAUSE_BETWEEN_VIDEO_FRAMES = 0.095
FRAME_RATE = 3
CACHE_FILE_NAME = 'cache.json'
CACHE_FILE_PATH = BASE_DIR / CACHE_FILE_NAME
