from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


PRESETS = {
    "voice_clear_light": ",".join(
        [
            "highpass=f=70",
            "lowpass=f=12500",
            "equalizer=f=220:t=q:w=1.1:g=-2",
            "equalizer=f=3200:t=q:w=1.0:g=2.5",
            "acompressor=threshold=0.12:ratio=2.2:attack=15:release=180:makeup=1.5",
            "alimiter=limit=0.95",
            "loudnorm=I=-16:LRA=8:TP=-1.5",
        ]
    ),
    "voice_clear_soft": ",".join(
        [
            "highpass=f=60",
            "lowpass=f=13000",
            "equalizer=f=250:t=q:w=1.0:g=-1.5",
            "equalizer=f=2800:t=q:w=1.0:g=1.8",
            "acompressor=threshold=0.14:ratio=2.0:attack=20:release=200:makeup=1.2",
            "alimiter=limit=0.95",
            "loudnorm=I=-16:LRA=9:TP=-1.5",
        ]
    ),
}


def build_output_path(input_path: Path, suffix: str) -> Path:
    return input_path.with_name(f"{input_path.stem}_{suffix}{input_path.suffix}")


def run_ffmpeg(input_path: Path, output_path: Path, filter_chain: str) -> None:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg not found in PATH")

    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(input_path),
        "-af",
        filter_chain,
        str(output_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffmpeg failed")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply a light clarity enhancement chain to narration audio using ffmpeg."
    )
    parser.add_argument("--input", required=True, help="Input WAV/MP3 path")
    parser.add_argument(
        "--output",
        help="Output path. Defaults to <input>_enhanced.wav or same extension suffix.",
    )
    parser.add_argument(
        "--preset",
        default="voice_clear_light",
        choices=sorted(PRESETS.keys()),
        help="Enhancement preset",
    )
    parser.add_argument(
        "--print-filter",
        action="store_true",
        help="Print the ffmpeg filter chain before running",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"input not found: {input_path}", file=sys.stderr)
        return 1

    output_path = Path(args.output) if args.output else build_output_path(input_path, "enhanced")
    filter_chain = PRESETS[args.preset]

    if args.print_filter:
        print(filter_chain)

    try:
        run_ffmpeg(input_path, output_path, filter_chain)
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
