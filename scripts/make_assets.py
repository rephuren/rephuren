"""Генерирует оформление профиля: карточки проектов, разделители и подвал (SVG), рамки для скриншотов.
Запуск: python3 scripts/make_assets.py. Зависимость только у рамок: Pillow."""
import re
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
RED, TEXT, DIM, FAINT, PANEL, LINE = "#b3000f", "#e8e8e8", "#8a8a8a", "#707070", "#0b0b0b", "#2a2a2a"

PROJECTS = [
    ("citadel", "шлюз безопасности MCP-агентов", "политики, taint tracking, бенчмарк атак", "typescript · mcp", "50 тестов"),
    ("basilisk", "аудит MCP и инструментов LLM", "инъекции, скрытые символы, подмена", "typescript · sarif", "65 тестов"),
    ("ectoplasm", "разбор сессий ИИ-агентов", "какой текст привёл к какому действию", "python · sarif", "93 теста"),
    ("exorcist", "стенд проверки LLM-приложений", "инъекции, утечки, OWASP LLM и ATLAS", "python · owasp llm · atlas", "16 тестов"),
    ("banshee", "движок правил Sigma и YARA", "журналы и файлы, сводка по ATT&CK", "rust · sigma · yara", "26 тестов"),
    ("gargoyle", "ловушка для веб-приложений", "сканеры, инъекции, приманки с ключами", "ruby · rack · owasp", "24 теста"),
    ("chimera", "пассивный сенсор сети и хоста", "pcap, DNS, TLS, биконинг, SQL", "c · go · sql", "74 проверки"),
    ("necropsy", "вскрытие бинарников ELF и PE", "защита, импорты, энтропия, строки", "go · imhex · pwntools", "21 тест"),
    ("ghoul", "SSH-ловушка с живым дашбордом", "пароли, команды и реверс-шеллы ботов", "python · asyncssh", "29 тестов"),
    ("shroud", "детектор стеганографии", "хвост файла, метаданные, LSB, RS-анализ", "python · numpy", "24 теста"),
    ("silhouette", "монитор поверхности атаки", "поддомены, висячие CNAME, оценка A–F", "python · dnspython", "100 тестов"),
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


WHOAMI = {
    "ru": ("фокус", "инфобез, защита, исследования", "стек", ["python · typescript · c · c++", "bash · linux · osint", "ai security (ниже подробно)"]),
    "en": ("focus", "infosec, defense, research", "stack", ["python · typescript · c · c++", "bash · linux · osint", "ai security (details below)"]),
}


def whoami(lang: str) -> str:
    """Блок «кто я» в стиле карточек вместо серого блока кода GitHub: тот же текст, свой оформление и без кнопки копирования."""
    focus_l, focus_v, stack_l, stack = WHOAMI[lang]
    rows = [
        (30, f'<tspan fill="{RED}">$</tspan> <tspan fill="{TEXT}">whoami</tspan>'),
        (52, f'<tspan fill="{TEXT}" font-weight="700">misxnthropy</tspan>'),
        (96, f'<tspan fill="{RED}">$</tspan> <tspan fill="{TEXT}">cat ~/focus</tspan>'),
    ]
    out = "".join(f'<text x="28" y="{y}" font-size="15">{t}</text>' for y, t in rows)
    out += f'<text x="28" y="120" font-size="15" fill="{DIM}">{escape(focus_l)}</text><text x="120" y="120" font-size="15" fill="{RED}">:</text><text x="140" y="120" font-size="15" fill="{TEXT}">{escape(focus_v)}</text>'
    out += f'<text x="28" y="144" font-size="15" fill="{DIM}">{escape(stack_l)}</text><text x="120" y="144" font-size="15" fill="{RED}">:</text>'
    for i, line in enumerate(stack):
        out += f'<text x="140" y="{144 + i * 24}" font-size="15" fill="{TEXT}">{escape(line)}</text>'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 224" width="830" height="224" role="img" aria-label="whoami: misxnthropy. {escape(focus_l)}: {escape(focus_v)}. {escape(stack_l)}: {escape(', '.join(stack))}">
  <title>whoami</title>
  <defs><pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.04"/></pattern>{STYLE}</defs>
  <rect x="0.5" y="0.5" width="829" height="223" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="224" fill="{RED}"/>
  {out}
  <text x="806" y="30" font-size="14" fill="{RED}" text-anchor="end">&gt;<tspan class="blink">_</tspan></text>
  <rect width="830" height="224" fill="url(#scan)"/>
</svg>
"""


def note(text: str, label: str) -> str:
    """Заметка о состоянии проектов в стиле карточек вместо серой цитаты GitHub. Полный текст лежит и в aria-label."""
    lines = textwrap.wrap(text, 104)
    h = 56 + 20 * len(lines)
    body = "".join(f'<text x="24" y="{54 + 20 * i}" font-size="12.5" fill="{TEXT if i else TEXT}">{escape(l)}</text>' for i, l in enumerate(lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 {h}" width="830" height="{h}" role="img" aria-label="{escape(label)}: {escape(text)}">
  <title>{escape(label)}</title>
  <defs><pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.04"/></pattern>{STYLE}</defs>
  <rect x="0.5" y="0.5" width="829" height="{h - 1}" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="{h}" fill="{RED}"/>
  <text x="24" y="30" font-size="12" fill="{RED}" letter-spacing="3">! {escape(label.upper())}</text>
  {body}
  <rect width="830" height="{h}" fill="url(#scan)"/>
</svg>
"""


def shots_button(label: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 40" width="830" height="40" role="img" aria-label="{escape(label)}">
  <title>{escape(label)}</title>
  <defs><style>text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}</style></defs>
  <rect x="0.5" y="0.5" width="829" height="39" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="40" fill="{RED}"/>
  <text x="24" y="25" font-size="12.5" fill="{TEXT}" letter-spacing="3">{escape(label.upper())}</text>
  <text x="806" y="25" font-size="12.5" fill="{DIM}" text-anchor="end">7 png</text>
</svg>
"""


ICON_SLUGS = {
    "python": "python", "c": "c", "c++": "cplusplus", "go": "go", "rust": "rust", "bash": "gnubash", "powershell": "powershell",
    "typescript": "typescript", "node.js": "nodedotjs", "javascript": "javascript", "sql": "sqlite", "wireshark": "wireshark",
    "burp suite": "portswigger", "owasp zap": "owasp", "google dorks": "google", "tor": "torproject", "wireguard": "wireguard",
    "owasp llm top 10": "owasp", "metasploit": "metasploit", "hashcat": "hashcat", "kali linux": "kalilinux", "parrot os": "parrotsecurity",
    "tails": "tails", "linux": "linux", "docker": "docker", "virtualbox": "virtualbox", "git": "git", "vs code": "visualstudiocode", "windows": "windows", "macos": "macos",
}


def _icon(icons: dict, name: str, x: float, y: float) -> str:
    slug = ICON_SLUGS.get(name)
    if slug and slug in icons:
        return f'<g transform="translate({x:.1f},{y}) scale(0.6667)"><path d="{icons[slug]}" fill="{TEXT}"/></g>'
    mono = "".join(ch for ch in name if ch.isalnum())[:2].lower() or "?"
    return (
        f'<rect x="{x + 0.5:.1f}" y="{y + 0.5}" width="15" height="15" rx="3" fill="none" stroke="{RED}" stroke-width="1"/>'
        f'<text x="{x + 8:.1f}" y="{y + 11}" font-size="8" font-weight="700" fill="{RED}" text-anchor="middle">{escape(mono)}</text>'
    )


def chip(name: str, icons: dict) -> str:
    """Один инструмент одной плашкой: значок simple-icons (CC0) или монограмма в красной рамке. Ссылку ставит README."""
    w = round(14 + 16 + 8 + len(name) * 7.8 + 14)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 30" width="{w}" height="30" role="img" aria-label="{escape(name)}">
  <title>{escape(name)}</title>
  <defs><style>text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}</style></defs>
  <rect x="0.5" y="0.5" width="{w - 1}" height="29" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="3" height="30" fill="{RED}"/>
  {_icon(icons, name, 14, 7)}
  <text x="38" y="19.5" font-size="13" fill="{TEXT}">{escape(name)}</text>
</svg>
"""


def category_label(title: str) -> str:
    w = round(len(title) * 10 + 8)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 22" width="{w}" height="22" role="img" aria-label="{escape(title)}">
  <title>{escape(title)}</title>
  <defs><style>text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}</style></defs>
  <text x="2" y="15" font-size="12" fill="{RED}" letter-spacing="3">{escape(title.upper())}</text>
