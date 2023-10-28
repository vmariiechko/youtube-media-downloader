import argparse

from pytube.exceptions import PytubeError

from youtube_media_downloader.utils.logger import setup_logger
from youtube_media_downloader.youtube.playlist import YouTubePlaylist
from youtube_media_downloader.youtube.video import YouTubeVideo

logger = setup_logger()

if __name__ == "__main__":
    logger.info("Starting CLI...")
    parser = argparse.ArgumentParser(description="YouTube playlist downloader")

    subparsers = parser.add_subparsers(dest="type", required=True, title="commands")

    video_parser = subparsers.add_parser("video", help="Download a YouTube video")
    video_parser.add_argument("-u", "--url", required=True, help="YouTube video URL to download")

    playlist_parser = subparsers.add_parser("playlist", help="Download a YouTube playlist")
    playlist_parser.add_argument(
        "-u", "--url", required=True, help="YouTube playlist URL to download"
    )
    playlist_parser.add_argument(
        "-scf",
        "--separate_channel_folders",
        action="store_true",
        help="Separate downloaded content to channel folders",
    )

    args = parser.parse_args()

    try:
        if args.type == "video":
            YouTubeVideo(args.url, logger, output_path="downloads").download_audio()
        elif args.type == "playlist":
            YouTubePlaylist(
                args.url,
                logger,
                output_path="downloads",
                separate_channel_folders=args.separate_channel_folders,
            ).download_audios()
    except PytubeError as e:
        logger.error(f"An error occurred while downloading the audio:\n{e.format_exc()}")
