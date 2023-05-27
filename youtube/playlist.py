import logging
from pathlib import Path

import pytube


class YouTubePlaylist:

    def __init__(self, url: str, logger: logging.Logger) -> None:
        self.logger = logger
        self.url = url

        try:
            self._playlist = pytube.Playlist(url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(
                f"Failed to initialize YT playlist:\n"
                f"{e}"
            )

    def download_audio(self, output_path: str = '') -> None:
        playlist_download_dir = Path(output_path).absolute() / self._playlist.title
        playlist_download_dir.mkdir(parents=True)

        try:
            for video in self._playlist.videos:
                audio_stream = video.streams.filter(only_audio=True).first()
                audio_stream.download(str(playlist_download_dir))
                self.logger.info(f"The audio from '{video.title}' has been downloaded")
        except pytube.exceptions.PytubeError as e:
            self.logger.error(
                f"An error occurred while downloading the audio:\n"
                f"{e}"
            )

        self.logger.info(
            f"All audios from playlist under URL: '{self.url}' "
            f"were downloaded to: '{playlist_download_dir}'"
        )
