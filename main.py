import argparse

from logger import setup_logger
from youtube.playlist import YouTubePlaylist
from youtube.video import YouTubeVideo

if __name__ == "__main__":
    logger = setup_logger()
    parser = argparse.ArgumentParser(
        description='YouTube playlist downloader'
    )

    parser.add_argument('-vu', '--video_url', help='YouTube video URL to download')
    parser.add_argument('-pu', '--playlist_url', help='YouTube playlist URL to download')
    args = parser.parse_args()

    if args.video_url:
        YouTubeVideo(args.url, logger).download_audio()

    if args.playlist_url:
        YouTubePlaylist(args.playlist_url, logger).download_audio('downloads')
