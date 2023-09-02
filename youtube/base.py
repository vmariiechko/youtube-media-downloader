import logging
from pathlib import Path

from moviepy.editor import VideoFileClip


class YouTubeBase:
    def __init__(
        self,
        url: str,
        logger: logging.Logger,
        output_path: str = "",
        quick_download=True,
    ) -> None:
        self.url = url
        self.logger = logger

        self.download_dir = Path(output_path).absolute()
        self.download_dir.mkdir(parents=True, exist_ok=True)

        self.quick_download = quick_download

    def convert_to_mp3(self, video_path: str, audio_path: str) -> None:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile("example.mp3")
