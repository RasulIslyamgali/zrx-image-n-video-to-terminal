<img src="redmi_media/img.png" width=500>

<img src="redmi_media/demo.gif" width=500>

#### video [from](https://www.youtube.com/watch?v=EOLafh8DPFM&t) 

## How to use?

### [install ffmpeg ](https://phoenixnap.com/kb/install-ffmpeg-ubuntu) for audio extracting process

### show YouTube video
`$ python main.py --youtube_link="https://www.youtube.com/watch?v=EOLafh8DPFM&t"`

### show local video
`$ python main.py --local_video_path=/home/rasul/Personal/py/zrx/media/video/cherimoya.mp4`

### show local image
`$ python main.py --local_image_path=/home/rasul/Personal/py/zrx/media/img/car.jpg`

### show video from camera
`$ python main.py --use_camera=1`


## Tips
> Stop video using Ctrl+C and resume by pressing Enter. Double Ctrl+C for exit

> For high resolution on terminal temporary change terminal font size to 1


## INFO

```
3rd dimensional matrix

[
  [ [199, 213, 216, 255] - pixel, RGB, and 4th value is alpha channel: transparency or opacity
    [199, 213, 212, 255], 
    [199, 213, 220, 255], 
    [199, 213, 216, 255] ] - row
]
```
