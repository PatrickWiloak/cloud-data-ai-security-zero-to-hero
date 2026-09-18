#!/usr/bin/env python3
"""Render the social preview card at assets/brand/social-preview-1280x640.png.

GitHub serves an auto-generated card for a repo with no social preview set, so
every share on X, LinkedIn or Slack rendered as a grey placeholder. This draws
the project's own card in the site's design language: pure black, the gitGood
green accent, and real Geist - the same typeface the site loads.

Deliberately carries **no counts**. An image with "148 certs" baked into it is a
number nothing can check, which is exactly the failure that left the repository
description reading "122+ certs across 22 providers" for months. The card states
what the project is; the page it links to states how big it is.

    pip install pillow
    python3 .github/scripts/build-social-card.py

Geist is fetched from Google Fonts at run time (as TTF - Pillow cannot read the
woff2 the modern CSS endpoint serves) and cached in .cache/fonts/, which is
gitignored. Committing the 1280x640 PNG is the point; this script exists so the
card can be regenerated rather than being an unexplained binary in the tree.

The output doubles as the site's Open Graph image, referenced by
.github/site-overrides/main.html. Upload it to GitHub's own social preview by
hand at Settings > General > Social preview - the REST API does not expose that
field, so it cannot be automated.
"""

from __future__ import annotations

import re
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "assets" / "brand" / "social-preview-1280x640.png"
FONT_CACHE = REPO / ".cache" / "fonts"

W, H = 1280, 640
PAD = 84

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 197, 94)          # #22c55e, the site's accent
GREY = (161, 161, 170)         # zinc-400, the site's secondary text
DIM = (113, 113, 122)          # zinc-500
FAINT = (82, 82, 91)           # zinc-600
HAIRLINE = (39, 39, 42)        # zinc-800, the card border colour

FONT_CSS = (
    "https://fonts.googleapis.com/css2"
    "?family=Geist:wght@300;400;600;700&family=Geist+Mono:wght@400;600"
)


def fonts() -> dict[str, Path]:
    """Download Geist and Geist Mono as TTF, cached.

    The modern Google Fonts CSS endpoint serves woff2, which Pillow cannot read.
    Asking with an ancient User-Agent gets the TTF fallbacks instead.
    """
    FONT_CACHE.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(FONT_CSS, headers={"User-Agent": "Mozilla/4.0"})
    css = urllib.request.urlopen(request).read().decode("utf-8")

    found: dict[str, Path] = {}
    for block in css.split("@font-face")[1:]:
        family = re.search(r"font-family:\s*'([^']+)'", block)
        weight = re.search(r"font-weight:\s*(\d+)", block)
        url = re.search(r"url\((https://[^)]+\.ttf)\)", block)
        if not (family and weight and url):
            continue
        key = f"{family.group(1).replace(' ', '')}-{weight.group(1)}"
        path = FONT_CACHE / f"{key}.ttf"
        if not path.exists():
            urllib.request.urlretrieve(url.group(1), path)
        found[key] = path
    return found


def glow(image: Image.Image) -> None:
    """The accent glow the site's hero carries, in the top-right corner.

    A filled disc blurred hard, rather than Pillow's radial_gradient: that
    gradient only reaches white at the midpoint of each edge, so its corners
    stay partly opaque and the tint renders as a visible rectangle over the
    page. Blurring a disc inside a larger canvas lets the alpha actually reach
    zero before the edge, which is what makes it read as a glow.
    """
    size = 1100
    disc = 250
    centre = size // 2

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse(
        (centre - disc, centre - disc, centre + disc, centre + disc), fill=255
    )
    mask = mask.filter(ImageFilter.GaussianBlur(190))
    mask = mask.point(lambda v: int(v * 0.30))

    tint = Image.new("RGBA", (size, size), (*GREEN, 0))
    tint.putalpha(mask)
    image.alpha_composite(tint, dest=(W - centre - 60, -centre + 30))


def pill(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font) -> int:
    """A bordered capsule, matching the provider chips on the landing page.

    Height comes from the font's own metrics, not from the rendered text's bbox:
    measuring each label made "Certify" taller than "Learn" because of the
    descender, so a row of chips came out ragged.
    """
    pad_x, height = 22, 44
    width = int(draw.textlength(text, font=font)) + pad_x * 2
    draw.rounded_rectangle(
        (x, y, x + width, y + height), radius=height // 2, outline=HAIRLINE, width=1
    )
    draw.text((x + pad_x, y + height / 2 - 1), text, font=font, fill=(228, 228, 231), anchor="lm")
    return x + width + 14


def main() -> int:
    f = fonts()
    mono_600 = ImageFont.truetype(str(f["GeistMono-600"]), 21)
    mono_400 = ImageFont.truetype(str(f["GeistMono-400"]), 19)
    title = ImageFont.truetype(str(f["Geist-700"]), 84)
    sub = ImageFont.truetype(str(f["Geist-300"]), 31)
    chip = ImageFont.truetype(str(f["Geist-600"]), 20)

    image = Image.new("RGBA", (W, H), (*BLACK, 255))
    glow(image)
    draw = ImageDraw.Draw(image)

    y = 96

    # Kicker. Letter-spacing has to be drawn by hand; Pillow has no tracking.
    x = PAD
    for char in "FREE & OPEN SOURCE":
        draw.text((x, y), char, font=mono_600, fill=GREEN)
        x += draw.textlength(char, font=mono_600) + 4.2

    y += 58
    draw.text((PAD, y), "Cloud, Data, AI", font=title, fill=WHITE)
    y += 88
    amp_w = draw.textlength("& ", font=title)
    draw.text((PAD, y), "&", font=title, fill=GREEN)
    draw.text((PAD + amp_w, y), "Security", font=title, fill=WHITE)

    y += 118
    draw.text((PAD, y), "From absolute zero to hired.", font=sub, fill=GREY)

    y += 66
    draw.rounded_rectangle((PAD, y, PAD + 112, y + 4), radius=2, fill=GREEN)

    y += 34
    x = PAD
    for label in ("Learn", "Certify", "Build", "Reference"):
        x = pill(draw, x, y, label, chip)

    draw.text((PAD, H - 62), "patrickwiloak.github.io/cloud-data-ai-security-zero-to-hero",
              font=mono_400, fill=DIM)
    draw.text((W - PAD, H - 62), "Nobler Works", font=mono_400, fill=FAINT, anchor="ra")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT.relative_to(REPO)} ({OUT.stat().st_size // 1024} KB, {W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
