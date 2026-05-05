"""
Renders 1200x630 PNG share cards for blames.
Falls back gracefully if bundled fonts are missing.
"""
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OG_DIR = Path("static/og")
OG_DIR.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("static/fonts")
FONT_BIG_PATH = FONT_DIR / "JetBrainsMono-Bold.ttf"
FONT_SMALL_PATH = FONT_DIR / "JetBrainsMono-Regular.ttf"

BG = (15, 15, 20)
TEXT = (240, 240, 245)
ACCENT = (255, 80, 80)
MUTED = (120, 120, 140)


def _load_font(path: Path, size: int):
    try:
        return ImageFont.truetype(str(path), size)
    except (OSError, IOError):
        # fallback: default font, looks worse but works
        return ImageFont.load_default()


def render_og(blame_id: str, blame_text: str) -> Path:
    out = OG_DIR / f"{blame_id}.png"
    if out.exists():
        return out

    img = Image.new("RGB", (1200, 630), color=BG)
    draw = ImageDraw.Draw(img)

    font_big = _load_font(FONT_BIG_PATH, 44)
    font_small = _load_font(FONT_SMALL_PATH, 24)

    # top tag
    draw.text((80, 80), "// blame report", fill=ACCENT, font=font_small)

    # blame body — wrap to fit
    wrapped = textwrap.fill(blame_text, width=42)
    # cap to 6 lines max so it doesn't overflow
    lines = wrapped.split("\n")[:6]
    if len(wrapped.split("\n")) > 6:
        lines[-1] = lines[-1].rstrip(".") + "…"
    body = "\n".join(lines)
    draw.multiline_text((80, 180), body, fill=TEXT, font=font_big, spacing=8)

    # footer branding
    draw.text((80, 540), "blame-as-a-service", fill=MUTED, font=font_small)
    draw.text((80, 575), "baas.budhathokisagar.com.np", fill=MUTED, font=font_small)

    img.save(out, "PNG", optimize=True)
    return out