# Assumptions log

Claims this design currently rests on. None has been validated. Every row is `unvalidated` and every row carries a label.

**Labels used:** `assumption`, `desk research`, `synthetic`, `self-review`.

**How to read this log:** "How a later prototype would falsify it" describes the observation that would count against the claim. It is not a test that has been run. A prototype does not exist yet.

| ID | Claim | Basis | How a later prototype would falsify it | Status | Label |
|---|---|---|---|---|---|
| A-01 | A teacher can read the class status in seconds on a 1280×800 laptop. | The brief says the teacher needs to see who is stuck, done and how they are working "in seconds"; no timing has been measured. | A timed task in a later prototype (for example "find who has not started") takes longer than the target chosen for that test (not yet set), or testers open several pupils before choosing one. | `unvalidated` | `assumption` |
| A-02 | Room mode needs larger type, larger targets and fewer rows than Desk mode. | Reasoning about viewing distance and projector legibility; no projected reading test has been run. | At 1920×1080, testers at the back of a room misread labels or status, or need to lean in; or the larger layout hides the information needed for the discussion. | `unvalidated` | `assumption` |
| A-03 | Hiding pupil names by default in Room is workable for a whole-class discussion. | The brief's privacy guardrail; no teacher has tried it. | Teachers cannot run the discussion without names, or repeatedly ask for a reveal; or pupils cannot follow which work is being shown. | `unvalidated` | `assumption` |
| A-04 | Status must be shown by shape and label, not colour alone. | Accessibility design target; the relevant public guidance was not read in this session. | A shape-and-label version is slower or less accurate than a colour-only version for sighted testers, or the labels add noise that slows the scan. | `unvalidated` | `assumption` |
| A-05 | An occasional or substitute teacher can complete the core flow on first use without training. | Proto-persona B; no first-use session has been run. | A first-time user needs help to open the class, start the task, present anonymised work or end the lesson; or gives up on a step. | `unvalidated` | `assumption` |
| A-06 | A late joiner can be added to a running lesson without a restart or duplicate lesson. | The lesson journey includes a late joiner; the behaviour is designed, not built. | The prototype requires a refresh, creates a second lesson, or shows the late joiner with a confusing status. | `unvalidated` | `assumption` |
| A-07 | An idle signal can help a teacher check in without feeling like surveillance or a public call-out. | The brief's care framing; no pupil or teacher reaction has been observed. | Teachers describe it as surveillance, pupils notice and dislike it, or the signal produces many false alarms for thinking or disconnected pupils. | `unvalidated` | `assumption` |
| A-08 | One Live lesson screen with Desk and Room states is clearer than two separate products or two navigation entries. | The brief's concept choice; no navigation test has been run. | Users look for a separate "projector" entry, get lost when toggling, or cannot tell which state they are in. | `unvalidated` | `assumption` |
| A-09 | Three follow-ups at the end of a lesson are enough for the after-class strip. | The brief proposes a thin strip of three follow-ups; no teacher has ranked or trialled this. | Teachers routinely mark more than three, cannot fit them on one screen, or need a different structure (for example per pupil or per topic). | `unvalidated` | `assumption` |
| A-10 | A connection loss can be handled with a clear banner, a last-updated time and read-only cached rows. | State design reasoning; no failure has been simulated with a user. | Users mistake cached rows for live data, retry repeatedly without understanding the state, or lose follow-ups marked during the outage. | `unvalidated` | `assumption` |
| A-11 | The core flow is operable by keyboard with a predictable focus order. | Accessibility design target; no keyboard-only run has happened. | A keyboard-only tester hits a focus trap, loses focus after a state change, or cannot reach the primary action. | `unvalidated` | `assumption` |
| A-12 | A synthetic class of 12 pupils is a useful size for the first layout. | The brief's fixture; no larger class has been tested. | A class of 30 breaks paging, makes the scan slow, or forces a density that fails the Room-mode targets. | `unvalidated` | `assumption` |
| A-13 | A neutral holding screen during breaks is safer than leaving the last projected view visible. | Privacy reasoning from the brief; no classroom observation. | Teachers find the extra step disruptive, or pupils need the previous view to stay on screen during a pause. | `unvalidated` | `assumption` |
| A-14 | Showing a short view of the working in the row is enough to choose the next pupil. | The brief says "how pupils are working" matters; the amount of detail is a guess. | Teachers still open most pupils' full work, or the short view is too small to judge and adds clutter. | `unvalidated` | `assumption` |
| A-15 | The after-class strip can stay generic and does not need a full review or feedback product. | The brief folds post-lesson review into a thin strip; no teacher has asked for more. | Teachers need a richer review, export or messaging flow before the strip is useful. | `unvalidated` | `assumption` |

---

## Assumptions that are deliberately **not** made

| Not assumed | Why | Label |
|---|---|---|
| That pupils have unlimited attention or reliable devices. | Idle and connection-lost states are part of the flow. | `self-review` |
| That the teacher knows every pupil's name or seating position. | The occasional-user persona may know neither. | `assumption` |
| That a projector is always connected or private. | Room is a state the teacher chooses; the screen may be visible to the whole class. | `assumption` |
| That research has already shown any of this. | No public source was read in this session. | `self-review` |
| That accessibility or privacy compliance has been achieved. | These are design targets and notes, not legal or compliance claims. | `self-review` |

---

## Status rule

Nothing in this log moves out of `unvalidated` without an actual observation: a usability session, a first-use session, a teacher interview, or a documented self-review against a named source. Until then, the design treats every row as a hypothesis. `self-review`
