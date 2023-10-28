from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QMovie
from PySide6.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from .config import ICONS_PATH, STATIC_PATH


class MainWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Media Downloader")
        self.setWindowIcon(QIcon(str(ICONS_PATH / "app_icon.png")))
        self.resize(700, 300)

        self.central_widget = QWidget(self)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Loading Spinner Setup
        self.loading_movie = QMovie(str(STATIC_PATH / "loading_spinner.gif"))
        self.loading_movie.setScaledSize(QSize(30, 30))
        self.loading_label = QLabel(self, visible=False)
        self.loading_label.setMovie(self.loading_movie)

        # Create a URL input and Download button
        self.url_layout = QHBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter YouTube URL here")
        self.url_layout.addWidget(self.url_input)

        self.download_button = QPushButton("Download", self)
        self.url_layout.addWidget(self.download_button)

        self.url_layout.addWidget(self.loading_label)
        self.main_layout.addLayout(self.url_layout)

        # Create Output Path controls
        self.output_path_layout = QHBoxLayout()

        self.output_path_label = QLabel("Choose output directory...", self)
        self.output_path_label.setStyleSheet("border: 1px solid gray; padding: 2px;")
        self.output_path_layout.addWidget(self.output_path_label, stretch=4)

        self.browse_output_button = QPushButton("Browse", self)
        self.output_path_layout.addWidget(self.browse_output_button)

        self.main_layout.addLayout(self.output_path_layout)

        # Video and Playlist Radio buttons for input YT URL
        self.link_type_group = QGroupBox("Link Type")
        self.link_type_layout = QVBoxLayout(self.link_type_group)

        self.radio_button_layout = QHBoxLayout()
        self.playlist_input_radio = QRadioButton("Playlist", self, checked=True)
        self.video_input_radio = QRadioButton("Video", self)
        self.radio_button_layout.addWidget(self.playlist_input_radio)
        self.radio_button_layout.addWidget(self.video_input_radio)

        self.link_type_layout.addLayout(self.radio_button_layout)

        self.separate_channel_checkbox = QCheckBox(
            "Separate by Channels", self, enabled=self.playlist_input_radio.isChecked()
        )
        self.link_type_layout.addWidget(self.separate_channel_checkbox)

        self.main_layout.addWidget(self.link_type_group)

        # Connect signals
        self.playlist_input_radio.toggled.connect(self.toggle_separate_channel_checkbox)

        # Audio and Video Radio buttons for output format
        self.output_format_group = QGroupBox("Output Format")
        self.output_format_layout = QHBoxLayout(self.output_format_group)

        self.audio_output_radio = QRadioButton("Audio", self)
        self.video_output_radio = QRadioButton("Video", self, enabled=False)
        self.output_format_layout.addWidget(self.audio_output_radio)
        self.output_format_layout.addWidget(self.video_output_radio)
        self.audio_output_radio.setChecked(True)

        self.main_layout.addWidget(self.output_format_group)

        self.setCentralWidget(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def toggle_separate_channel_checkbox(self, checked):
        """Enable or Disable the separate_channel_checkbox based on Playlist radio button state."""
        self.separate_channel_checkbox.setEnabled(checked)

    def start_loading_spinner(self):
        """Start the loading spinner animation."""
        self.loading_label.show()
        self.loading_movie.start()

    def stop_loading_spinner(self):
        """Stop the loading spinner animation and hide the label."""
        self.loading_movie.stop()
        self.loading_label.hide()
