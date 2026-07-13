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
import platform
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

# ── Platform detection ──────────────────────────────────────────────────
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"


def env_flag(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def resolve_image_command() -> str:
    configured = os.environ.get("INFOGRAPHIC_IMAGE_COMMAND") or os.environ.get("GPT_IMAGE_BIN")
    if configured:
        return configured

    # macOS / Linux: ~/bin/gpt-image
    if not IS_WINDOWS:
        home_bin = Path.home() / "bin" / "gpt-image"
        if home_bin.exists():
            return str(home_bin)
        return "gpt-image"

    # Windows: %USERPROFILE%\bin\gpt-image.exe / gpt-image.cmd / gpt-image.bat
    win_bin = Path.home() / "bin"
    for ext in ("", ".exe", ".cmd", ".bat"):
        candidate = win_bin / f"gpt-image{ext}"
        if candidate.exists():
            return str(candidate)

    # Also check %USERPROFILE%\AppData\Local\gpt-image
    local_bin = Path.home() / "AppData" / "Local" / "gpt-image" / "gpt-image.exe"
    if local_bin.exists():
        return str(local_bin)

    return "gpt-image"


def check_command_available(cmd: str) -> tuple[bool, str]:
    """Check if the image-generation command is available and executable."""
    resolved = shutil.which(cmd)

    if not resolved:
        # macOS / Linux: try with PATH including ~/bin
        if not IS_WINDOWS:
            home_bin = str(Path.home() / "bin")
            env = {**os.environ, "PATH": f"{home_bin}:{os.environ.get('PATH', '')}"}
            resolved = shutil.which(cmd, path=env.get("PATH"))
        else:
            # Windows: try %USERPROFILE%\bin and AppData\Local
            home_bin = str(Path.home() / "bin")
            local_bin = str(Path.home() / "AppData" / "Local" / "gpt-image")
            extra_path = f"{home_bin};{local_bin};{os.environ.get('PATH', '')}"
            resolved = shutil.which(cmd, path=extra_path)

        if not resolved:
            platform_hint = (
                "On Windows: install gpt-image or set INFOGRAPHIC_IMAGE_COMMAND / GPT_IMAGE_BIN"
                if IS_WINDOWS else
                "Install gpt-image or set INFOGRAPHIC_IMAGE_COMMAND / GPT_IMAGE_BIN"
            )
            return False, f"Command '{cmd}' not found. {platform_hint}."

    # Verify the resolved path is executable (stat-based, no subprocess call)
    if os.access(resolved, os.X_OK):
        return True, f"Found '{resolved}'"
    else:
        return False, f"Found '{resolved}' but it is not executable"


def default_output_path() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"infographic_{timestamp}.png"


def generate_image(prompt: str, output_path: str | None = None) -> str:
    import time
    start_time = time.time()

    image_command = resolve_image_command()
    ratio = os.environ.get("INFOGRAPHIC_ASPECT_RATIO", "9:16")
    # Default to "low" for speed; only upgrade when explicitly requested
    quality = os.environ.get("GPT_IMAGE_QUALITY", "low")
    compress_jpg = env_flag("INFOGRAPHIC_COMPRESS_JPG", True)

    if not output_path:
        output_path = default_output_path()

    print("Generating infographic...")
    print(f"   Platform: {platform.system()} {platform.release()}")
    print(f"   Command: {image_command}")
    print(f"   Ratio: {ratio}")
    print(f"   Quality: {quality}")
    print(f"   Prompt length: {len(prompt)} chars")

    # Pre-flight check: verify command is available
    ok, msg = check_command_available(image_command)
    if not ok:
        raise RuntimeError(
            f"Image-generation command is not available.\n\n"
            f"  {msg}\n\n"
            f"To fix:\n"
            f"  1. Install the gpt-image CLI\n"
            f"  2. Or set environment variable:\n"
            f"       {'set' if IS_WINDOWS else 'export'} INFOGRAPHIC_IMAGE_COMMAND=path/to/gpt-image\n"
            f"       {'set' if IS_WINDOWS else 'export'} GPT_IMAGE_BIN=path/to/gpt-image"
        )
    print(f"   \u2713 {msg}")

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
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            f"Image generation timed out after {exc.timeout} seconds.\n"
            "Try: reducing prompt length, or set GPT_IMAGE_CURL_MAX_TIME to a higher value."
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"Image command failed with exit code {exc.returncode}.\n"
            f"Stdout: {exc.stdout or '(empty)'}\n"
            f"Stderr: {exc.stderr or '(empty)'}"
        ) from exc

    if not Path(output_path).exists():
        raise RuntimeError(f"Image command completed but output file was not found: {output_path}")

    elapsed = time.time() - start_time
    print(f"Image saved to: {output_path}  (generation: {elapsed:.1f}s)")

    if compress_jpg:
        jpg_path = compress_to_jpg(output_path)
        if jpg_path:
            return jpg_path

    return output_path


