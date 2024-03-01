import argparse
import pathlib
from typing import Optional

from config import MAX_HEIGHT, MAX_WIDTH, AUDIO_DIR, FPS
from utils.audio import save_audio_from_video_to_file
from utils.common import clear_terminal
from utils.image import get_image, print_img_to_terminal
from utils.video import print_video_to_terminal, download_video_from_youtube


def main(
        is_video: bool | int,
        youtube_link: Optional[str] = None,
        local_video_path: Optional[str] = None,
        local_image_path: Optional[str] = None,
) -> None:
    if is_video:
        if youtube_link:
            path_to_video = download_video_from_youtube(youtube_link)
        else:
            path_to_video = local_video_path
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
        image = get_image(local_image_path)
        print_img_to_terminal(image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube_link', default=None)
    parser.add_argument('--local_video_path', default=None)
    parser.add_argument('--local_image_path', default=None)
    args = parser.parse_args()
    chosen_sources_count = sum(
        (
            int(bool(args.youtube_link)),
            int(bool(args.local_video_path)),
            int(bool(args.local_image_path)),
        )
    )
    assert_msg = 'set exactly one source for image or video'
    assert chosen_sources_count == 1, assert_msg
    is_video = any((args.youtube_link, args.local_video_path))
    kwargs = {
        'is_video': is_video,
        'youtube_link': args.youtube_link,
        'local_video_path': args.local_video_path,
        'local_image_path': args.local_image_path,
    }
    try:
        main(**kwargs)
    except KeyboardInterrupt:
        clear_terminal()
        print('Goodbye!')
