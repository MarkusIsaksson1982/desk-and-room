# Proto-personas

Two proto-personas for a teacher's live-lesson board. These are **not real people** and no interviews have been run. They are written as testable guesses, not as findings.

**Labels used:** `assumption`, `desk research`, `synthetic`, `self-review`. Every item below carries one.

**Synthetic context shared by both personas:** a class called **Class North** with 12 pupils (**Pupil 01–Pupil 12**), a 45-minute maths lesson, pupils working on their own devices, a 1280×800 laptop on the teacher's desk and a 1920×1080 projector at the front. `synthetic`

---

## Proto-persona A — Classroom maths teacher

**One line:** A maths teacher who runs independent-work lessons and needs to see, in seconds, who is stuck, who is done and how pupils are working. `assumption`

### Context

| Item | Description | Label |
|---|---|---|
| Role | Secondary-school maths teacher; teaches several lessons a day. | `assumption` |
| Class | One class of about 12 pupils in the synthetic showcase; mixed confidence. | `synthetic` |
| Lesson shape | 45 minutes: short start, independent work, one or two whole-class discussions, a wrap-up. | `assumption` |
| Devices | Pupils work on their own devices; the teacher has a small laptop and a projector. | `assumption` |
| Room | Teacher sometimes stays at the laptop and sometimes moves between desks. | `assumption` |
| Tech comfort | Moderate: uses slides, a learning platform and spreadsheets; not a developer; will adopt a tool only if it saves time in the lesson. | `assumption` |
| Training | Little or no dedicated training time; learns by using the tool. | `assumption` |

### Goals

- See who is stuck, who is done and **how** pupils are working without opening every pupil's work. `assumption`
- Choose the next pupil to visit or the next piece of work to discuss. `assumption`
- Keep the lesson moving when pupils join late or drift. `assumption`
- Project one pupil's working for a whole-class discussion without exposing their name. `assumption`
- Leave the lesson with a short list of follow-ups rather than a memory of the room. `assumption`

### Likely behaviours (hypotheses)

- Scans the room and the screen in short bursts rather than watching continuously. `assumption`
- Sorts or filters by "needs help" when the class is large enough to need it. `assumption`
- Uses the projector for a whole-class discussion, not for routine monitoring. `assumption`
- May currently mirror a pupil's whole device to the projector, which can expose more than intended. `assumption`
- Marks follow-ups at the end of the lesson, or forgets them. `assumption`

### Pain points

- Dashboards that show only "done / not done" and hide the working. `assumption`
- Text and targets that are too small when projected. `assumption`
- Status shown by colour alone, or by icons with no label. `assumption`
- Losing the current row or scroll position when switching between laptop and projector. `assumption`
- Modal dialogs and setup steps that interrupt the lesson. `assumption`
- Not knowing whether the screen is live or stale. `assumption`

### Accessibility considerations (design targets, not personal disclosures)

- Must be readable at a distance when projected; large type and high contrast are design targets. `assumption`
- Must work for a teacher with low vision, colour-vision deficiency or a motor impairment; status uses shape and label, targets are large. `assumption`
- Must be operable by keyboard for the core flow, with visible focus and a predictable order. `assumption`
- Must tolerate 200% zoom without hiding the primary action. `assumption`

### Success definition (design target, not measured)

The teacher can answer "who needs me next?" and present one anonymised piece of working without leaving the Live lesson screen. `assumption`

### Quote

**No quote.** No interview has been run; inventing one would break the honesty rules. `self-review`

### What would change this persona

A real interview or a first-use session. Until then, every line above is a hypothesis. `assumption`

---

## Proto-persona B — Occasional / substitute user (the non-tech-savvy case)

**One line:** A teacher covering a class at short notice, on a shared laptop, with little or no handover and no time to learn the tool. `assumption`

### Context

| Item | Description | Label |
|---|---|---|
| Role | Occasional or substitute teacher; may cover a class they do not usually teach. | `assumption` |
| Notice | May receive the class minutes before the lesson. | `assumption` |
| Class knowledge | May not know pupils' names, seating or working habits. | `assumption` |
| Devices | Shared laptop; projector already connected, or connected by someone else. | `assumption` |
| Tech comfort | Low: mouse-first, avoids settings, may not know keyboard shortcuts, may be anxious about the projector. | `assumption` |
| Training | None for this tool; first use may happen in front of a class. | `assumption` |

### Goals

- Open the correct class without guessing. `assumption`
- Start the task with a safe default, even if not everyone has joined. `assumption`
- See who needs help without knowing the pupils personally. `assumption`
- Project work without revealing names. `assumption`
- End the lesson and leave a short note for the regular teacher. `assumption`

### Likely behaviours (hypotheses)

- Reads on-screen labels carefully and looks for one obvious next action. `assumption`
- Avoids settings, filters and anything that looks irreversible. `assumption`
- Uses the mouse rather than the keyboard. `assumption`
- Asks a nearby colleague for help if a term is unclear. `assumption`
- Leaves the projector on a neutral screen rather than risk showing pupil data. `assumption`

### Pain points

- Jargon, especially a mode name that sounds like a second product. `assumption`
- Hidden toggles and unclear defaults. `assumption`
- Dense rows with small text. `assumption`
- Error messages that do not say what to do next. `assumption`
- Fear of exposing a pupil's name or work to the whole class. `assumption`
- A flow that assumes knowledge of the class or the tool. `assumption`

### Needs

- One obvious primary action per state. `assumption`
- Plain language, with "Room" explained where it appears. `assumption`
- Safe defaults: names hidden on the projector, destructive actions confirmed. `assumption`
- Reversible actions and a clear way back. `assumption`
- On-screen help that does not require leaving the lesson. `assumption`
- A neutral holding screen between segments, so the projector is never left on pupil data. `assumption`

### Success definition (design target, not measured)

A first-time user can open the right class, start the task, present one anonymised piece of working and end the lesson without assistance. `assumption`

### Quote

**No quote.** No interview has been run; inventing one would break the honesty rules. `self-review`

### What would change this persona

A real first-use session with an occasional teacher, or an interview about handover. Until then, every line above is a hypothesis. `assumption`

---

## What the two personas share, and where they differ

| Dimension | Persona A — classroom teacher | Persona B — occasional user | Label |
|---|---|---|---|
| Same interface | Yes; Room is a state of Live lesson, not a separate product. | Yes. | `assumption` |
| Class knowledge | High. | Low or none. | `assumption` |
| Time to learn | Some, spread across lessons. | Almost none; first use may be live. | `assumption` |
| Default interaction | Keyboard and mouse; may use shortcuts. | Mouse-first; avoids shortcuts and settings. | `assumption` |
| Main risk | Tool adds work or hides the working. | Tool is confusing or exposes names. | `assumption` |
| Design implication | Density is acceptable on Desk, but not at the cost of clarity. | Clarity and safe defaults come before density. | `self-review` |

**Working rule:** if a flow works for Persona B on first use, it should also work for Persona A under time pressure. This is a design heuristic, not a validated result. `self-review`