</svg>
"""


def write_stack(cats: list, links: dict) -> str:
    """Пишет плашки в assets/stack/ и возвращает разметку для README (каждая плашка это ссылка)."""
    import json as _json
    import shutil

    icons = _json.loads((ROOT / "scripts" / "icons.json").read_text(encoding="utf-8"))
    out_dir = ASSETS / "stack"
    shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir()
    parts = []
    for ci, (title, names) in enumerate(cats):
        (out_dir / f"h{ci}.svg").write_text(category_label(title), encoding="utf-8")
        row = [f'<img src="assets/stack/h{ci}.svg" alt="{escape(title)}" height="22"/><br/>']
        for ni, n in enumerate(names):
            fn = f"c{ci}-{ni}.svg"
            (out_dir / fn).write_text(chip(n, icons), encoding="utf-8")
            url = links.get(n)
            img = f'<img src="assets/stack/{fn}" alt="{escape(n)}" height="30"/>'
            row.append(f'<a href="{url}">{img}</a>' if url else img)
        parts.append("<p>\n" + "\n".join(row) + "\n</p>")
    return "\n\n".join(parts)


def lang_button(code: str, active: bool) -> str:
    """Маленькая кнопка переключения языка в стиле карточек: активная с красной полоской, неактивная приглушённая."""
    bar = RED if active else LINE
    fill = TEXT if active else DIM
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 76 28" width="76" height="28" role="img" aria-label="{code}">
  <title>{code}</title>
  <defs><style>text {{ font-family: 'Courier New', Menlo, Consolas, monospace; }}</style></defs>
  <rect x="0.5" y="0.5" width="75" height="27" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="3" height="28" fill="{bar}"/>
  <text x="38" y="18.5" font-size="12" fill="{fill}" text-anchor="middle" letter-spacing="3">{code}</text>
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
    for name in ("ghoul", "shroud", "silhouette", "wyrm", "basilisk", "citadel", "ectoplasm"):
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
    releases = 0
    for n in names:
        releases += len(gh_json("api", f"repos/rephuren/{n}/releases") or [])
        for lang, size in (gh_json("api", f"repos/rephuren/{n}/languages") or {}).items():
            langs[lang] = langs.get(lang, 0) + size
        data = gh_json("api", "graphql", "-f", f'query={{repository(owner:"rephuren",name:"{n}"){{defaultBranchRef{{target{{... on Commit{{history{{totalCount}}}}}}}}}}}}')
        try:
            commits += data["data"]["repository"]["defaultBranchRef"]["target"]["history"]["totalCount"]
        except (TypeError, KeyError):
            pass
    tests = sum(int(p[4].split()[0]) for p in PROJECTS)
    shown = [(k, v) for k, v in sorted(langs.items(), key=lambda kv: -kv[1]) if k not in ("Makefile", "CMake", "Shell", "Dockerfile")][:8]
    total = sum(v for _, v in shown) or 1
    shown = [(k, v) for k, v in shown if v / total >= 0.003]  # мелочь меньше процента на карточке только шумит
    total = sum(v for _, v in shown) or 1
    colors = [RED, TEXT, "#b5b5b5", "#8a8a8a", "#686868", "#4d4d4d", "#383838", "#2a2a2a"]
    bar, legend, x = [], [], 24.0
    for i, (lang, size) in enumerate(shown):
        w = 782.0 * size / total
        bar.append(f'<rect x="{x:.1f}" y="150" width="{max(w - 2, 1):.1f}" height="8" fill="{colors[i]}"/>')
        x += w
        col, row = i % 4, i // 4
        lx, ly = 24 + col * 200, 178 + row * 38
        pct = f"{100 * size / total:.0f}%" if size / total >= 0.01 else "&lt;1%"
        legend.append(f'<rect x="{lx}" y="{ly}" width="9" height="9" fill="{colors[i]}"/><text x="{lx + 16}" y="{ly + 9}" font-size="12" fill="{TEXT}">{escape(lang)}</text><text x="{lx + 16}" y="{ly + 25}" font-size="11" fill="{DIM}">{pct}</text>')
    H = 224 + (38 if len(shown) > 4 else 0)
    numbers = [(str(len(names)), "проектов"), (str(tests), "тестов"), (str(releases), "релизов"), (str(commits), "коммитов")]
    cells = "".join(
        f'<g class="n"><text x="{24 + i * 200}" y="88" font-size="46" font-weight="700" fill="{RED if i == 1 else TEXT}">{escape(v)}</text>'
        f'<text x="{24 + i * 200}" y="112" font-size="12" fill="{DIM}" letter-spacing="2">{escape(label.upper())}</text></g>'
        for i, (v, label) in enumerate(numbers)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 {H}" width="830" height="{H}" role="img" aria-label="статистика: {len(names)} проектов, {tests} тестов, {commits} коммитов">
  <title>статистика профиля</title>
  <defs><pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" opacity="0.04"/></pattern>{STYLE}</defs>
  <rect x="0.5" y="0.5" width="829" height="{H - 1}" rx="2" fill="{PANEL}" stroke="{LINE}"/>
  <rect x="0" y="0" width="4" height="{H}" fill="{RED}"/>
  <text x="24" y="36" font-size="13" fill="{DIM}" letter-spacing="3">СТАТИСТИКА</text>
  <text x="806" y="36" font-size="14" fill="{RED}" text-anchor="end">&gt;<tspan class="blink">_</tspan></text>
  {cells}
  <text x="24" y="140" font-size="11" fill="{FAINT}" letter-spacing="2">ЯЗЫКИ ПО ДАННЫМ GITHUB</text>
  {"".join(bar)}
  {"".join(legend)}
  <rect width="830" height="{H}" fill="url(#scan)"/>
</svg>
"""


