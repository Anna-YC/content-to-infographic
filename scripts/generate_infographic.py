#!/usr/bin/env python3
"""
Generate an infographic by calling the local image-generation command.

Usage:
  python3 generate_infographic.py "prompt text" [output_path]

The command, credentials, and service details stay in the user's local
environment. This skill only passes prompt, ratio, quality, and output path to
the local command.
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def env_flag(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def resolve_image_command() -> str:
    configured = os.environ.get("INFOGRAPHIC_IMAGE_COMMAND") or os.environ.get("GPT_IMAGE_BIN")
    if configured:
        return configured

    home_bin = Path.home() / "bin" / "gpt-image"
    if home_bin.exists():
        return str(home_bin)

    return "gpt-image"


def default_output_path() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"infographic_{timestamp}.png"


def generate_image(prompt: str, output_path: str | None = None) -> str:
    image_command = resolve_image_command()
    ratio = os.environ.get("INFOGRAPHIC_ASPECT_RATIO", "9:16")
    fast_mode = env_flag("INFOGRAPHIC_FAST_MODE")
    quality = os.environ.get("GPT_IMAGE_QUALITY", "low" if fast_mode else "medium")
    compress_jpg = env_flag("INFOGRAPHIC_COMPRESS_JPG", True)

    if not output_path:
        output_path = default_output_path()

    print("Generating infographic...")
    print(f"   Command: {image_command}")
    print(f"   Ratio: {ratio}")
    print(f"   Quality: {quality}")
    print(f"   Prompt length: {len(prompt)} chars")

    try:
        subprocess.run(
            [image_command, prompt, ratio, quality, output_path],
            check=True,
            timeout=int(os.environ.get("GPT_IMAGE_CURL_MAX_TIME", "900")),
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            "Local image-generation command was not found. "
            "Set INFOGRAPHIC_IMAGE_COMMAND or GPT_IMAGE_BIN to the command path."
        ) from exc

    if not Path(output_path).exists():
        raise RuntimeError(f"Image command completed but output file was not found: {output_path}")

    print(f"Image saved to: {output_path}")

    if compress_jpg:
        jpg_path = compress_to_jpg(output_path)
        if jpg_path:
            return jpg_path

    return output_path


def compress_to_jpg(image_path: str) -> str | None:
    source = Path(image_path)
    if source.suffix.lower() in {".jpg", ".jpeg"}:
        return str(source)

    jpg_path = str(source.with_suffix(".jpg"))

    try:
        command = [
            "sips",
            "-s",
            "format",
            "jpeg",
            "-s",
            "formatOptions",
            "82",
        ]

        target_width = int(os.environ.get("INFOGRAPHIC_JPG_MAX_WIDTH", "1024"))
        source_width = get_image_width(str(source))
        if source_width and source_width > target_width:
            command.extend(["--resampleWidth", str(target_width)])

        command.extend([str(source), "--out", jpg_path])

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.returncode != 0 or not Path(jpg_path).exists():
            print(f"Compression failed: {result.stderr}")
            return None

        source.unlink(missing_ok=True)
        size_kb = Path(jpg_path).stat().st_size / 1024
        print(f"Compressed to JPG: {jpg_path}")
        print(f"   File size: {size_kb:.1f} KB")
        return jpg_path
    except Exception as exc:
        print(f"Compression error: {exc}")
        return None


def get_image_width(image_path: str) -> int:
    try:
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", image_path],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return 0
        for line in result.stdout.splitlines():
            if "pixelWidth:" in line:
                return int(line.split(":", 1)[1].strip())
    except Exception:
        return 0
    return 0


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 generate_infographic.py 'prompt text' [output_path]")
        print("\nOptional environment variables:")
        print("  INFOGRAPHIC_IMAGE_COMMAND  - local image-generation command path")
        print("  GPT_IMAGE_BIN              - alternate command path")
        print("  INFOGRAPHIC_ASPECT_RATIO   - 1:1, 4:3, 3:4, 16:9, or 9:16")
        print("  GPT_IMAGE_QUALITY          - low, medium, high, or auto")
        print("  INFOGRAPHIC_FAST_MODE=1    - lower-latency defaults")
        print("  INFOGRAPHIC_COMPRESS_JPG=0 - skip JPG compression")
        sys.exit(1)

    prompt = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result_path = generate_image(prompt, output_path)
        print(f"\nDone! Image saved to: {result_path}")
    except Exception as exc:
        print(f"\nFailed to generate image: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
