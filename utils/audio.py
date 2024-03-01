from typing import Optional

import ffmpeg
from pygame import mixer

from utils.common import is_file_exists
from utils.types import PathType

mixer.init()


def save_audio_from_video_to_file(path_to_video: PathType, path_to_save: PathType, acodec: str = 'mp3') -> None:
    if is_file_exists(path_to_save):
        return

    input_file = ffmpeg.input(path_to_video)
    input_file.output(filename=path_to_save, acodec=acodec).run()


def play_audio(path: Optional[PathType]) -> None:
    if path is None:
        return
    mixer.music.load(path)
    mixer.music.play()


def pause_audio() -> None:
    mixer.music.pause()


def unpause_audio() -> None:
    mixer.music.unpause()


def stop_audio() -> None:
    mixer.music.stop()
