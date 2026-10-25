"""Генерирует оформление профиля: карточки проектов, разделители и подвал (SVG), рамки для скриншотов.
Запуск: python3 scripts/make_assets.py. Зависимость только у рамок: Pillow."""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
RED, TEXT, DIM, FAINT, PANEL, LINE = "#b3000f", "#e8e8e8", "#8a8a8a", "#707070", "#0b0b0b", "#2a2a2a"

PROJECTS = [
    ("citadel", "шлюз безопасности MCP-агентов", "политики, taint tracking, бенчмарк атак", "typescript · mcp", "50 тестов"),
    ("basilisk", "аудит MCP и инструментов LLM", "инъекции, скрытые символы, подмена", "typescript · sarif", "58 тестов"),
    ("ghoul", "SSH-ловушка с живым дашбордом", "пароли, команды и реверс-шеллы ботов", "python · asyncssh", "22 теста"),
    ("shroud", "детектор стеганографии", "хвост файла, метаданные, LSB, RS-анализ", "python · numpy", "24 теста"),
    ("silhouette", "монитор поверхности атаки", "поддомены, висячие CNAME, оценка A–F", "python · dnspython", "45 тестов"),
    ("wyrm", "coverage-guided фаззер", "persistent-режим, воркеры, дедупликация", "c++ · asan", "39 тестов"),
]

STYLE = """<style>
    text { font-family: 'Courier New', Menlo, Consolas, monospace; }
    .jit { animation: jit 4.2s infinite steps(1); }
    .blink { animation: blink 1.1s infinite steps(1); }
    @keyframes jit { 0%,93%,100%{transform:translate(0,0)} 94%{transform:translate(-3px,1px)} 96%{transform:translate(2px,0)} 98%{transform:translate(-1px,0)} }
    @keyframes blink { 0%,49%{opacity:1} 50%,100%{opacity:0} }
  </style>"""


def card(name: str, title: str, line: str, tags: str, tests: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 128" width="400" height="128" role="img" aria-label="{escape(name)}: {escape(title)}">
  <title>{escape(name)}: {escape(title)}</title>
  <defs>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.04"/></pattern>
    {STYLE}
  </defs>
  <rect x="0.5" y="0.5" width="399" height="127" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="128" fill="{RED}"/>
  <g class="jit"><text x="24" y="40" font-size="22" font-weight="700" fill="{TEXT}" letter-spacing="3">{escape(name.upper())}</text></g>
  <text x="24" y="64" font-size="13" fill="{TEXT}">{escape(title)}</text>
  <text x="24" y="84" font-size="11.5" fill="{DIM}">{escape(line)}</text>
  <text x="24" y="110" font-size="11" fill="{FAINT}">{escape(tags)}</text>
  <text x="376" y="110" font-size="11" fill="{DIM}" text-anchor="end">{escape(tests)}</text>
  <text x="376" y="40" font-size="14" fill="{RED}" text-anchor="end">&gt;<tspan class="blink">_</tspan></text>
  <rect width="400" height="128" fill="url(#scan)"/>
</svg>
"""


def divider() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 22" width="830" height="22" role="presentation" aria-hidden="true">
  <defs>
    <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{RED}" stop-opacity="0"/><stop offset="0.5" stop-color="{RED}"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient>
    <style>
      text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}
      .a {{ animation: f 3.1s infinite steps(1); }} .b {{ animation: f 2.3s infinite steps(1) 0.7s; }}
      @keyframes f {{ 0%,86%,100%{{opacity:1}} 90%{{opacity:.15}} 94%{{opacity:.7}} }}
    </style>
  </defs>
  <rect x="0" y="10.5" width="830" height="1" fill="url(#g)"/>
  <g class="a"><text x="388" y="15" font-size="12" fill="{RED}">▓</text></g>
  <g class="b"><text x="402" y="15" font-size="12" fill="{DIM}">▒</text></g>
  <text x="416" y="15" font-size="12" fill="{FAINT}">░</text>
</svg>
"""


def footer() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="1200" height="140" role="img" aria-label="exit 0">
  <title>exit 0</title>
  <defs>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.045"/></pattern>
    <radialGradient id="vig" cx="50%" cy="50%" r="75%"><stop offset="55%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="0.9"/></radialGradient>
    <style>
      text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}
      .blink {{ animation: blink 1.1s infinite steps(1); }} .jit {{ animation: jit 3.6s infinite steps(1); }}
      @keyframes blink {{ 0%,49%{{opacity:1}} 50%,100%{{opacity:0}} }}
      @keyframes jit {{ 0%,92%,100%{{transform:translate(0,0)}} 93%{{transform:translate(-5px,1px)}} 95%{{transform:translate(4px,0)}} 97%{{transform:translate(-2px,0)}} }}
    </style>
  </defs>
  <rect width="1200" height="140" fill="#050505"/>
  <rect x="1" y="1" width="1198" height="138" fill="none" stroke="#3a3a3a" stroke-width="2"/>
  <text x="40" y="34" font-size="12" fill="#d9d9d9" opacity="0.6">0x4748554C ░▒▓█ exit 0</text>
  <g class="jit"><text x="600" y="76" text-anchor="middle" font-size="30" font-weight="700" fill="{TEXT}" letter-spacing="10">MISXNTHROPY</text></g>
  <text x="600" y="106" text-anchor="middle" font-size="15" fill="{DIM}" letter-spacing="6">DEFENSE · DETECTION · AI AGENT SECURITY</text>
  <text x="1160" y="122" text-anchor="end" font-size="16" fill="{RED}">&gt; <tspan class="blink">█</tspan></text>
  <rect width="1200" height="140" fill="url(#scan)"/>
  <rect width="1200" height="140" fill="url(#vig)"/>
