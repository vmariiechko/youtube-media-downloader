from PySide6.QtCore import QThread, Signal
from pytube.exceptions import PytubeError

from ..utils.logger import setup_logger
from ..youtube.playlist import YouTubePlaylist
from ..youtube.video import YouTubeVideo

logger = setup_logger()


class DownloadWorker(QThread):
    finished_signal = Signal(bool, str)

    def __init__(self, url, is_video_url_type, is_audio_output, output_path, separate_channels):
        super().__init__()
        self.url = url
        self.is_video_url_type = is_video_url_type
        self.is_audio_output = is_audio_output
        self.output_path = output_path
        self.separate_channels = separate_channels

    def run(self):
        try:
            if self.is_video_url_type:
                if self.is_audio_output:
                    YouTubeVideo(self.url, logger, output_path=self.output_path).download_audio()
                # TODO handle video download when the feature added
            else:
                if self.is_audio_output:
                    YouTubePlaylist(
                        self.url,
                        logger,
                        output_path=self.output_path,
                        separate_channel_folders=self.separate_channels,
                    ).download_audios()
                # TODO handle playlist video download when the feature added
            self.finished_signal.emit(True, "Download completed successfully!")
        except PytubeError:
            msg = "An error occurred while downloading. Please check the URL and try again."
            self.finished_signal.emit(False, msg)
        except Exception as e:
            self.finished_signal.emit(False, str(e))
