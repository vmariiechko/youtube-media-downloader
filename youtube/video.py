
import logging

import pytube


class YouTubeVideo:

    def __init__(self, url: str, logger: logging.Logger) -> None:
        self.logger = logger
        self.url = url

        try:
            self.video = pytube.YouTube(url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(
                f"Failed to initialize YT video:\n"
                f"{e}"
            )

    def download_audio(self, output_path: str = '') -> None:
        try:
            audio_stream = self.video.streams.filter(only_audio=True).first()
            download_path = audio_stream.download(output_path)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(
                f"An error occurred while downloading the audio:\n"
                f"{e}"
            )

        self.logger.info(f"The audio under URL: '{self.url}' was downloaded to: '{download_path}'")
