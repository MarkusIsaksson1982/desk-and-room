# Changelog

## 2026-11-26 — Pass 2: tokens, dual-scale system, static gallery
- Added `tokens.json` (light theme, 8 px spacing, type scale, focus ring, motion with a reduced-motion value) with Desk and Room modes: Desk body 15 px and 32 px targets; Room body 32 px, 64 px targets, at most 6 pupils visible.
- Added `scripts/build_tokens.py` (generates `styles/tokens.css`, `--check` for drift) and `scripts/contrast_table.py` (generates `docs/design-system/contrast.md`; 36 of 36 pairs meet the WCAG 2.2 AA design target).
- Status is shown by shape and label, never colour alone (circle, triangle, square, dashed circle).
- Added a static component gallery (`gallery/index.html`) showing every state in both modes, with seat codes in Room mode.
- Added `tests/test_tokens.py` (9 checks) and a design-system page (`docs/design-system/index.md`). Still no interactive prototype.

## 2026-11-20 — First public release
- Published at https://github.com/MarkusIsaksson1982/desk-and-room (plan + Pass 1, fresh history).
- Added `scripts/check-docs.py`: required files, relative links and research provenance labels.

## 2026-11-19 — Pass 1: desk research and flows
- Added a research pack (source log as initial hypotheses, two proto-personas, five job stories, a synthetic 45-minute lesson journey, an unvalidated assumptions log, and an interview guide not yet run).
- Added a sitemap and a core flow with empty, loading, connection-lost and finished states, plus a landing page at `docs/index.md`.
- README now describes this design-process stage: research notes and flows exist; there is still no prototype.

## 2026-11-19 — Planning
- Concept chosen: a live-lesson board with Desk (laptop) and Room (projector) modes.
- Plan split into eight self-contained passes, each ending publish-ready.
- Added a public README, this changelog, an MIT licence and a publish-readiness check.
