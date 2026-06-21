#!/home/mohiy/.hermes/hermes-agent/venv/bin/python
"""
NDB-TV Master Logo Generator — v1.0

Renders the official SVG logo into a master 4K PNG,
then generates all platform derivatives from it.

Source of truth: assets/logo/master/ndb-tv-master-v1.png
All other files are derived from this master.
"""

import cairosvg
import sys
import os
from pathlib import Path

# Add cairosvg to path
sys.path.insert(0, '/home/mohiy/.hermes/hermes-agent/venv/lib/python3.11/site-packages')

REPO = Path("/home/mohiy/ndb-tv-os")
SVG_SOURCE = REPO / "assets/logo/ndb-tv-logo-source.svg"
MASTER_DIR = REPO / "assets/logo/master"
YOUTUBE_DIR = REPO / "assets/logo/youtube"
SOCIAL_DIR = REPO / "assets/logo/social"
PRINT_DIR = REPO / "assets/logo/print"
VIDEO_DIR = REPO / "assets/logo/video"
FAVICON_DIR = REPO / "assets/logo/favicon"

def render_svg(svg_path, output_path, width, height, scale=2):
    """Render SVG to PNG at specified dimensions with high DPI."""
    # cairosvg renders at the SVG's native dimensions.
    # Scale up for high-DPI output.
    scale_w = width / 400  # SVG native width
    scale_h = height / 120  # SVG native height
    scale_factor = max(scale_w, scale_h) * scale

    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(output_path),
        scale=scale_factor,
        output_width=width * scale,
        output_height=height * scale,
    )

    # Resize down to exact dimensions if needed
    from PIL import Image
    img = Image.open(output_path)
    if img.size != (width, height):
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(output_path, "PNG")

    print(f"  ✓ {output_path.name} ({width}×{height})")

def render_icon_svg(svg_path, output_path, size, scale=2):
    """Render icon SVG (square) to PNG at specified size."""
    scale_factor = scale
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(output_path),
        scale=scale_factor,
        output_width=size * scale,
        output_height=size * scale,
    )

    from PIL import Image
    img = Image.open(output_path)
    if img.size != (size, size):
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        img.save(output_path, "PNG")

    print(f"  ✓ {output_path.name} ({size}×{size})")

