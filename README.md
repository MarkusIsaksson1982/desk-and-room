# Desk & Room

A design-process showcase for a teacher's live-lesson board: one interface that works on a small laptop (**Desk**) and when projected to the whole class (**Room**). Room is a state of the Live lesson screen, not a separate product.

**Stage:** design-process stage, Pass 2. **There is no interactive prototype yet.** Pass 2 adds design tokens, a generated contrast table and a static component gallery on top of the Pass 1 research notes and flow documents.

Start at [docs/index.md](docs/index.md). The concept, passes and guardrails are in [PLAN.md](PLAN.md). Progress is in [CHANGELOG.md](CHANGELOG.md).

## What exists

- **Research pack:** a source log written as initial hypotheses (no public source read for this pass), two proto-personas, five job stories, a synthetic 45-minute lesson journey, an assumptions log with status `unvalidated`, and an interview guide marked *not yet run*.
- **Flows:** a sitemap and a core flow with empty, loading, connection-lost and finished states, with accessibility and privacy notes beside each flow.
- **Design system (Pass 2):** `tokens.json` as the source of truth, generated `styles/tokens.css`, a generated contrast table for Desk and Room modes, and a static component gallery showing both modes side by side. See [docs/design-system/index.md](docs/design-system/index.md) and [gallery/index.html](gallery/index.html).
- **Not here yet:** an interactive prototype, a reusable component library, usability results or a case study.

## Why

During a maths lesson a teacher needs to see in seconds who is stuck, who is done and how pupils are working, and then discuss one pupil's working with the class on the projector without exposing names. This project treats the laptop and the projector as two states of one product decision, not two products.

## Principles

- Synthetic data only. No real schools, classes, pupils, employers, vendors or commercial products.
- Research is labelled honestly: `desk research`, `assumption`, `synthetic` or `self-review`. No invented quotes, participants or findings.
- Accessibility and privacy are design targets to check on these screens, not compliance or legal claims.

## Checks
```bash
python3 scripts/check-docs.py            # required files, relative links resolve, research files carry provenance labels
python3 scripts/build_tokens.py          # regenerate styles/tokens.css from tokens.json
python3 scripts/contrast_table.py        # regenerate docs/design-system/contrast.md
python3 -m unittest discover -s tests -v # token, contrast, mode-scale and status tests
```

## Licence
MIT, see [LICENSE](LICENSE).
