import sys

from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from qt_material import apply_stylesheet

from youtube_media_downloader.gui.config import STATIC_PATH
from youtube_media_downloader.gui.main_ui import MainWindowUI
from youtube_media_downloader.gui.workers import DownloadWorker
from youtube_media_downloader.utils.logger import setup_logger

logger = setup_logger()


class MainWindow(MainWindowUI):
    def __init__(self):
        super().__init__()
        self.browse_output_button.clicked.connect(self.browse_output_path)
        self.download_button.clicked.connect(self.start_download)
        self.worker = None

    def browse_output_path(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_path_label.setText(directory)

    def _disable_ui(self, disable):
        """Helper method to disable/enable UI elements"""

        self.url_input.setEnabled(not disable)
        self.download_button.setEnabled(not disable)
        self.browse_output_button.setEnabled(not disable)
        self.playlist_input_radio.setEnabled(not disable)
        self.video_input_radio.setEnabled(not disable)
        self.audio_output_radio.setEnabled(not disable)
        # self.video_output_radio.setEnabled(not disable)
        self.separate_channel_checkbox.setEnabled(
            not disable and self.playlist_input_radio.isChecked()
        )

    def on_download_finished(self, success, message):
        self.stop_loading_spinner()
        self._disable_ui(False)
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)

    def start_download(self):
        url = self.url_input.text()
        output_directory = self.output_path_label.text()

        if not url:
            QMessageBox.warning(self, "Warning", "Please enter a YouTube URL.")
            return

        self.worker = DownloadWorker(
            url,
            self.video_input_radio.isChecked(),
            self.audio_output_radio.isChecked(),
            output_directory,
            self.separate_channel_checkbox.isChecked(),
        )
        self.worker.finished_signal.connect(self.on_download_finished)

        self._disable_ui(True)
        self.start_loading_spinner()
        self.worker.start()


if __name__ == "__main__":
    logger.info("Starting GUI...")
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme=str(STATIC_PATH / "gui_theme.xml"), invert_secondary=True)
    window.show()
    sys.exit(app.exec())
