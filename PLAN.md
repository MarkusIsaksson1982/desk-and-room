# PLAN — "Desk & Room": a teacher live-lesson board that works on a laptop and on the class projector

Working name: **Desk & Room** (repo name if published: `desk-and-room`). Generic, check for name clashes before publishing.
Status: planning done (2026-11-19); next is Pass 1. Nothing is public yet.

This file is written to be publishable as-is. It names no company, product, school, municipality or person, and contains no CV content. Private working notes, tool outputs and personal documents are kept out of public exports.

## 1. Problem and constraint

A maths teacher runs a lesson where every pupil works on tasks on their own device. The teacher needs to see, in seconds, who is stuck, who is done and *how* pupils are working, so they can choose the next discussion or the next pupil to visit. The same teacher interface is used on a small laptop **and** projected to the whole class, by teachers who are not especially tech-savvy. Most dashboards solve one of those screens; this showcase designs for both as one product decision.

## 2. Concept choice (all three planning passes agreed)

| Candidate | Verdict |
|---|---|
| **A. Live lesson board** with a Desk (dense, laptop) mode and a Room (projector) mode | **Chosen.** It sits directly on the hard constraint and gives every phase a real artefact. |
| B. Differentiation / task planner before the lesson | Folded in as one secondary screen idea, not built. |
| C. Post-lesson review and feedback lane | Folded in as a thin "after-class strip" (three follow-ups), not a separate product. |

Core flow: open class → start task → scan progress (Desk) → switch to Room to discuss one pupil's anonymised working → back to Desk → mark follow-ups → end lesson → after-class strip.

## 3. Phases (1–3 evenings each, about 12–14 evenings in total)

