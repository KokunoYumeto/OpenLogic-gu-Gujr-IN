# Reproducing this cumulative chapter

Requirements: Python 3, BeautifulSoup 4, Pandoc, and LuaLaTeX with fontspec, amsmath, amssymb, amsthm, nicefrac, TikZ, xparse, hyperref and bookmark. Gujarati fonts are pinned and included in `fonts/`; the original variable-font identity and static instance parameters are recorded.

From the repository root:

```powershell
python tools/prepare_sets.py
python tools/build_sets_html.py
./tools/build_sets_guarded.ps1 -TimeoutMs 15000
```

The TeX script currently names the commissioned production and state boundaries explicitly. Adapt those two path parameters to a separate checkout before running elsewhere. It acquires the global Windows mutex once, retains it throughout all three passes and immediate log checks, and releases in `finally`. It never starts a TeX process if the slot is occupied, and never stops another task's process. Shell escape and automatic package installation are disabled. The captured process has a 180-second ceiling; only that owned process tree may be terminated on timeout.

The PDF is written to `build/gu-sets.pdf`. Its final two passes must have identical SHA-256 values. HTML is written to `reader/sets.html`. Open it locally with the adjacent assets and sibling `fonts/` directory present. It contains native MathML and requires no CDN.

The source-aligned files in `gu/` are the editable authority. The build adapters expand them into a reader; the individual upstream `subfiles` wrappers are retained for alignment, not claimed as independently compilable entry points in this cumulative build.
