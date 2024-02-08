import pathlib
from typing import Optional

from config import MAX_HEIGHT, MAX_WIDTH, VIDEO_DIR, AUDIO_DIR, MEDIA_DIR, PAUSE_BETWEEN_VIDEO_FRAMES
from utils.audio import save_audio_from_video_to_file
from utils.image import get_images, print_images_to_terminal
from utils.video import print_video_to_terminal, download_video_from_youtube


def main(
        is_video: bool,
        youtube_link: Optional[str] = None,
        path_to_pre_downloaded_video: Optional[str] = None,
) -> None:
    FPS = PAUSE_BETWEEN_VIDEO_FRAMES if is_video else 3

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
            MEDIA_DIR / 'man_portrait.jpg',
            MEDIA_DIR / 'sportcar1.png',
        ]

        images = get_images(images_paths)
        print_images_to_terminal(images, fps=FPS)


if __name__ == '__main__':
    IS_VIDEO = True
    youtube_link = input('set youtube link>\n')  # если есть линк в ютуб видео оно юзается, иначе
    path_to_pre_downloaded_video = 'brad_pitt_interview.mp4'  # предустановленное видео

    main(IS_VIDEO, youtube_link=youtube_link, path_to_pre_downloaded_video=path_to_pre_downloaded_video)