| Phase | Evenings | Deliverables | Adjacent skill it shows |
|---|---:|---|---|
| P0 Desk research pack | 2 | Source log of public sources actually read; 2 proto-personas (classroom maths teacher; occasional/substitute user = the non-tech-savvy case); 5 job stories; one 45-minute lesson journey with breaks (late joiner, idle pupil, projector switch); assumptions log (claim, basis, how the prototype would falsify it, status `unvalidated`); a teacher interview guide marked *not yet run*. | Product discovery |
| P1 IA and flows | 1–2 | Sitemap (Class list → Live lesson → Pupil peek → After-class strip; Room is a *state* of Live lesson); core flow plus empty, loading, connection-lost and finished states; privacy and a11y notes beside the flow. | Product design |
| P2 Tokens and dual-scale design system | 2–3 | `tokens.json` → CSS custom properties; two modes `desk` (13–16 px body, 8 px grid) and `room` (body ≥ 28 px, targets ≥ 64 px, status by shape + label not colour alone, max ~6 pupils visible before paging); contrast table for both modes against WCAG 2.2 AA as a design target; focus ring and reduced-motion spec; static component gallery route showing every state in both modes. | Design systems |
| P3 Repo-native wireframes | 1–2 | Low-fi wireframes as SVG/HTML for 4 screens × 2 modes (1280×800 laptop, 1920×1080 projected). Optional Figma mirror if wanted; the repo stays canonical. | Figma-equivalent artefacts |
| P4 Clickable prototype | 3 | Vite + React + TypeScript, client-only, hash routes, keyboard-operable. Seeded synthetic class ("Class North", pupils "Pupil 01–12", typed synthetic working steps, no handwriting). Scripted clock for "live" updates, clearly labelled simulated. Room mode hides names by default (seat codes/initials). README tour of what is simulated. | Frontend / TypeScript |
| P5 Evaluation and accessibility | 2 | Usability test plan with 5 synthetic tasks (find who has not started; project without showing names; open the stuck pupil's last step; leave Room mode; mark a follow-up), observation sheet, success signals; results only if sessions really happen, labelled hallway test with method and n. Self heuristic review (Nielsen 10) signed as the author's review. Playwright + axe on all routes in both modes; manual keyboard, 200 % zoom, reduced motion, projected-reading check. Publish what still fails. | Usability + a11y |
| P6 After-launch measurement and QA | 2 | Versioned event schema (`lesson_opened`, `room_mode_toggled`, `pupil_row_focused`, `work_presented`, `followup_marked`, `lesson_ended`) with no free-text pupil work; generator for a synthetic 4-week JSONL stream; small metrics view (time to first focus, Room uses per lesson, follow-ups per lesson); data-quality checks (required fields, enums, id format, duplicate ids, impossible durations) that fail CI; 10–15 manual test cases incl. both viewports, keyboard and sv/en localisation; one contract test (Zod schema) against a fixture or a tiny read-only Node/TS route, described with an OpenAPI snippet. | Data + QA + Node/TS |
| P7 Case study and ship | 1–2 | ≤ 800-word case study: problem and constraint → process (labelled desk research) → IA → dual-mode system → prototype → what was tested and what was not → a11y and privacy posture → what to measure after launch → next steps. GitHub Actions: typecheck, unit, Playwright, data-quality, build; static hosting. | Communication |

Cut order if time slips: P6 metrics view → contract test → second flow in P1. The prototype (P4) and the dual-mode system (P2) are never cut.

## 3a. Cadence

- Work happens in **irregular passes**, not daily. A pass is triggered only on days the author chooses (the trigger is recorded in private notes, not here).
- **Every pass ends publish-ready** the same day or by the next morning:
  - `README.md` is a clean, generic public README that describes only what exists.
  - `CHANGELOG.md` gets a short dated entry for the pass.
  - All tests and checks pass: `scripts/check-docs.py` (public) and a private pre-publish scan that exports the committed tree and fails on disallowed terms or missing files.
  - Private working material never enters the public export.
- Publishing is a separate step that needs the owner's explicit approval. The public repo is created from a clean export with fresh history, never by pushing the private working repo.
- If a pass cannot finish, it is reverted or trimmed to the last publish-ready state before it ends.

## 3b. Passes (self-contained increments, each ends publish-ready)

| Pass | Contains | Publish-ready when |
|---|---|---|
| **Pass 1** | P0 desk research pack + P1 screen structure and flows + README/landing (`docs/index.md` linking the artefacts) | Every research item labelled `desk research` or `assumption`; flows as Markdown + Mermaid or SVG; README states "design-process stage, no prototype yet"; check script passes. |
| **Pass 2** | P2 tokens + dual-scale (desk/room) system + static component gallery page | `tokens.json` → CSS builds; a contrast table for both modes is generated by a script and checked by a test; gallery opens as a static page. |
| **Pass 3** | P3 wireframes (4 screens × 2 modes) | SVG/HTML wireframes linked from the landing; a link-check test passes. |
| **Pass 4** | P4 clickable prototype, part 1: Live lesson in Desk + Room modes on synthetic fixtures | `npm ci && npm test && npm run build` pass; Playwright smoke on both modes; static build deployable. |
| **Pass 5** | P4 part 2: Pupil peek, follow-ups, after-class strip, empty/loading/connection-lost states | Same gates as Pass 4 plus state tests. |
| **Pass 6** | P5 usability test plan, heuristic self-review, axe + manual a11y checks | axe runs in CI on both modes; findings published, including what still fails. |
| **Pass 7** | P6 event schema, synthetic stream, data-quality checks, manual test cases, contract test | Data-quality checks and contract test run in CI; metrics view optional (first to cut). |
| **Pass 8** | P7 case study and polish | Case study ≤ 800 words; all links valid; check script passes. |

Passes may be merged or split on a given day, but none may end in a non-publishable state.

## 4. Tech choices

- **Use:** Vite, React, TypeScript (strict), CSS custom properties from tokens (no utility framework, the token pipeline is the point), static JSON fixtures, Zod, Vitest, Playwright + axe-core, GitHub Actions, static hosting. A Python or Node script for data-quality checks, whichever is faster; no second app server.
- **Do not build:** auth, accounts, database, websockets, handwriting recognition, message brokers, streaming or warehouse infrastructure, district or pupil apps, content-authoring AI, AI teaching recommendations, native apps, npm-published component library, i18n beyond one sv/en string file. Backend and data systems appear only as "later seams" in the case study (events could be streamed; roster could come from an API).

## 5. Honesty and privacy guardrails

- Every research artefact carries a provenance label: `desk research`, `assumption`, `synthetic`, `self-review`. No invented quotes, participants or outcome metrics.
- Synthetic data only; pupil identifiers are obviously fake; Room mode hides names by default; the event schema stores no answer text; no third-party trackers on the demo.
- Accessibility and privacy are shown as general awareness ("checked with axe and a contrast table on these screens"), never as compliance or legal claims.
- AI coding agents may write code; the author records the design decisions and what was rejected.
- The concept must stay generic and not mimic any specific commercial product's UI or branding.

## 6. Planning passes (raw tool outputs kept privately)

| Pass | Tool / model | Key contribution kept |
|---|---|---|
| OpenCode | Lenovo, `opencode/deepseek-v4.1-flash-free` | "Two-viewport rule", 1280×800 vs 1920×1080 wireframes, explicit cut order, publish failing a11y results. |
| Codex | `codex exec` (box) | Empty/loading/connection-lost states, measure teacher actions not pupil surveillance, no results unless sessions occur. |
| Grok Build | `grok` 1.0.88, `--effort low` (box) | Desk/Room naming, Room as a state not a product, shape+label status, names hidden in Room, risk table. |

Rejected: Storybook (a static gallery route is enough), a full NestJS/MongoDB mock backend (echoes job ads without adding design value), a Figma file as the source of truth.

## 7. Open questions (also in STATUS.md)

1. UI language: Swedish, English, or a sv/en string file with English visible by default?
2. Room-mode default: seat codes, initials, or synthetic names with a hide toggle?
3. Can 2–3 hallway testers (or later, consenting teachers) try the prototype, or ship with plan + heuristic review only?
4. Optional Figma mirror for reviewers who expect Figma?
5. Real evening budget for the next two weeks; is cutting the P6 metrics view acceptable?
6. Publish as a new public repo under the main GitHub account when ready (needs explicit approval)?
