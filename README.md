# Desk & Room

A design-process showcase for a teacher's live-lesson board: one interface that works on a small laptop (**Desk**) and when projected to the whole class (**Room**). Room is a state of the Live lesson screen, not a separate product.

**Stage:** design-process stage, Pass 1. **There is no prototype yet.** This pass contains research notes and flow documents only.

Start at [docs/index.md](docs/index.md). The concept, passes and guardrails are in [PLAN.md](PLAN.md). Progress is in [CHANGELOG.md](CHANGELOG.md).

## What exists

- **Research pack:** a source log written as initial hypotheses (no public source read for this pass), two proto-personas, five job stories, a synthetic 45-minute lesson journey, an assumptions log with status `unvalidated`, and an interview guide marked *not yet run*.
- **Flows:** a sitemap and a core flow with empty, loading, connection-lost and finished states, with accessibility and privacy notes beside each flow.
- **Not here yet:** a prototype, a component library, usability results or a case study.

## Why

During a maths lesson a teacher needs to see in seconds who is stuck, who is done and how pupils are working, and then discuss one pupil's working with the class on the projector without exposing names. This project treats the laptop and the projector as two states of one product decision, not two products.

## Principles

- Synthetic data only. No real schools, classes, pupils, employers, vendors or commercial products.
- Research is labelled honestly: `desk research`, `assumption`, `synthetic` or `self-review`. No invented quotes, participants or findings.
- Accessibility and privacy are design targets to check on these screens, not compliance or legal claims.

## Checks
```bash
python3 scripts/check-docs.py   # required files, relative links resolve, research files carry provenance labels
```

## Licence
MIT, see [LICENSE](LICENSE).
