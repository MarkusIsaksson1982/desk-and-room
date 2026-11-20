#!/usr/bin/env python3
"""Public docs check (stdlib only): required files exist, every relative Markdown link resolves,
and every research file carries a provenance label. Exit 1 on any failure."""
import pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
fail = []
for f in ("README.md", "CHANGELOG.md", "LICENSE", "PLAN.md", "docs/index.md"):
    if not (root / f).is_file() or not (root / f).stat().st_size:
        fail.append(f"missing or empty: {f}")

link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
md_files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
checked = 0
for md in md_files:
    text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for target in link.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        checked += 1
        if not (md.parent / path).resolve().exists():
            fail.append(f"broken link in {md.relative_to(root)}: {target}")

labels = ("`desk research`", "`assumption`", "`synthetic`", "`self-review`")
for md in sorted((root / "docs" / "research").glob("*.md")):
    if not any(l in md.read_text(encoding="utf-8") for l in labels):
        fail.append(f"no provenance label in {md.relative_to(root)}")

for f in fail:
    print("FAIL", f)
print(f"{len(md_files)} Markdown files, {checked} relative links checked")
print("DOCS CHECK:", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