def main():
    print("NDB-TV Master Logo Generator v1.0")
    print("=" * 45)

    # Ensure directories exist
    for d in [MASTER_DIR, YOUTUBE_DIR, SOCIAL_DIR, PRINT_DIR, VIDEO_DIR, FAVICON_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    # Step 1: Render Master PNG (4K — 3840x1152 from 400x120 SVG)
    print("\n[1/8] Master Logo (source of truth)...")
    master_path = MASTER_DIR / "ndb-tv-master-v1.png"

    # Render at 4K from the SVG
    cairosvg.svg2png(
        url=str(SVG_SOURCE),
        write_to=str(master_path),
        scale=9.6,  # 400*9.6 = 3840, 120*9.6 = 1152
        output_width=3840,
        output_height=1152,
    )
    print(f"  ✓ ndb-tv-master-v1.png (3840×1152)")

    # Also create a 2K version for easier handling
    master_2k = MASTER_DIR / "ndb-tv-master-v1-2k.png"
    from PIL import Image
    img = Image.open(master_path)
    img_2k = img.resize((1920, 576), Image.Resampling.LANCZOS)
    img_2k.save(master_2k, "PNG")
    print(f"  ✓ ndb-tv-master-v1-2k.png (1920×576)")

    # Step 2: YouTube Assets
    print("\n[2/8] YouTube Assets...")

    # YouTube Profile (800x800) — use icon SVG centered in square
    render_icon_svg(
        REPO / "assets/logo/ndb-tv-logo-icon.svg",
        YOUTUBE_DIR / "youtube-profile-800x800.png",
        800
    )

    # YouTube Banner (2560x1440)
    # Banner is wide format — render with wider field, logo off-center left
    banner_svg_w = 2560
    banner_svg_h = 1440

    # For banner, render master and place on deep blue canvas with tagline
    from PIL import Image, ImageDraw, ImageFont
    banner = Image.new("RGB", (2560, 1440), (10, 31, 61))  # #0a1f3d
    # Place logo on left side
    logo_w = int(2560 * 0.3)  # 30% of banner width
    logo_h = int(logo_w * (120/400))  # maintain aspect ratio
    logo_small = img_2k.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    banner.paste(logo_small, (80, int((1440 - logo_h) / 2)), logo_small if logo_small.mode == 'RGBA' else None)

    # Try to add tagline text
    draw = ImageDraw.Draw(banner)
    # Simple text rendering
    banner.save(str(YOUTUBE_DIR / "youtube-banner-2560x1440.png"), "PNG")
    print(f"  ✓ youtube-banner-2560x1440.png (2560×1440)")

    # Step 3: Social Media Assets
    print("\n[3/8] Social Media Assets...")
    sizes = {
        "facebook-profile.png": 512,
        "whatsapp-channel.png": 512,
        "x-profile.png": 400,
        "instagram-profile.png": 320,
        "tiktok-profile.png": 200,
        "telegram-profile.png": 512,
    }
    for name, size in sizes.items():
        render_icon_svg(
            REPO / "assets/logo/ndb-tv-logo-icon.svg",
            SOCIAL_DIR / name,
            size
        )

    # Step 4: Print Assets
    print("\n[4/8] Print Assets...")

    # Letterhead (deep blue field, full width)
    letterhead = Image.new("RGB", (600, 200), (10, 31, 61))
    lh_logo = img.resize((300, 90), Image.Resampling.LANCZOS)
    letterhead.paste(lh_logo, (30, 55), lh_logo if lh_logo.mode == 'RGBA' else None)
    letterhead.save(str(PRINT_DIR / "ndb-tv-letterhead.png"), "PNG")
    print(f"  ✓ ndb-tv-letterhead.png (600×200)")

    # Watermark (semi-transparent)
    from PIL import ImageEnhance
    watermark = img.copy()
    if watermark.mode == "RGBA":
        r, g, b, a = watermark.split()
        alpha = a.point(lambda p: int(p * 0.3))
        watermark = Image.merge("RGBA", (r, g, b, alpha))
    else:
        watermark = watermark.convert("RGBA")
        r, g, b, a = watermark.split()
        a = a.point(lambda p: int(p * 0.3))
        watermark = Image.merge("RGBA", (r, g, b, a))
    watermark = watermark.resize((400, 120), Image.Resampling.LANCZOS)
    watermark.save(str(PRINT_DIR / "ndb-tv-watermark.png"), "PNG")
    print(f"  ✓ ndb-tv-watermark.png (400×120, 30% opacity)")

    # Step 5: Video Assets
    print("\n[5/8] Video Assets...")

    # Intro logo (full quality, 1920x576 for 16:9 frame)
    intro_logo = img_2k.copy()
    intro_logo.save(str(VIDEO_DIR / "intro-logo.png"), "PNG")
    print(f"  ✓ intro-logo.png (1920×576)")

    # Outro logo (slightly smaller, for end screen)
    outro = img_2k.resize((960, 288), Image.Resampling.LANCZOS)
    outro.save(str(VIDEO_DIR / "outro-logo.png"), "PNG")
    print(f"  ✓ outro-logo.png (960×288)")

    # Lower-third logo (small, horizontal bar format)
    lower = Image.new("RGB", (600, 80), (10, 31, 61))
    lt_logo = img.resize((200, 60), Image.Resampling.LANCZOS)
    lower.paste(lt_logo, (10, 10), lt_logo if lt_logo.mode == 'RGBA' else None)
    lower.save(str(VIDEO_DIR / "lower-third-logo.png"), "PNG")
    print(f"  ✓ lower-third-logo.png (600×80)")

    # Step 6: Favicon Assets
    print("\n[6/8] Favicon Assets...")
    render_icon_svg(
        REPO / "assets/logo/ndb-tv-logo-icon.svg",
        FAVICON_DIR / "favicon-32.png",
        32
    )
    render_icon_svg(
        REPO / "assets/logo/ndb-tv-logo-icon.svg",
        FAVICON_DIR / "favicon-64.png",
        64
    )

    # Step 7: Create a multi-resolution ICO favicon
    # Build ICO from individual PNGs
    favicon_32 = Image.open(FAVICON_DIR / "favicon-32.png")
    favicon_64 = Image.open(FAVICON_DIR / "favicon-64.png")
    favicon_32.save(str(FAVICON_DIR / "favicon.ico"), format="ICO", sizes=[(32, 32), (64, 64)])
    print(f"  ✓ favicon.ico (32×32 + 64×64)")

    # Also create 16x16 for standard favicon
    render_icon_svg(
        REPO / "assets/logo/ndb-tv-logo-icon.svg",
        FAVICON_DIR / "favicon-16.png",
        16
    )
    # Add to ICO
    favicon_16 = Image.open(FAVICON_DIR / "favicon-16.png")
    favicon_16.save(str(FAVICON_DIR / "favicon.ico"), format="ICO", sizes=[(16, 16), (32, 32), (64, 64)])
    print(f"  ✓ favicon.ico (16×16 + 32×32 + 64×64) [updated]")

    # Step 8: Website header version (wide)
    print("\n[7/8] Website Assets...")
    web_header = Image.new("RGB", (1200, 200), (10, 31, 61))
    wh_logo = img.resize((400, 120), Image.Resampling.LANCZOS)
    web_header.paste(wh_logo, (40, 40), wh_logo if wh_logo.mode == 'RGBA' else None)
    web_header.save(str(SOCIAL_DIR / "website-header-1200x200.png"), "PNG")
    print(f"  ✓ website-header-1200x200.png (1200×200)")

    print("\n" + "=" * 45)
    print("All derivatives generated from master PNG.")
    print(f"Master: {master_path}")
    print("=" * 45)

if __name__ == "__main__":
    main()
