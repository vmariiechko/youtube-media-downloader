"""

To exec CLI, from project root run:
```
python -m youtube_media_downloader.gui.main
```
"""


import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from pytube.exceptions import PytubeError
from qt_material import apply_stylesheet

from ..utils.logger import setup_logger
from ..youtube.playlist import YouTubePlaylist
from ..youtube.video import YouTubeVideo
from .config import STATIC_PATH
from .main_ui import MainWindowUI


class MainWindow(MainWindowUI):
    def __init__(self):
        super().__init__()
        self.logger = setup_logger()

        self.browse_output_button.clicked.connect(self.browse_output_path)
        self.download_button.clicked.connect(self.start_download)
        self.worker = None

    def browse_output_path(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_path_label.setText(directory)

    def start_download(self):
        url = self.url_input.text()
        output_directory = self.output_path_label.text()

        if not url:
            QMessageBox.warning(self, "Warning", "Please enter a YouTube URL.")
            return

        try:
            # Download YouTube video
            if self.video_input_radio.isChecked():
                if self.audio_output_radio.isChecked():
                    YouTubeVideo(url, self.logger, output_path=output_directory).download_audio()
                    QMessageBox.information(self, "Success", "Video audio downloaded successfully!")
                # TODO handle video download when the feature added

            # Download YouTube playlist
            elif self.playlist_input_radio.isChecked():
                separate_channels = self.separate_channel_checkbox.isChecked()

                if self.audio_output_radio.isChecked():
                    YouTubePlaylist(
                        url,
                        self.logger,
                        output_path=output_directory,
                        separate_channel_folders=separate_channels,
                    ).download_audios()
                    QMessageBox.information(
                        self,
                        "Success",
                        "Playlist audios downloaded successfully!\nHappy listening :)",
                    )
                # TODO handle playlist video download when the feature added

        except PytubeError:
            QMessageBox.critical(
                self,
                "Error",
                "An error occurred while downloading. Please check the URL and try again.",
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme=str(STATIC_PATH / "gui_theme.xml"), invert_secondary=True)
    window.show()
    sys.exit(app.exec())
