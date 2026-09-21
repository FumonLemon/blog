"""压缩顶栏纸盒 logo：754x512 / 747x512 源图 → 高 128 的 PNG。

顶栏实际只显示 3rem/4rem(约 48~64px)高，源图尺寸过剩。
输出仍保持宽高比，两图等高(切主题不跳版)。

跑法: python scripts/shrink-logo.py
"""
from pathlib import Path
from PIL import Image

STATIC = Path(__file__).resolve().parent.parent / "static"
TARGET_H = 128


def shrink(name: str) -> tuple[int, int]:
    p = STATIC / name
    img = Image.open(p).convert("RGBA")
    w, h = img.size
    nw = round(w * TARGET_H / h)
    img = img.resize((nw, TARGET_H), Image.LANCZOS)
    img.save(p, "PNG", optimize=True)
    return nw, p.stat().st_size


if __name__ == "__main__":
    for name in ("logo.png", "logo-closed.png"):
        w, size = shrink(name)
        assert size > 0, f"{name} 空了"
        print(f"{name}: {w}x{TARGET_H}, {size} bytes")
    # 自检：两图高度必须一致，否则切主题时顶栏跳版
    hs = {Image.open(STATIC / n).size[1] for n in ("logo.png", "logo-closed.png")}
    assert len(hs) == 1, f"开/合两图高度不一致: {hs}"
    print(f"OK: 开盖/合盖同为 {hs.pop()}px 高，切换不跳版")
