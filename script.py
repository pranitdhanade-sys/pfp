#!/usr/bin/env python3
"""
Download images from a Pinterest board using gallery-dl.

Use only for images you own or have permission to download/use.
Pinterest may require authentication or restrict automated access. This script
does not bypass logins, CAPTCHAs, or access controls.
"""
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_BOARD = "https://in.pinterest.com/pranitdhanade/pfp/_tools/more-ideas/?ideas_referrer=23"
DESTINATION = Path("pfps")


def main():
    board_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BOARD

    if not board_url.startswith(("https://", "http://")):
        print("Please provide a valid http(s) Pinterest board URL.")
        raise SystemExit(2)

    if shutil.which("gallery-dl") is None:
        print("gallery-dl is not installed.")
        print("Install it with: python -m pip install -U gallery-dl")
        raise SystemExit(1)

    DESTINATION.mkdir(parents=True, exist_ok=True)
    command = [
        "gallery-dl",
        "--dest", str(DESTINATION),
        board_url,
    ]

    print(f"Downloading available images into: {DESTINATION.resolve()}")
    print("Pinterest may block access or require an authorized login.")
    try:
        result = subprocess.run(command, check=False)
    except KeyboardInterrupt:
        print("\nStopped by user.")
        raise SystemExit(130)

    if result.returncode == 0:
        print("\nFinished. Check the pfps/ folder, then commit/upload those files to your GitHub repository.")
    else:
        print(
            "\nDownload did not complete. The board may be private, Pinterest may "
            "require authentication, or gallery-dl may need an updated version/configuration."
        )
        print("Do not share your Pinterest password. Do not try to bypass access restrictions.")
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
