import sys

import cv2
from pytube import YouTube

from config import VIDEO_DIR, FRAME_RATE
from utils.audio import play_audio, stop_audio, unpause_audio, pause_audio
from utils.common import (
    write_to_terminal,
    clear_terminal,
    pause,
    convert_array_to_text,
    is_file_exists,
    add_to_cache,
    get_in_cache,
)
from utils.types import PathType


def get_frames_from_video(video_path: PathType):
    cap = cv2.VideoCapture(str(video_path))
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.release()
            return
        frame_count += 1
        if frame_count % FRAME_RATE == 0:  # Check if it's the third frame
            yield frame


def print_video_to_terminal(
        video_path: str,
        height: int,
        width: int,
        path_to_audio_file: PathType,
        fps: float = 0.058,
) -> None:
    clear_terminal()

    is_first_loop = True
    for frame in get_frames_from_video(video_path):
        try:
            resized_frame = cv2.resize(frame, (width, height))
            gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
            # Convert to binary (black and white)
            _, resized_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

            text = convert_array_to_text(resized_frame)
            write_to_terminal(text)

            if is_first_loop:
                play_audio(path_to_audio_file)
                is_first_loop = False

            pause(fps)
            clear_terminal()
        except KeyboardInterrupt:
            pause_audio()
            input('Video paused press enter to resume or Ctrl+C for exit')
            unpause_audio()
    stop_audio()


def download_video_from_youtube(link: str, file_extension: str = '.mp4') -> PathType:
    if file_path := get_in_cache(link):
        return file_path

    yt = YouTube(link)
    video = yt.streams.get_lowest_resolution()

    file_name = video.title.replace(' ', '-') + file_extension
    file_path = VIDEO_DIR / file_name

    if is_file_exists(file_path):
        pass
    else:
        video.download(output_path=VIDEO_DIR, filename=file_name)

    add_to_cache(link, file_path)

    return file_path
