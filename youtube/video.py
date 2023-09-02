from pathlib import Path

import pytube
from mutagen.mp3 import MP3  # TODO remove?

from youtube.base import YouTubeBase


class YouTubeVideo(YouTubeBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        try:
            self.video = pytube.YouTube(self.url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(f"Failed to initialize YT video:\n{e}")

    def download_audio(self) -> None:
        if self.quick_download:
            audio_stream = self.video.streams.filter(only_audio=True).first()
        else:
            audio_stream = (
                self.video.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
        download_path = Path(audio_stream.download(str(self.download_dir)))

        if self.quick_download:
            download_path = download_path.replace(download_path.with_suffix(".mp3"))
            audio = MP3(str(download_path.with_suffix(".mp3")))
            self.logger.info(f"Bitrate: {audio.info.bitrate}")
        else:
            self.convert_to_mp3(download_path, None)

        self.logger.info(f"The audio under URL: '{self.url}' was downloaded to: '{download_path}'")
