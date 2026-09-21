"""生成黑白 favicon PNG（黑底白字 L）。与 static/favicon.svg 同设计。
跑法: python scripts/make-favicon.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def render(size: int) -> Image.Image:
    # 4x 超采样，缩小时边缘才干净
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.1875), fill=(17, 17, 17, 255))

    # 优先用系统衬线体，找不到就退回 PIL 默认位图字体
    font = None
    for name in ("georgia.ttf", "times.ttf", "DejaVuSerif-Bold.ttf", "arialbd.ttf"):
        try:
            font = ImageFont.truetype(name, int(s * 0.625))
            break
        except OSError:
            continue
    if font is None:
        # ponytail: 默认字体是位图、不可缩放，仅作兜底；不会崩
        font = ImageFont.load_default()

    d.text((s / 2, s * 0.70), "L", font=font, fill=(255, 255, 255, 255), anchor="mm")
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "static"
    out.mkdir(parents=True, exist_ok=True)
    for n, fname in ((32, "favicon-32.png"), (180, "apple-touch-icon.png")):
        p = out / fname
        render(n).save(p, "PNG", optimize=True)
        assert p.stat().st_size > 0, f"{fname} 写出来是空的"
        print(f"{fname}: {n}x{n}, {p.stat().st_size} bytes")
