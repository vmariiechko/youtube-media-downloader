import pytube

from youtube.base import YouTubeBase


class YouTubePlaylist(YouTubeBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        try:
            self._playlist = pytube.Playlist(self.url)
        except pytube.exceptions.PytubeError as e:
            self.logger.error(f"Failed to initialize YT playlist:\n{e}")

        self.download_dir = self.download_dir / self._playlist.title
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def download_audio(self) -> None:
        for video in self._playlist.videos:
            try:
                audio_stream = video.streams.filter(only_audio=True).first()
            except pytube.exceptions.RecordingUnavailable:
                self.logger.error(
                    f"Attention! The recording from '{video.title}' "
                    "is not available, skipping download..."
                )

            audio_stream.download(str(self.download_dir))
            self.logger.info(f"The video '{video.title}' has been downloaded")

        self.logger.info("Converting all videos to audio format...")
        for mp4_path in self.download_dir.glob("*.mp4"):
            mp3_path = mp4_path.with_suffix(".mp3")
            if mp3_path.exists():
                mp3_path.unlink()
            mp4_path.rename(mp3_path)

        self.logger.info(
            f"All audios from playlist under URL: '{self.url}' "
            f"were downloaded to: '{self.download_dir}'.\nHappy listening :)"
        )
