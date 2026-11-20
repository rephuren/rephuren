<div align="center">

<img src="assets/banner.svg" alt="misxnthropy" width="100%"/>

</div>

<p align="center"><a href="README.md"><img src="assets/lang-ru-off.svg" alt="RU" width="76"/></a>&nbsp;<img src="assets/lang-en-on.svg" alt="EN" width="76"/></p>

<p align="center"><img src="assets/whoami-en.svg" alt="whoami: misxnthropy" width="830"/></p>

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ PROJECTS

<!-- projects:start -->
<p align="center">
<a href="https://github.com/rephuren/citadel"><img src="assets/cards/citadel.svg" alt="citadel" width="400"/></a>
<a href="https://github.com/rephuren/basilisk"><img src="assets/cards/basilisk.svg" alt="basilisk" width="400"/></a>
<a href="https://github.com/rephuren/ectoplasm"><img src="assets/cards/ectoplasm.svg" alt="ectoplasm" width="400"/></a>
<a href="https://github.com/rephuren/exorcist"><img src="assets/cards/exorcist.svg" alt="exorcist" width="400"/></a>
<a href="https://github.com/rephuren/gargoyle"><img src="assets/cards/gargoyle.svg" alt="gargoyle" width="400"/></a>
<a href="https://github.com/rephuren/banshee"><img src="assets/cards/banshee.svg" alt="banshee" width="400"/></a>
<a href="https://github.com/rephuren/chimera"><img src="assets/cards/chimera.svg" alt="chimera" width="400"/></a>
<a href="https://github.com/rephuren/necropsy"><img src="assets/cards/necropsy.svg" alt="necropsy" width="400"/></a>
<a href="https://github.com/rephuren/ghoul"><img src="assets/cards/ghoul.svg" alt="ghoul" width="400"/></a>
<a href="https://github.com/rephuren/shroud"><img src="assets/cards/shroud.svg" alt="shroud" width="400"/></a>
<a href="https://github.com/rephuren/silhouette"><img src="assets/cards/silhouette.svg" alt="silhouette" width="400"/></a>
<a href="https://github.com/rephuren/wyrm"><img src="assets/cards/wyrm.svg" alt="wyrm" width="400"/></a>
</p>

<a href="https://github.com/rephuren/citadel"><img src="assets/proj/citadel.svg" alt="citadel" height="30"/></a>

A gateway between an AI client and MCP servers: call policies, taint tracking, definition pinning. On the range, 9 of 9 attacks pass without the gateway and none with it; the range is deliberately simple.

<p align="center"><img src="assets/citadel.png" alt="citadel" width="720"/></p>

<a href="https://github.com/rephuren/basilisk"><img src="assets/proj/basilisk.svg" alt="basilisk" height="30"/></a>

Finds what a model would read as a command in MCP configs and tool descriptions, and catches definitions swapped after approval. Static analysis, false positives are possible.

<p align="center"><img src="assets/basilisk.png" alt="basilisk" width="720"/></p>

<a href="https://github.com/rephuren/ectoplasm"><img src="assets/proj/ectoplasm.svg" alt="ectoplasm" height="30"/></a>

From an agent session log, shows which foreign text led to a dangerous action, with a confidence level and the event chain. Demo on synthetic sessions.

<p align="center"><img src="assets/ectoplasm.png" alt="ectoplasm" width="720"/></p>

<a href="https://github.com/rephuren/exorcist"><img src="assets/proj/exorcist.svg" alt="exorcist" height="30"/></a>

A test stand for LLM apps: 18 attacks with canaries in the prompt, mapped to the OWASP LLM Top 10 and MITRE ATLAS. Not run against a real model.

<a href="https://github.com/rephuren/gargoyle"><img src="assets/proj/gargoyle.svg" alt="gargoyle" height="30"/></a>

Rack middleware for Ruby: notices scanners and injections, serves decoys with fake keys and catches their use. Not run on a real site, observe-only by default.

<a href="https://github.com/rephuren/banshee"><img src="assets/proj/banshee.svg" alt="banshee" height="30"/></a>

A rule engine in Rust: a Sigma and YARA subset, logs and files, an ATT&CK summary. Whatever it does not understand is rejected with a reason. Tested on my own rules, not on SigmaHQ.

<a href="https://github.com/rephuren/chimera"><img src="assets/proj/chimera.svg" alt="chimera" height="30"/></a>

A passive network sensor: a C core reads pcap, a Go analyzer finds beacons, DNS tunnels and scans. The core was fuzzed with wyrm without crashes; not run on live traffic.

<a href="https://github.com/rephuren/necropsy"><img src="assets/proj/necropsy.svg" alt="necropsy" height="30"/></a>

ELF and PE dissection in Go: hardening, imports, entropy, strings, ImHex patterns. ImHex and the teaching labs were not run live.

<a href="https://github.com/rephuren/ghoul"><img src="assets/proj/ghoul.svg" alt="ghoul" height="30"/></a>

An SSH trap with a fake shell: records passwords, commands and download links from bots, executes nothing. Demo on synthetic data, not on real bots.

<p align="center"><img src="assets/ghoul.png" alt="ghoul" width="720"/></p>

<a href="https://github.com/rephuren/shroud"><img src="assets/proj/shroud.svg" alt="shroud" height="30"/></a>

Looks for hidden data in images: file tails, metadata, LSB, RS analysis, chi-square. Every verdict is explained, but it is statistical and not proof.

<p align="center"><img src="assets/shroud.png" alt="shroud" width="720"/></p>

<a href="https://github.com/rephuren/silhouette"><img src="assets/proj/silhouette.svg" alt="silhouette" height="30"/></a>

Shows a domain's external attack surface: subdomains, dangling CNAMEs, email hardening, an A-F grade and the diff between scans. Shodan and nuclei are checked on mocks only.

<p align="center"><img src="assets/silhouette.png" alt="silhouette" width="720"/></p>

<a href="https://github.com/rephuren/wyrm"><img src="assets/proj/wyrm.svg" alt="wyrm" height="30"/></a>

A C++ fuzzer in the AFL spirit: coverage, crash minimizer, persistent mode, workers. Applied to the chimera core; slower and less clever than AFL++.

<p align="center"><img src="assets/wyrm.png" alt="wyrm" width="720"/></p>
<!-- projects:end -->

<p align="center"><img src="assets/note-en.svg" alt="Project status: Screenshots of ghoul, shroud, silhouette and ectoplasm come from demo mode on synthetic data. wyrm and basilisk output comes from runs on training targets. exorcist, banshee, chimera and gargoyle were checked only on their own teaching rules, mocks and synthetic data. The citadel table was computed on a range with a deliberately naive agent. Methodology and limitations are described in each project's README." width="830"/></p>

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ CONTACT

- telegram: [@rephuren](https://t.me/rephuren) · [@wx1ze](https://t.me/wx1ze)
- email: [misxnthropy@gmail.com](mailto:misxnthropy@gmail.com)

<p align="center"><img src="assets/footer.svg" alt="exit 0" width="100%"/></p>
