<div align="center">

<img src="assets/banner.svg" alt="misxnthropy" width="100%"/>

</div>

<p align="center"><a href="README.md"><img src="assets/lang-ru-off.svg" alt="RU" width="76"/></a>&nbsp;<img src="assets/lang-en-on.svg" alt="EN" width="76"/></p>

<p align="center"><img src="assets/whoami-en.svg" alt="whoami: misxnthropy" width="830"/></p>

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ PROJECTS

<table>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/citadel"><img src="assets/cards/citadel.svg" alt="citadel" width="400"/></a></td><td valign="middle">What it does: <b>A gateway between an AI client and MCP servers.</b><br/>Inside: call policies, taint tracking, a block on the "lethal trifecta", tool-definition pinning.<br/>Checked: a benchmark on a range with a deliberately naive agent: 9 of 9 attacks pass without the gateway, none with it.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/basilisk"><img src="assets/cards/basilisk.svg" alt="basilisk" width="400"/></a></td><td valign="middle">What it does: <b>Looks in MCP configs and tool descriptions for what a model would read as instructions.</b><br/>Inside: hidden instructions, invisible Unicode, image leaks, shadowing; `pin` and `verify` catch changes after approval.<br/>Checked: 65 tests and runs on training targets.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/ectoplasm"><img src="assets/cards/ectoplasm.svg" alt="ectoplasm" width="400"/></a></td><td valign="middle">What it does: <b>From an agent session log, shows which foreign text led to a dangerous action.</b><br/>Inside: confidence level and event chain, a hook, HTML and SARIF, an open set of 75 labelled sessions.<br/>Checked: 93 tests; demo on synthetic sessions.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/exorcist"><img src="assets/cards/exorcist.svg" alt="exorcist" width="400"/></a></td><td valign="middle">What it does: <b>A test stand for LLM applications.</b><br/>Inside: 18 attacks with canaries in the prompt, mapped to the OWASP LLM Top 10 and MITRE ATLAS; targets: endpoint, command, mocks.<br/>Checked: 16 tests; not run against a real model.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/banshee"><img src="assets/cards/banshee.svg" alt="banshee" width="400"/></a></td><td valign="middle">What it does: <b>A defensive rule engine in Rust.</b><br/>Inside: a Sigma and YARA subset, logs and files, an ATT&CK summary; unsupported rules are rejected with a reason.<br/>Checked: 26 tests on my own rules and invented data, not on SigmaHQ.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/chimera"><img src="assets/cards/chimera.svg" alt="chimera" width="400"/></a></td><td valign="middle">What it does: <b>A passive network sensor.</b><br/>Inside: a C core reads pcap (DNS, TLS SNI), a Go analyzer finds beacons, DNS tunnels and scans, SQLite and a dashboard.<br/>Checked: 74 checks, core fuzzed with wyrm with no crashes; not run on live traffic.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/necropsy"><img src="assets/cards/necropsy.svg" alt="necropsy" width="400"/></a></td><td valign="middle">What it does: <b>Binary dissection.</b><br/>Inside: ELF and PE parsers in Go, hardening, imports, entropy, strings, ImHex patterns, teaching labs.<br/>Checked: 21 tests, cross-checked against `debug/elf` and `debug/pe`; ImHex and labs not run live.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/ghoul"><img src="assets/cards/ghoul.svg" alt="ghoul" width="400"/></a></td><td valign="middle">What it does: <b>An SSH trap with a fake shell.</b><br/>Inside: passwords, commands and download links from bots, own dashboard; nothing is executed.<br/>Checked: 29 tests and a demo on synthetic data, not on real bots.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/shroud"><img src="assets/cards/shroud.svg" alt="shroud" width="400"/></a></td><td valign="middle">What it does: <b>A steganography detector for images.</b><br/>Inside: file tails, metadata, LSB, RS analysis, chi-square, JPEG DCT; every verdict is explained.<br/>Checked: 24 tests.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/silhouette"><img src="assets/cards/silhouette.svg" alt="silhouette" width="400"/></a></td><td valign="middle">What it does: <b>A domain's external attack surface.</b><br/>Inside: subdomains, dangling CNAMEs, headers, email hardening, A–F grade, scan diff, `meta`, Shodan, nuclei.<br/>Checked: 100 tests; Shodan and nuclei on mocks only.</td></tr>
<tr><td width="410" valign="middle"><a href="https://github.com/rephuren/wyrm"><img src="assets/cards/wyrm.svg" alt="wyrm" width="400"/></a></td><td valign="middle">What it does: <b>A coverage-guided C++ fuzzer in the AFL spirit.</b><br/>Inside: shared-memory coverage, crash minimizer, persistent mode, workers; applied to the chimera core.<br/>Checked: 50 tests; slower and less clever than AFL++.</td></tr>
</table>

<details><summary>screenshots</summary>

**`citadel`**

<img src="assets/citadel.png" alt="citadel" width="720"/>

**`basilisk`**

<img src="assets/basilisk.png" alt="basilisk" width="720"/>

**`ectoplasm`**

<img src="assets/ectoplasm.png" alt="ectoplasm" width="720"/>

**`ghoul`**

<img src="assets/ghoul.png" alt="ghoul" width="720"/>

**`shroud`**

<img src="assets/shroud.png" alt="shroud" width="720"/>

**`silhouette`**

<img src="assets/silhouette.png" alt="silhouette" width="720"/>

**`wyrm`**

<img src="assets/wyrm.png" alt="wyrm" width="720"/>

</details>

> **Project status.** Screenshots of `ghoul`, `shroud`, `silhouette` and `ectoplasm` come from demo mode on synthetic data. `wyrm` and `basilisk` output comes from runs on training targets. `exorcist`, `banshee` and `chimera` were checked only on their own teaching rules, mocks and synthetic data. The `citadel` table was computed on a range with a deliberately naive agent. Methodology and limitations are described in each project's README.

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ CONTACT

- telegram: [@rephuren](https://t.me/rephuren) · [@wx1ze](https://t.me/wx1ze)
- email: [misxnthropy@gmail.com](mailto:misxnthropy@gmail.com)

<p align="center"><img src="assets/footer.svg" alt="exit 0" width="100%"/></p>
