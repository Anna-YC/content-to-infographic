#!/usr/bin/env python3
"""
Generate infographic using gpt-image-2 API.
Usage: python3 generate_infographic.py "prompt text" [output_path]

Required environment variables:
  IMAGE_GEN_API_KEY  - API key for image generation service
  IMAGE_GEN_API_URL  - API endpoint for an OpenAI-compatible image generation service
"""

import sys
import json
import urllib.request
import urllib.parse
import base64
import os
import ssl
from pathlib import Path

# API configuration. Override IMAGE_GEN_API_URL when using a proxy or another
# OpenAI-compatible image generation provider.
API_KEY = os.environ.get("IMAGE_GEN_API_KEY", "")
API_BASE = os.environ.get(
    "IMAGE_GEN_API_URL",
    "https://api.openai.com/v1/images/generations"
)
MODEL = "gpt-image-2"
TIMEOUT = 300  # seconds


def check_config():
    """Validate that required environment variables are set."""
    if not API_KEY:
        raise EnvironmentError(
            "IMAGE_GEN_API_KEY is not set. "
            "Please configure your image generation API key in the skill settings."
        )


def generate_image(prompt: str, output_path: str = None) -> str:
    """
    Generate infographic using gpt-image-2 API.
    
    Args:
        prompt: Text prompt for image generation
        output_path: Optional path to save the image (default: ./infographic_<timestamp>.png)
    
    Returns:
        Path to the generated image file
    """
    # Validate configuration
    check_config()
    
    # Prepare request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "n": 1,
        "size": "1024x1792",
        "response_format": "b64_json"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(API_BASE, data=data, headers=headers, method='POST')
    
    print(f"Generating infographic...")
    print(f"   Model: {MODEL}")
    print(f"   Prompt length: {len(prompt)} chars")
    
    try:
        # Disable SSL verification (self-signed cert)
        ctx = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        # Extract base64 image
        if 'data' not in result or not result['data']:
            raise Exception("No image data in API response")
        
        b64_image = result['data'][0].get('b64_json')
        if not b64_image:
            raise Exception("No b64_json in API response")
        
        # Determine output path
        if not output_path:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"infographic_{timestamp}.png"
        
        # Save image
        image_data = base64.b64decode(b64_image)
        with open(output_path, 'wb') as f:
            f.write(image_data)
        
        print(f"Image saved to: {output_path}")
        
        # Compress to JPG for smaller file size
        jpg_path = compress_to_jpg(output_path)
        if jpg_path:
            return jpg_path
        
        return output_path
        
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"HTTP Error {e.code}: {error_body}")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


def compress_to_jpg(png_path: str) -> str:
    """
    Compress PNG to JPG using sips (macOS built-in tool).
    From MEMORY.md: sips -s format jpeg -s formatOptions 70 --resampleWidth 1024
    
    Args:
        png_path: Path to PNG file
    
    Returns:
        Path to compressed JPG file, or None if compression failed
    """
    jpg_path = str(Path(png_path).with_suffix('.jpg'))
    
    try:
        import subprocess
        result = subprocess.run([
            'sips', '-s', 'format', 'jpeg',
            '-s', 'formatOptions', '82',
            '--resampleWidth', '1024',
            png_path,
            '--out', jpg_path
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and os.path.exists(jpg_path):
            # Remove original PNG to save space
            os.remove(png_path)
            print(f"Compressed to JPG: {jpg_path}")
            
            # Get file size
            size_kb = os.path.getsize(jpg_path) / 1024
            print(f"   File size: {size_kb:.1f} KB")
            return jpg_path
        else:
            print(f"Compression failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"Compression error: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_infographic.py 'prompt text' [output_path]")
        print("\nRequired environment variables:")
        print("  IMAGE_GEN_API_KEY  - API key for image generation service")
        print("  IMAGE_GEN_API_URL  - API base URL (optional)")
        print("\nExample:")
        print("  IMAGE_GEN_API_KEY=your-api-key python3 generate_infographic.py 'Create an infographic'")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result_path = generate_image(prompt, output_path)
        print(f"\nDone! Image saved to: {result_path}")
    except Exception as e:
        print(f"\nFailed to generate image: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
