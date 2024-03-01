import pathlib
from typing import Optional

from config import MAX_HEIGHT, MAX_WIDTH, VIDEO_DIR, AUDIO_DIR, IMG_DIR, PAUSE_BETWEEN_VIDEO_FRAMES
from utils.audio import save_audio_from_video_to_file
from utils.image import get_images, print_images_to_terminal
from utils.video import print_video_to_terminal, download_video_from_youtube


def main(
        is_video: bool | int,
        youtube_link: Optional[str] = None,
        path_to_pre_downloaded_video: Optional[str] = None,
) -> None:
    FPS = PAUSE_BETWEEN_VIDEO_FRAMES if is_video else 60

    if is_video:
        path_to_video = download_video_from_youtube(
            youtube_link) if youtube_link else VIDEO_DIR / path_to_pre_downloaded_video
        path_to_audio_from_video = AUDIO_DIR / f'{pathlib.Path(path_to_video).stem}.mp3'
        save_audio_from_video_to_file(path_to_video, path_to_audio_from_video)
        print_video_to_terminal(
            path_to_video,
            height=MAX_HEIGHT,
            width=MAX_WIDTH,
            fps=FPS,
            path_to_audio_file=path_to_audio_from_video,
        )
    else:
        images_paths = [
            IMG_DIR / 'car.png',
        ]

        images = get_images(images_paths)
        print_images_to_terminal(images, fps=FPS)


if __name__ == '__main__':
    is_video = int(input('This is video?: answer 1 if is else 0'))
    youtube_link = ''
    pre_downloaded_video_name = ''
    if is_video:
        youtube_link = input('set youtube link or just press enter for skip>\n')
        if not youtube_link.strip():
            pre_downloaded_video_name = input('set pre download video name>\n')
        assert youtube_link.strip() or pre_downloaded_video_name.strip(), 'set either youtube link or video name'
    main(is_video, youtube_link=youtube_link, path_to_pre_downloaded_video=pre_downloaded_video_name)