</svg>
"""


def frame_images() -> None:
    """Тонкая серая рамка 2 px: на чёрном фоне едва заметна, а на белом странице светлой темы не даёт картинке «висеть коробкой»."""
    from PIL import Image
    for name in ("ghoul", "shroud", "silhouette", "wyrm", "basilisk", "citadel"):
        path = ASSETS / f"{name}.png"
        if not path.exists():
            continue
        src = ASSETS / "src" / f"{name}.png"
        src.parent.mkdir(exist_ok=True)
        if not src.exists():
            src.write_bytes(path.read_bytes())  # оригинал без рамки хранится рядом, чтобы повторный запуск не рисовал рамку поверх рамки
        im = Image.open(src).convert("RGB")
        out = Image.new("RGB", (im.width + 4, im.height + 4), (58, 58, 58))
        out.paste(im, (2, 2))
        out.save(path, optimize=True)


def gh_json(*args: str):
    import json, subprocess
    out = subprocess.run(["gh", *args], capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 and out.stdout.strip() else None


def stats_svg() -> str:
    """Собственная карточка статистики: числа берутся из GitHub API и из таблицы PROJECTS, внешних сервисов нет."""
    names = [p[0] for p in PROJECTS]
    langs: dict[str, int] = {}
    commits = 0
    for n in names:
        for lang, size in (gh_json("api", f"repos/rephuren/{n}/languages") or {}).items():
            langs[lang] = langs.get(lang, 0) + size
        data = gh_json("api", "graphql", "-f", f'query={{repository(owner:"rephuren",name:"{n}"){{defaultBranchRef{{target{{... on Commit{{history{{totalCount}}}}}}}}}}}}')
        try:
            commits += data["data"]["repository"]["defaultBranchRef"]["target"]["history"]["totalCount"]
        except (TypeError, KeyError):
            pass
    tests = sum(int(p[4].split()[0]) for p in PROJECTS)
    shown = [(k, v) for k, v in sorted(langs.items(), key=lambda kv: -kv[1]) if k not in ("Makefile", "CMake", "Shell", "Dockerfile")][:5]
    total = sum(v for _, v in shown) or 1
    shown = [(k, v) for k, v in shown if v / total >= 0.01]  # мелочь меньше процента на карточке только шумит
    total = sum(v for _, v in shown) or 1
    colors = [RED, TEXT, DIM, "#555555", "#2e2e2e"]
    bar, legend, x = [], [], 24.0
    for i, (lang, size) in enumerate(shown):
        w = 782.0 * size / total
        bar.append(f'<rect x="{x:.1f}" y="150" width="{max(w - 2, 1):.1f}" height="8" fill="{colors[i]}"/>')
        x += w
        legend.append(f'<rect x="{24 + i * 156}" y="178" width="9" height="9" fill="{colors[i]}"/><text x="{40 + i * 156}" y="187" font-size="12" fill="{TEXT}">{escape(lang)}</text><text x="{40 + i * 156}" y="203" font-size="11" fill="{DIM}">{100 * size / total:.0f}%</text>')
    numbers = [(str(len(names)), "проектов"), (str(tests), "тестов"), (str(len(names)), "релизов"), (str(commits), "коммитов")]
    cells = "".join(
        f'<g class="n"><text x="{24 + i * 200}" y="88" font-size="46" font-weight="700" fill="{RED if i == 1 else TEXT}">{escape(v)}</text>'
        f'<text x="{24 + i * 200}" y="112" font-size="12" fill="{DIM}" letter-spacing="2">{escape(label.upper())}</text></g>'
        for i, (v, label) in enumerate(numbers)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 224" width="830" height="224" role="img" aria-label="статистика: {len(names)} проектов, {tests} тестов, {commits} коммитов">
  <title>статистика профиля</title>
  <defs><pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.04"/></pattern>{STYLE}</defs>
  <rect x="0.5" y="0.5" width="829" height="223" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="224" fill="{RED}"/>
  <text x="24" y="36" font-size="13" fill="{DIM}" letter-spacing="3">СТАТИСТИКА</text>
  <text x="806" y="36" font-size="14" fill="{RED}" text-anchor="end">&gt;<tspan class="blink">_</tspan></text>
  {cells}
  <text x="24" y="140" font-size="11" fill="{FAINT}" letter-spacing="2">ЯЗЫКИ ПО ДАННЫМ GITHUB</text>
  {"".join(bar)}
  {"".join(legend)}
  <rect width="830" height="224" fill="url(#scan)"/>
</svg>
"""


def main() -> None:
    cards = ASSETS / "cards"
    cards.mkdir(exist_ok=True)
    for name, title, line, tags, tests in PROJECTS:
        (cards / f"{name}.svg").write_text(card(name, title, line, tags, tests), encoding="utf-8")
    (ASSETS / "divider.svg").write_text(divider(), encoding="utf-8")
    (ASSETS / "footer.svg").write_text(footer(), encoding="utf-8")
    (ASSETS / "stats.svg").write_text(stats_svg(), encoding="utf-8")
    try:
        frame_images()
    except ImportError:
        print("Pillow не установлен: рамки для скриншотов пропущены")
    print("готово")


if __name__ == "__main__":
    main()