def main() -> None:
    cards = ASSETS / "cards"
    cards.mkdir(exist_ok=True)
    for name, title, line, tags, tests in PROJECTS:
        (cards / f"{name}.svg").write_text(card(name, title, line, tags, tests), encoding="utf-8")
    for code in ("RU", "EN"):
        for state, active in (("on", True), ("off", False)):
            (ASSETS / f"lang-{code.lower()}-{state}.svg").write_text(lang_button(code, active), encoding="utf-8")
    (ASSETS / "divider.svg").write_text(divider(), encoding="utf-8")
    (ASSETS / "footer.svg").write_text(footer(), encoding="utf-8")
    for lg in ("ru", "en"):
        (ASSETS / f"whoami-{lg}.svg").write_text(whoami(lg), encoding="utf-8")
    for lg, (lab, txt) in {'ru': ('Состояние проектов', 'Скриншоты ghoul, shroud, silhouette и ectoplasm сняты в демо-режиме на синтетических данных. Вывод wyrm и basilisk взят из прогонов на учебных целях. exorcist, banshee, chimera и gargoyle проверены только на своих учебных правилах, имитациях и синтетических данных. Таблица citadel посчитана на полигоне с намеренно наивным агентом. Методология и ограничения каждого проекта описаны в его README.'), 'en': ('Project status', "Screenshots of ghoul, shroud, silhouette and ectoplasm come from demo mode on synthetic data. wyrm and basilisk output comes from runs on training targets. exorcist, banshee, chimera and gargoyle were checked only on their own teaching rules, mocks and synthetic data. The citadel table was computed on a range with a deliberately naive agent. Methodology and limitations are described in each project's README.")}.items():
        (ASSETS / f"note-{lg}.svg").write_text(note(txt, lab), encoding="utf-8")
    for lg, lab in (("ru", "скриншоты"), ("en", "screenshots")):
        (ASSETS / f"shots-{lg}.svg").write_text(shots_button(lab), encoding="utf-8")
    import json as _json
    stack = _json.loads((ROOT / "scripts" / "stack.json").read_text(encoding="utf-8"))
    links = _json.loads((ROOT / "scripts" / "stack_links.json").read_text(encoding="utf-8"))
    markup = write_stack(stack["ru"], links)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = re.sub(r"(<!-- stack:start -->\n).*?(<!-- stack:end -->)", lambda m: m.group(1) + markup + "\n" + m.group(2), readme, flags=re.S)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    (ASSETS / "stats.svg").write_text(stats_svg(), encoding="utf-8")
    try:
        frame_images()
    except ImportError:
        print("Pillow не установлен: рамки для скриншотов пропущены")
    print("готово")


if __name__ == "__main__":
    main()
