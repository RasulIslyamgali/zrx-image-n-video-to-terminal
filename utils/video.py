import cv2

from config import MAX_WIDTH, MAX_HEIGHT
from utils.common import write_to_terminal, clear_terminal, pause, convert_array_to_text


def get_frames_from_video(video_path: str):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.release()
            raise StopIteration
        yield frame


def print_video_to_terminal(video_path: str, height: int, width: int, fps: float = 0.058) -> None:
    for frame in get_frames_from_video(video_path):
        resized_frame = cv2.resize(frame, (MAX_WIDTH, MAX_HEIGHT))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        # Convert to binary (black and white)
        _, resized_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

        text = convert_array_to_text(resized_frame)
        write_to_terminal(text)

        pause(fps)
        clear_terminal()
