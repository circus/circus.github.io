#!/usr/bin/env python3
from pathlib import Path
from xml.sax.saxutils import escape
import random

W, H = 1376, 768
OUT = Path("wadt.svg")

all_colors = [
    "#3e7fba",  # blue
    "#5ab1d8",  # cyan
    "#5dad55",  # green
    "#8f3b98",  # purple
    "#c9dd3c",  # lime
    "#d5327d",  # magenta
    "#db3731",  # red
    "#de6aa0",  # pink
    "#fff544",  # yellow
]

letters = 'wadt'

def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'

def text(label, x, y):
    return f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="80" font-weight="700" text-anchor="middle" dominant-baseline="middle" fill="#000000">{escape(label)}</text>'

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<rect x="0" y="0" width="100%" height="100%" fill="#ffffff"/>',
]

last = newc = ''
label = ''
cx = 0
for x in range(0,6):
    for y in range(0,6):
        while newc == last:
            newc = random.choice(all_colors)
        last = newc
        if y == 2:
            if x == 0 or x == 5:
                label = text('.', x*100+50, y*100+30)
            else:
                svg_parts.append(text(letters[cx], x*100+50, y*100+50))
                cx += 1
                continue
        svg_parts.append(rect(x*100, y*100, 95, 95, newc))
        if label:
            svg_parts.append(label)
            label = ''

svg_parts.append("</svg>")

OUT.write_text("\n".join(svg_parts), encoding="utf-8")
print(f"Wrote {OUT.resolve()}")
