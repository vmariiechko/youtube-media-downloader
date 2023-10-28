import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent
MAIN_SCRIPT_PATH = ROOT_DIR / "youtube_media_downloader" / "gui" / "main.py"
PYINSTALLER_EXEC = ROOT_DIR / "dist"
VERSION_FILE_PATH = ROOT_DIR / "config" / "app_version_info.version"
STATIC_PATH = ROOT_DIR / "youtube_media_downloader" / "gui" / "static"
ICON_PATH = STATIC_PATH / "icons" / "app_icon.ico"

APP_NAME = "YouTube Media Downloader"


def make_windows_executable():
    cmd = [
        "pyinstaller",
        "--name",
        APP_NAME,
        "--windowed",
        "--onefile",
        "--noconfirm",
        f"--add-data={STATIC_PATH};static",
        "--icon",
        str(ICON_PATH),
        "--version-file",
        str(VERSION_FILE_PATH),
        str(MAIN_SCRIPT_PATH),
    ]

    subprocess.run(cmd)


if __name__ == "__main__":
    if sys.platform in ("win32", "cygwin"):
        make_windows_executable()
    else:
        raise RuntimeError("Can't create executable - unsupported OS platform")

    print(f"Success! Check the '{PYINSTALLER_EXEC / APP_NAME}.exe' for executable.")
