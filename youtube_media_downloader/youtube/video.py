from pathlib import Path

import pytube

from youtube_media_downloader.youtube.base import YouTubeBase


class YouTubeVideo(YouTubeBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._initialize_video()

    def _initialize_video(self) -> None:
        try:
            self.video = pytube.YouTube(self.url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(f"Failed to initialize YT video:\n{e}")
            raise

    def _get_audio_stream(self) -> pytube.StreamQuery:
        try:
            return self.video.streams.filter(only_audio=True).first()
        except pytube.exceptions.RecordingUnavailable:
            self.logger.error(
                f"Attention! The recording from URL '{self.url}' "
                "is not available, please check it and try again."
            )

    def download_audio(self) -> None:
        audio_stream = self._get_audio_stream()

        if not audio_stream:
            return

        download_path = Path(audio_stream.download(str(self.download_dir)))
        self.convert_to_mp3(download_path)
        self.logger.info(f"The audio under URL: '{self.url}' was downloaded to: '{download_path}'")
