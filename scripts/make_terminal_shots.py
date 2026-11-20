"""Рисует «скриншоты» терминала из текстов в scripts/shots/*.txt (реальный вывод команд на демо-данных, снят вручную) в assets/src/.
Запуск: python3 scripts/make_terminal_shots.py, затем scripts/make_assets.py ставит рамку. Нужен Pillow."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
BG, TEXT, DIM, RED = (5, 5, 5), (232, 232, 232), (138, 138, 138), (212, 32, 47)
FONT = "/System/Library/Fonts/Menlo.ttc"
SIZE, PAD, COLS = 30, 44, 100


def colour(line: str):
    if line.startswith("$ "):
        return None
    low = line.strip().lower()
    if low.startswith(("fail", "[high", "[medium", "[medium", "[low")) or " fail " in line[:18]:
        return RED
    if low.startswith(("ok", "...")) or line.startswith("  ") and "entropy" in line:
        return DIM
    return TEXT


def render(name: str) -> None:
    lines = (ROOT / "scripts" / "shots" / f"{name}.txt").read_text(encoding="utf-8").splitlines()
    lines = [ln if len(ln) <= COLS else ln[: COLS - 1] + "…" for ln in lines]
    reg, bold = ImageFont.truetype(FONT, SIZE, index=0), ImageFont.truetype(FONT, SIZE, index=1)
    cw = reg.getlength("M")
    lh = int(SIZE * 1.45)
    w, h = int(PAD * 2 + cw * COLS), PAD * 2 + lh * len(lines)
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    for i, ln in enumerate(lines):
        y = PAD + i * lh
        if ln.startswith("$ "):
            d.text((PAD, y), "$", font=bold, fill=RED)
            d.text((PAD + cw * 2, y), ln[2:], font=bold, fill=TEXT)
        else:
            c = colour(ln)
            d.text((PAD, y), ln, font=reg, fill=c or TEXT)
    out = ROOT / "assets" / "src"
    out.mkdir(exist_ok=True)
    im.resize((w // 2 + w // 4, h // 2 + h // 4), Image.LANCZOS).save(out / f"{name}.png", optimize=True)


if __name__ == "__main__":
    for n in ("exorcist", "gargoyle", "banshee", "chimera", "necropsy"):
        render(n)
    print("готово")
