"""纸盒图标压缩：512² 母图 → favicon 32/180 尺寸。

源(E:\\mygarden\\static)：favicon.png(开盖) / favicon-closed.png(合盖)
输出(E:\\blog\\blog\\static)：
  favicon-open-32.png / favicon-closed-32.png   ← 浏览器标签页, 切主题时换
  apple-touch-icon.png                          ← iOS 主屏(开盖, 已存在则覆盖为压缩版)

跑法: python scripts/make-box-icons.py
"""
from pathlib import Path
from PIL import Image

SRC = Path(r"E:\mygarden\static")
OUT = Path(__file__).resolve().parent.parent / "static"


def shrink(src: Path, dest: Path, size: int) -> int:
    img = Image.open(src).convert("RGBA")
    img = img.resize((size, size), Image.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    img.save(dest, "PNG", optimize=True)
    return dest.stat().st_size


if __name__ == "__main__":
    jobs = [
        (SRC / "favicon.png",        OUT / "favicon-open-32.png",   32),
        (SRC / "favicon-closed.png", OUT / "favicon-closed-32.png", 32),
        (SRC / "favicon.png",        OUT / "apple-touch-icon.png",  180),
    ]
    for src, dest, size in jobs:
        assert src.exists(), f"缺素材: {src}"
        n = shrink(src, dest, size)
        assert n > 0, f"{dest.name} 写出来是空的"
        print(f"{dest.name}: {size}x{size}, {n} bytes")

    # 自检：开盖/合盖两张 favicon 必须都真的存在且非空（切主题靠它俩）
    for f in ("favicon-open-32.png", "favicon-closed-32.png"):
        p = OUT / f
        assert p.exists() and p.stat().st_size > 0, f"缺少 {f}"
    print("OK: 开盖/合盖 favicon 齐备")
