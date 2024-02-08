from config import MAX_HEIGHT, MAX_WIDTH
from utils.image import get_images, print_images_to_terminal
from utils.video import print_video_to_terminal


def main(is_video: bool) -> None:
    FPS = 0.058 if is_video else 3

    if is_video:
        print_video_to_terminal('media/videos/brad_pitt_interview.mp4', height=MAX_HEIGHT, width=MAX_WIDTH, fps=FPS)
    else:
        images_paths = [
            'media/man_portrait.jpg',
            'media/sportcar1.png',
        ]

        images = get_images(images_paths)
        print_images_to_terminal(images, fps=FPS)


if __name__ == '__main__':
    IS_VIDEO = True
    main(IS_VIDEO)
