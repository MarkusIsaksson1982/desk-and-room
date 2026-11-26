# Desk & Room — design process, Pass 2

A landing page for the Pass 2 artefacts of **Desk & Room**, a teacher's live-lesson board that works on a small laptop (**Desk**) and when projected to the whole class (**Room**).

**Stage:** design process. **There is no interactive prototype yet.** Pass 2 adds a dual-scale design system and a static component gallery on top of the Pass 1 research notes and flow documents.

- [Read the plan](../PLAN.md) for the concept, passes and guardrails.
- [Read the project README](../README.md) for the short version.

---

## What this pass contains

| Area | Artefact | What it is | Label |
|---|---|---|---|
| Research | [Source log](research/source-log.md) | Initial hypotheses; no public source was read in this session, so candidate sources are listed as unread. | `assumption` |
| Research | [Proto-personas](research/personas.md) | Two proto-personas: a classroom maths teacher and an occasional/substitute user. | `assumption` |
| Research | [Job stories](research/job-stories.md) | Five situations to design for, not validated features. | `assumption` |
| Research | [Lesson journey](research/lesson-journey.md) | A synthetic 45-minute lesson with breaks, a late joiner, an idle pupil and a projector switch. | `synthetic` |
| Research | [Assumptions log](research/assumptions.md) | Claims, basis, falsification route and status `unvalidated`. | `assumption` |
| Research | [Interview guide](research/interview-guide.md) | A teacher interview plan marked **not yet run**. | `assumption` |
| Flows | [Sitemap](flows/sitemap.md) | Class list → Live lesson → Pupil peek → After-class strip; Room is a state of Live lesson. | `assumption` |
| Flows | [Core flow and states](flows/core-flow.md) | Core flow plus empty, loading, connection-lost and finished states, with accessibility and privacy notes. | `assumption` |
| Design system | [Tokens and dual-scale system](design-system/index.md) | Token pipeline, Desk/Room modes, the status shape + label rule, focus and reduced motion, and how to run the checks. | `self-review` |
| Design system | [Contrast table](design-system/contrast.md) | Generated WCAG 2.x contrast ratios for text and status colours in both modes, treated as a design target. | `self-review` |
| Gallery | [Static component gallery](../gallery/index.html) | Every component state in both modes side by side, with seat codes in the Room column. | `synthetic` |

---

## How to read the labels

Every research item carries a label so the provenance is visible:

- `desk research` — derived from public sources that were actually read. **None were read in this session.**
- `assumption` — a reasoned guess, not yet validated.
- `synthetic` — invented for illustration, not observed.
- `self-review` — the author's own critique or decision, not a research finding.

No quotes, participants, interviews, usability results or numbers presented as findings appear in this pass.

---

## What is not here

- No interactive prototype, no clickable demo and no reusable component library.
- No usability results, no heuristic review and no case study.
- No real schools, classes, pupils, employers, vendors or commercial products.
- No compliance or legal claims. Accessibility and privacy are design targets and notes.
- No dark theme. The token set is light only.

---

## Project links

- [Plan](../PLAN.md)
- [README](../README.md)
- [Design system](design-system/index.md)
- [Contrast table](design-system/contrast.md)
- [Component gallery](../gallery/index.html)
