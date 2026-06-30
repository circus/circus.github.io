#!/usr/bin/env python3
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1376, 768
OUT = Path("wadt.svg")

# Layout approximated from the reference image
GAP = 13
TILE_W = 218
TILE_H = 218

TOP_Y = 45
MID_Y = 276
BOT_Y = 508

xs = [0, 231, 464, 693, 927, 1158]

top_colors = [
    "#fff544",  # yellow
    "#5dad55",  # green
    "#3e7fba",  # blue
    "#de6aa0",  # pink
    "#db3731",  # red
    "#fff544",  # yellow
]

bottom_colors = [
    "#3e7fba",  # blue
    "#de6aa0",  # pink
    "#8f3b98",  # purple
    "#fff544",  # yellow
    "#c9dd3c",  # lime
    "#3e7fba",  # blue
]

middle_blocks = [
    (0, MID_Y, TILE_W, TILE_H, "#d5327d"),       # magenta left
    (1158, MID_Y, TILE_W, TILE_H, "#5ab1d8"),    # cyan right
]

letters = [
    ("·", 111, 384),
    ("w", 337, 384),
    ("a", 594, 384),
    ("d", 810, 384),
    ("t", 1038, 384),
    ("·", 1268, 384),
]

def rect(x, y, w, h, fill):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
        f'fill="{fill}" filter="url(#softShadow)"/>'
    )

def text(label, x, y):
    return (
        f'<text x="{x}" y="{y}" '
        f'font-family="Arial, Helvetica, sans-serif" '
        f'font-size="104" font-weight="700" '
        f'text-anchor="middle" dominant-baseline="middle" '
        f'fill="#000000" filter="url(#tinyBlur)">'
        f'{escape(label)}</text>'
    )

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<defs>",
    """
    <filter id="softShadow" x="-4%" y="-4%" width="108%" height="108%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.2"
                    flood-color="#000000" flood-opacity="0.28"/>
    </filter>
    """,
    """
    <filter id="tinyBlur">
      <feGaussianBlur stdDeviation="0.35"/>
    </filter>
    """,
    "</defs>",
    '<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>',
]

# Top row
for x, c in zip(xs, top_colors):
    svg_parts.append(rect(x, TOP_Y, TILE_W, TILE_H, c))

# Middle row side blocks
for block in middle_blocks:
    svg_parts.append(rect(*block))

# Bottom row
for x, c in zip(xs, bottom_colors):
    svg_parts.append(rect(x, BOT_Y, TILE_W, TILE_H, c))

# Text and dots
for label, x, y in letters:
    svg_parts.append(text(label, x, y))

svg_parts.append("</svg>")

OUT.write_text("\n".join(svg_parts), encoding="utf-8")
print(f"Wrote {OUT.resolve()}")