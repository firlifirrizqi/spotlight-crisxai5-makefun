#!/usr/bin/env python3
"""Draw the Spotlight @crisxai5 card (1080x1080) from scratch with PIL.

Original flat art for the make.fun bounty "Spotlight @crisxai5: AI & Crypto
Expert on X". Nothing is downloaded or copied in: every shape, bar and
letter is drawn here by code. Run: python3 draw_spotlight.py
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080

NAVY = (11, 18, 38)
NAVY2 = (15, 29, 61)
CYAN = (34, 211, 238)
TEAL = (45, 212, 191)
GREEN = (74, 222, 128)
YELLOW = (250, 204, 21)
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)
CARD = (23, 37, 84)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def text_center(draw, cx, y, text, fnt, fill):
    """Draw text centred on cx at height y; return its width."""
    box = draw.textbbox((0, 0), text, font=fnt)
    w = box[2] - box[0]
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return w


def pill(draw, cx, y, w, h, text, fnt, bg, fg):
    """A centred rounded pill with centred text."""
    x0, x1 = cx - w / 2, cx + w / 2
    draw.rounded_rectangle([x0, y, x1, y + h], radius=h // 2, fill=bg)
    box = draw.textbbox((0, 0), text, font=fnt)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text((cx - tw / 2, y + (h - th) / 2 - box[1]), text, font=fnt, fill=fg)


def chip(draw, x, y, w, h, text, fnt, outline, fg):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2,
                           outline=outline, width=4)
    box = draw.textbbox((0, 0), text, font=fnt)
    tw, th = box[2] - box[0], box[3] - box[1]
    draw.text((x + (w - tw) / 2, y + (h - th) / 2 - box[1]),
              text, font=fnt, fill=fg)


def background(draw):
    """Vertical navy gradient plus faint circuit dots in the corners."""
    for y in range(H):
        t = y / H
        r = int(NAVY[0] + (NAVY2[0] - NAVY[0]) * t)
        g = int(NAVY[1] + (NAVY2[1] - NAVY[1]) * t)
        b = int(NAVY[2] + (NAVY2[2] - NAVY[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    dot = (56, 189, 248)
    for (x, y) in [(70, 90), (1010, 80), (60, 990), (1010, 990),
                   (140, 160), (950, 170)]:
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], outline=dot, width=2)
    draw.line([(70, 90), (140, 160)], fill=dot, width=2)
    draw.line([(1010, 80), (950, 170)], fill=dot, width=2)


def chart(draw, x0, y_base, heights, colors):
    """A rising candlestick-style bar chart: the market going up."""
    bw, gap = 64, 26
    for i, h in enumerate(heights):
        x = x0 + i * (bw + gap)
        c = colors[i % len(colors)]
        draw.rounded_rectangle([x, y_base - h, x + bw, y_base],
                               radius=10, fill=c)
        # wick above each bar
        draw.line([(x + bw // 2, y_base - h - 26),
                   (x + bw // 2, y_base - h)], fill=c, width=5)
    # trend arrow above the bars
    draw.line([(x0 - 10, y_base - heights[0] - 60),
               (x0 + 4 * (bw + gap), y_base - heights[-1] - 60)],
              fill=YELLOW, width=8)
    ax, ay = x0 + 4 * (bw + gap), y_base - heights[-1] - 60
    draw.polygon([(ax, ay - 26), (ax + 34, ay), (ax, ay + 12)], fill=YELLOW)


def robot(draw, cx, cy):
    """A friendly flat robot head: rounded face, glowing cyan visor eyes,
    antenna with a signal dot. The AI half of the AI x crypto story."""
    # antenna
    draw.line([(cx, cy - 118), (cx, cy - 168)], fill=CYAN, width=10)
    draw.ellipse([cx - 16, cy - 192, cx + 16, cy - 160], fill=YELLOW)
    # head
    draw.rounded_rectangle([cx - 150, cy - 118, cx + 150, cy + 118],
                           radius=56, fill=CARD, outline=CYAN, width=6)
    # visor eyes
    draw.rounded_rectangle([cx - 108, cy - 48, cx - 18, cy + 6],
                           radius=16, fill=CYAN)
    draw.rounded_rectangle([cx + 18, cy - 48, cx + 108, cy + 6],
                           radius=16, fill=CYAN)
    # smile
    draw.arc([cx - 52, cy + 18, cx + 52, cy + 92], start=15, end=165,
             fill=TEAL, width=9)
    # side ears
    draw.rectangle([cx - 172, cy - 40, cx - 150, cy + 40], fill=TEAL)
    draw.rectangle([cx + 150, cy - 40, cx + 172, cy + 40], fill=TEAL)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)
    background(draw)

    # Top tag: what this card is.
    pill(draw, W // 2, 52, 470, 64, "MUST-FOLLOW ON X",
         font(34), CYAN, NAVY)

    # Headline: the hook.
    text_center(draw, W // 2, 140, "AI x CRYPTO", font(110), WHITE)
    text_center(draw, W // 2, 258, "ONE ACCOUNT. ZERO NOISE.",
                font(40), YELLOW)

    # Middle: robot (AI) on the left, rising chart (crypto) on the right.
    robot(draw, 330, 540)
    chart(draw, 560, 640, [90, 140, 110, 190, 250],
          [TEAL, CYAN, TEAL, GREEN, GREEN])
    text_center(draw, 790, 668, "SIGNAL, NOT NOISE", font(30), MUTED)

    # The account itself, big and unmissable.
    text_center(draw, W // 2, 800, "@crisxai5", font(96), CYAN)

    # What followers get: three chips.
    labels = ["AI AGENTS", "CRYPTO ALPHA", "WEB3 TOOLING"]
    widths = [250, 300, 310]
    total = sum(widths) + 2 * 24
    x = (W - total) // 2
    for label, w in zip(labels, widths):
        chip(draw, x, 920, w, 62, label, font(30), CYAN, WHITE)
        x += w + 24

    text_center(draw, W // 2, 1010, "Follow the signal  ·  x.com/crisxai5",
                font(30, bold=False), MUTED)

    img.save("spotlight.png")
    print("wrote spotlight.png", img.size)


if __name__ == "__main__":
    main()
