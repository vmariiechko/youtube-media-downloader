import logging
from pathlib import Path


class YouTubeBase:
    def __init__(
        self,
        url: str,
        logger: logging.Logger,
        output_path: str = "",
        separate_channel_folders: bool = False,
    ) -> None:
        self.url = url
        self.logger = logger

        self.download_dir = Path(output_path).absolute()
        self.download_dir.mkdir(parents=True, exist_ok=True)

        self.separate_channel_folders = separate_channel_folders

    def convert_to_mp3(self, video_path: Path) -> None:
        """Convert video to mp3 format.

        It assumes that the video was downloaded with only_audio=True option,
        so it's enough to rename the video file to an audio file with .mp3 extension
        """

        mp3_path = video_path.with_suffix(".mp3")
        if mp3_path.exists():
            mp3_path.unlink()
        video_path.rename(mp3_path)
