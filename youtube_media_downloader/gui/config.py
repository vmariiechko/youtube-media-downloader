import sys
from pathlib import Path

# Check if running as a packaged executable
if getattr(sys, "frozen", False):
    # If packaged, use the PyInstaller-created temporary folder
    SRC_ROOT = Path(sys._MEIPASS)
else:
    # Otherwise, use the current script's directory
    SRC_ROOT = Path(__file__).parent

STATIC_PATH = SRC_ROOT / "static"
ICONS_PATH = STATIC_PATH / "icons"
