"""
python main.py -pu "https://www.youtube.com/playlist?list=PLhvGGyZjDqHrmlkJESdvuJkdNvTJnDQ8N"
"""

import argparse

from pytube.exceptions import PytubeError

from logger import setup_logger
from youtube.playlist import YouTubePlaylist
from youtube.video import YouTubeVideo

if __name__ == "__main__":
    logger = setup_logger()
    parser = argparse.ArgumentParser(description="YouTube playlist downloader")

    parser.add_argument("-vu", "--video_url", help="YouTube video URL to download")
    parser.add_argument("-pu", "--playlist_url", help="YouTube playlist URL to download")
    args = parser.parse_args()

    if args.video_url:
        try:
            YouTubeVideo(
                args.video_url, logger, output_path="downloads", quick_download=True
            ).download_audio()
        except PytubeError as e:
            logger.error(f"An error occurred while downloading the audio:\n{e.format_exc()}")

    if args.playlist_url:
        try:
            YouTubePlaylist(
                args.playlist_url, logger, output_path="downloads", quick_download=True
            ).download_audio()
        except PytubeError as e:
            logger.error(f"An error occurred while downloading the audio:\n{e.format_exc()}")
