# Initial hypotheses — source log (no public sources read in this session)

**Status:** No public source was opened or read in this session. This file is therefore a list of **initial hypotheses** and candidate public sources, not a log of research findings. Every candidate below is marked **unread**.

**What was read in this session:** `PLAN.md` and `README.md` in this folder only. Those are project documents, not public research sources.

**Labels used:** `assumption`, `desk research`, `synthetic`, `self-review`, `initial hypothesis`. In this pass, almost everything is `assumption` or `synthetic` because no external source was consulted.

---

## Why this file exists

A source log should show what was actually read and what changed because of it. This pass has no such reading. Keeping the file honest is more useful than filling it with links that were never opened.

- No quote, participant, interview, usability result or number in this repository is presented as a finding. `self-review`
- No source is cited as support for a design decision. `self-review`
- URLs are deliberately omitted until a source is actually opened. Adding a link now would imply it was checked. `assumption`

---

## Candidate public sources (all unread)

| Candidate source | What it could inform | Status | Label | Notes |
|---|---|---|---|---|
| Web Content Accessibility Guidelines (WCAG) 2.2 | Contrast, focus visibility, target size, reflow, status messages, motion | **Unread** | `assumption` | Used in this pass only as the name of a design target, never as a claim that anything passes. |
| WAI-ARIA Authoring Practices | Keyboard patterns, focus management, live-region behaviour | **Unread** | `assumption` | Would inform the keyboard path and live-update announcements in the flows. |
| Public guidance on classroom orchestration and teacher noticing | How teachers scan a room, choose whom to help, and pace a lesson | **Unread** | `assumption` | Would test whether the row scan matches real classroom practice. |
| Public literature on substitute and occasional teachers | Handover, first-use confidence, low-training use | **Unread** | `assumption` | Would test proto-persona B and the "no training" success target. |
| Public guidance on data minimisation and privacy in classroom tools | Names on a projector, retention, what a teacher needs to see | **Unread** | `assumption` | Would inform the privacy notes; not a legal assessment. |
| Public guidance on projection legibility and viewing distance | Type size, contrast and density at the back of a room | **Unread** | `assumption` | Would test the Room-mode sizes in a later pass. |
| Ten usability heuristics (public framework) | A later heuristic self-review | **Unread this session** | `assumption` | The author is aware of the framework but did not open a source in this session. |
| Public guidance on reduced motion and animation | State transitions and loading behaviour | **Unread** | `assumption` | Would inform the reduced-motion notes beside the flows. |

**No source in this table has been read. Do not treat any row as evidence.** `self-review`

---

## What this log does not contain

- No interview notes, transcripts or participant details. `self-review`
- No usability results or task timings. `self-review`
- No statistics presented as findings. `self-review`
- No claim that a public standard, paper or guide supports a specific screen decision. `self-review`
- No real school, class, pupil, employer, vendor or commercial product. `self-review`

---

## How to update this log later

1. When a source is actually opened, add the date, the exact section read, and a one-line takeaway. `assumption`
2. Record which artefact changed because of it, or write "no change". `assumption`
3. Keep unread candidates marked **unread**; do not quietly promote them to evidence. `assumption`
4. If a claim cannot be traced to a read source, leave it labelled `assumption`. `assumption`
5. If a later usability session happens, report method and n, and publish what failed as well as what passed. `assumption`

---

## Traceability in this pass

| Artefact | Basis in this pass | Label |
|---|---|---|
| `personas.md` | Project brief plus reasoned guesses about classroom work; no interviews | `assumption` |
| `job-stories.md` | Project brief plus the same guesses; written as hypotheses to test | `assumption` |
| `lesson-journey.md` | A constructed 45-minute scenario, not an observed lesson | `synthetic` |
| `assumptions.md` | Claims extracted from the brief and the flows, each with a falsification route | `assumption` |
| `interview-guide.md` | A question plan that has not been run | `assumption` |
| `../flows/sitemap.md` | The brief's screen list plus information-architecture reasoning | `assumption` |
| `../flows/core-flow.md` | The brief's core flow plus state and accessibility reasoning | `assumption` |
| Accessibility notes | Design targets, not compliance claims; candidate standard unread | `assumption` |
| Privacy notes | Project guardrails plus design reasoning; not a legal assessment | `assumption` |
