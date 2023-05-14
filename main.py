import argparse

from logger import setup_logger
from youtube.video import YouTubeVideo

if __name__ == "__main__":
    logger = setup_logger()
    parser = argparse.ArgumentParser(
        description='YouTube playlist downloader'
    )

    parser.add_argument('-u', '--url', help='YouTube video URL to download')
    args = parser.parse_args()
    YouTubeVideo(args.url, logger).download_audio()
