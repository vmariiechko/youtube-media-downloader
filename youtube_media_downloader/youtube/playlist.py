from pathlib import Path

import pytube

from .base import YouTubeBase


class YouTubePlaylist(YouTubeBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        try:
            self._playlist = pytube.Playlist(self.url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(f"Failed to initialize YT playlist:\n{e}")
            raise

        self.download_dir = self.download_dir / self._playlist.title
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def _get_download_directory_for_video(self, video: pytube.YouTube) -> Path:
        if self.separate_channel_folders:
            current_download_dir = self.download_dir / video.author
            current_download_dir.mkdir(exist_ok=True)
            return current_download_dir

        return self.download_dir

    def _download_single_video(self, video: pytube.YouTube) -> None:
        try:
            audio_stream = video.streams.filter(only_audio=True).first()
        except pytube.exceptions.RecordingUnavailable:
            self.logger.error(
                f"Attention! The recording from '{video.title}' "
                "is not available, skipping download..."
            )
            return

        current_download_dir = self._get_download_directory_for_video(video)
        audio_stream.download(str(current_download_dir))
        self.logger.info(f"The video '{video.title}' has been downloaded")

    def download_videos(self):
        for video in self._playlist.videos:
            self._download_single_video(video)

    def convert_to_mp3(self):
        self.logger.info("Converting all videos to audio format...")
        for mp4_path in self.download_dir.rglob("*.mp4"):
            super().convert_to_mp3(mp4_path)

    def download_audios(self) -> None:
        self.download_videos()
        self.convert_to_mp3()
        self.logger.info(
            f"All audios from playlist under URL: '{self.url}' "
            f"were downloaded to: '{self.download_dir}'.\nHappy listening :)"
        )
