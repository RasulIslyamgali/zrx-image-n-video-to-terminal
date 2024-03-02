FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get update && apt-get install -y alsa-utils

# TODO add multistage building for ffmpeg
# TODO may be als-utils is not required after usign --device /dev/snd

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV youtube_link=""
ENV local_video_path=""
ENV local_image_path=""
ENV use_camera=""


COPY . /app

CMD python main.py \
    --youtube_link=$youtube_link \
    --local_video_path=$local_video_path \
    --local_image_path=$local_image_path \
    --use_camera=$use_camera
