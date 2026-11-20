<div align="center">

<img src="assets/banner.svg" alt="misxnthropy" width="100%"/>

</div>

<p align="center"><a href="README.md"><img src="assets/lang-ru-off.svg" alt="RU" width="76"/></a>&nbsp;<img src="assets/lang-en-on.svg" alt="EN" width="76"/></p>

<p align="center"><img src="assets/whoami-en.svg" alt="whoami: misxnthropy" width="830"/></p>

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ PROJECTS

<!-- projects:start -->
<p align="center">
<a href="https://github.com/rephuren/citadel"><img src="assets/cards/citadel.svg" alt="citadel" width="400"/></a><br/>
A gateway between an AI client and MCP servers: call policies,<br/>
taint tracking, definition pinning. On the range, 9 of 9 attacks<br/>
pass without the gateway and none with it; the range is<br/>
deliberately simple.
</p>

<p align="center"><img src="assets/citadel.png" alt="citadel" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/basilisk"><img src="assets/cards/basilisk.svg" alt="basilisk" width="400"/></a><br/>
Finds what a model would read as a command in MCP configs and tool<br/>
descriptions, and catches definitions swapped after approval.<br/>
Static analysis, false positives are possible.
</p>

<p align="center"><img src="assets/basilisk.png" alt="basilisk" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/ectoplasm"><img src="assets/cards/ectoplasm.svg" alt="ectoplasm" width="400"/></a><br/>
From an agent session log, shows which foreign text led to a<br/>
dangerous action, with a confidence level and the event chain.<br/>
Demo on synthetic sessions.
</p>

<p align="center"><img src="assets/ectoplasm.png" alt="ectoplasm" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/exorcist"><img src="assets/cards/exorcist.svg" alt="exorcist" width="400"/></a><br/>
A test stand for LLM apps: 18 attacks with canaries in the prompt,<br/>
mapped to the OWASP LLM Top 10 and MITRE ATLAS. Not run against a<br/>
real model.
</p>

<p align="center">
<a href="https://github.com/rephuren/gargoyle"><img src="assets/cards/gargoyle.svg" alt="gargoyle" width="400"/></a><br/>
Rack middleware for Ruby: notices scanners and injections, serves<br/>
decoys with fake keys and catches their use. Not run on a real<br/>
site, observe-only by default.
</p>

<p align="center">
<a href="https://github.com/rephuren/banshee"><img src="assets/cards/banshee.svg" alt="banshee" width="400"/></a><br/>
A rule engine in Rust: a Sigma and YARA subset, logs and files, an<br/>
ATT&CK summary. Whatever it does not understand is rejected with a<br/>
reason. Tested on my own rules, not on SigmaHQ.
</p>

<p align="center">
<a href="https://github.com/rephuren/chimera"><img src="assets/cards/chimera.svg" alt="chimera" width="400"/></a><br/>
A passive network sensor: a C core reads pcap, a Go analyzer finds<br/>
beacons, DNS tunnels and scans. The core was fuzzed with wyrm<br/>
without crashes; not run on live traffic.
</p>

<p align="center">
<a href="https://github.com/rephuren/necropsy"><img src="assets/cards/necropsy.svg" alt="necropsy" width="400"/></a><br/>
ELF and PE dissection in Go: hardening, imports, entropy, strings,<br/>
ImHex patterns. ImHex and the teaching labs were not run live.
</p>

<p align="center">
<a href="https://github.com/rephuren/ghoul"><img src="assets/cards/ghoul.svg" alt="ghoul" width="400"/></a><br/>
An SSH trap with a fake shell: records passwords, commands and<br/>
download links from bots, executes nothing. Demo on synthetic<br/>
data, not on real bots.
</p>

<p align="center"><img src="assets/ghoul.png" alt="ghoul" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/shroud"><img src="assets/cards/shroud.svg" alt="shroud" width="400"/></a><br/>
Looks for hidden data in images: file tails, metadata, LSB, RS<br/>
analysis, chi-square. Every verdict is explained, but it is<br/>
statistical and not proof.
</p>

<p align="center"><img src="assets/shroud.png" alt="shroud" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/silhouette"><img src="assets/cards/silhouette.svg" alt="silhouette" width="400"/></a><br/>
Shows a domain's external attack surface: subdomains, dangling<br/>
CNAMEs, email hardening, an A-F grade and the diff between scans.<br/>
Shodan and nuclei are checked on mocks only.
</p>

<p align="center"><img src="assets/silhouette.png" alt="silhouette" width="640"/></p>

<p align="center">
<a href="https://github.com/rephuren/wyrm"><img src="assets/cards/wyrm.svg" alt="wyrm" width="400"/></a><br/>
A C++ fuzzer in the AFL spirit: coverage, crash minimizer,<br/>
persistent mode, workers. Applied to the chimera core; slower and<br/>
less clever than AFL++.
</p>

<p align="center"><img src="assets/wyrm.png" alt="wyrm" width="640"/></p>
<!-- projects:end -->

<p align="center"><img src="assets/note-en.svg" alt="Project status: Screenshots of ghoul, shroud, silhouette and ectoplasm come from demo mode on synthetic data. wyrm and basilisk output comes from runs on training targets. exorcist, banshee, chimera and gargoyle were checked only on their own teaching rules, mocks and synthetic data. The citadel table was computed on a range with a deliberately naive agent. Methodology and limitations are described in each project's README." width="830"/></p>

<p align="center"><img src="assets/divider.svg" alt="" width="830"/></p>

## ▓ CONTACT

- telegram: [@rephuren](https://t.me/rephuren) · [@wx1ze](https://t.me/wx1ze)
- email: [misxnthropy@gmail.com](mailto:misxnthropy@gmail.com)

<p align="center"><img src="assets/footer.svg" alt="exit 0" width="100%"/></p>