def compress_to_jpg(image_path: str) -> str | None:
    """Compress PNG to JPG using Pillow (cross-platform) with platform fallbacks."""
    source = Path(image_path)
    if source.suffix.lower() in {".jpg", ".jpeg"}:
        return str(source)

    jpg_path = str(source.with_suffix(".jpg"))

    # Primary: use Pillow (cross-platform, works on macOS / Linux / Windows)
    if HAS_PILLOW:
        try:
            img = Image.open(str(source))
            # Convert RGBA to RGB (white background) if needed
            if img.mode in ("RGBA", "LA", "P"):
                bg = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                img = bg
            elif img.mode != "RGB":
                img = img.convert("RGB")

            target_width = int(os.environ.get("INFOGRAPHIC_JPG_MAX_WIDTH", "1024"))
            if img.width > target_width:
                ratio = target_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((target_width, new_height), Image.LANCZOS)

            img.save(jpg_path, "JPEG", quality=82, optimize=True)
            source.unlink(missing_ok=True)
            size_kb = Path(jpg_path).stat().st_size / 1024
            print(f"Compressed to JPG (Pillow): {jpg_path}")
            print(f"   File size: {size_kb:.1f} KB")
            return jpg_path
        except Exception as exc:
            print(f"Pillow compression failed: {exc}")

    # ── Platform-specific fallbacks (only if Pillow is unavailable or failed) ──

    if IS_MACOS:
        return _compress_jpg_macos(str(source), jpg_path)
    elif IS_WINDOWS:
        return _compress_jpg_windows(str(source), jpg_path)
    else:
        return _compress_jpg_linux(str(source), jpg_path)


def _compress_jpg_macos(source_path: str, jpg_path: str) -> str | None:
    """macOS: use sips (system built-in)."""
    try:
        command = [
            "sips", "-s", "format", "jpeg",
            "-s", "formatOptions", "82",
        ]
        target_width = int(os.environ.get("INFOGRAPHIC_JPG_MAX_WIDTH", "1024"))
        source_width = _get_image_width_sips(source_path)
        if source_width and source_width > target_width:
            command.extend(["--resampleWidth", str(target_width)])
        command.extend([source_path, "--out", jpg_path])

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.returncode != 0 or not Path(jpg_path).exists():
            print(f"sips compression failed: {result.stderr}")
            return None

        Path(source_path).unlink(missing_ok=True)
        size_kb = Path(jpg_path).stat().st_size / 1024
        print(f"Compressed to JPG (sips): {jpg_path} ({size_kb:.1f} KB)")
        return jpg_path
    except Exception as exc:
        print(f"sips compression error: {exc}")
        return None


def _compress_jpg_windows(source_path: str, jpg_path: str) -> str | None:
    """Windows: use PowerShell + System.Drawing (built-in)."""
    try:
        ps_command = (
            f'Add-Type -AssemblyName System.Drawing; '
            f'$img = [System.Drawing.Image]::FromFile("{source_path}"); '
            f'$bmp = New-Object System.Drawing.Bitmap $img; '
            f'$bmp.Save("{jpg_path}", [System.Drawing.Imaging.ImageFormat]::Jpeg); '
            f'$img.Dispose(); $bmp.Dispose()'
        )
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_command],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0 and Path(jpg_path).exists():
            Path(source_path).unlink(missing_ok=True)
            size_kb = Path(jpg_path).stat().st_size / 1024
            print(f"Compressed to JPG (PowerShell): {jpg_path} ({size_kb:.1f} KB)")
            return jpg_path
        print(f"PowerShell compression failed: {result.stderr}")
        return None
    except Exception as exc:
        print(f"PowerShell compression error: {exc}")
        return None


def _compress_jpg_linux(source_path: str, jpg_path: str) -> str | None:
    """Linux: try ImageMagick convert (may need manual install)."""
    try:
        result = subprocess.run(
            ["convert", source_path, "-quality", "82", jpg_path],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0 and Path(jpg_path).exists():
            Path(source_path).unlink(missing_ok=True)
            size_kb = Path(jpg_path).stat().st_size / 1024
            print(f"Compressed to JPG (ImageMagick): {jpg_path} ({size_kb:.1f} KB)")
            return jpg_path
        print(f"ImageMagick convert failed: {result.stderr}")
        return None
    except Exception as exc:
        print(f"ImageMagick error: {exc}")
        return None


def _get_image_width_sips(image_path: str) -> int:
    """Get image width using sips (macOS-only)."""
    try:
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", image_path],
            capture_output=True, text=True, timeout=10,
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
