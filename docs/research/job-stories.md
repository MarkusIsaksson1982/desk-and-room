# Job stories

Five job stories for the teacher's live-lesson board. They describe situations to design for, not features to build. None has been validated with a teacher.

**Labels used:** `assumption`, `desk research`, `synthetic`, `self-review`. Each story and each note carries one.

**Format:** When [situation], I want to [motivation], so I can [outcome].

---

## JS-01 — Start while pupils are still joining

**Job story:** When pupils are still arriving and the lesson has already started, I want to start the task without waiting for the full class, so the first minutes are not lost to a roster. `assumption`

- **Context:** A late joiner may arrive several minutes into the lesson. The teacher should not have to restart the task or refresh the screen. `synthetic`
- **Design implication:** The Live lesson screen must allow "start task" before every pupil is present, and add late joiners to the same lesson. `assumption`
- **Signals of success (design targets, not measured):** The teacher starts the task before the last pupil arrives; the late joiner appears without a restart; no duplicate lesson is created. `assumption`
- **Related persona:** Persona A and Persona B. `self-review`

---

## JS-02 — See who is stuck, who is done and how they are working

**Job story:** When pupils are working independently, I want to see who is stuck, who is done and how they are working at a glance, so I can choose the next pupil to visit or the next discussion. `assumption`

- **Context:** The teacher scans in short bursts while moving around the room. "Done" alone is not enough; the working matters. `assumption`
- **Design implication:** Rows should carry a status, a last-updated cue and a short view of the working, without opening every pupil. `assumption`
- **Signals of success (design targets, not measured):** The teacher can name the next pupil to help without opening more than one pupil's work; the status is readable at a glance on Desk. `assumption`
- **Related persona:** Persona A. `self-review`

---

## JS-03 — Discuss one pupil's working without exposing their name

**Job story:** When I project one pupil's working to the class, I want to show the mathematics without revealing who produced it, so the class can discuss the approach safely. `assumption`

- **Context:** The projector is visible to every pupil. The teacher may want to discuss a mistake, a neat method or two contrasting approaches. `synthetic`
- **Design implication:** Room hides names by default and uses a seat code or initials; the teacher can still see the name on Desk. Presenting is an explicit action, not an automatic mirror. `assumption`
- **Signals of success (design targets, not measured):** No pupil name is visible in Room by default; the teacher can return to Desk in one action; the class can follow the working at a distance. `assumption`
- **Related persona:** Persona A and Persona B. `self-review`

---

## JS-04 — Notice an idle pupil without calling them out

**Job story:** When a pupil has stopped changing their working for a while, I want a calm, non-accusatory signal and a quick way to check in, so I can help without embarrassing them in front of the class. `assumption`

- **Context:** "Idle" can mean stuck, thinking, distracted, disconnected or away. A public alarm would be harmful. `assumption`
- **Design implication:** Idle is shown on Desk with a shape, a label and a time; it is never shown by colour alone and never announced to the class by default. `assumption`
- **Signals of success (design targets, not measured):** The teacher can open the pupil's last step from the signal; the signal does not appear in Room unless the teacher chooses it; the pupil is not named aloud by the tool. `assumption`
- **Related persona:** Persona A and Persona B. `self-review`

---

## JS-05 — Leave with a short follow-up list

**Job story:** When the lesson ends, I want the follow-ups I marked during the lesson to be waiting for me, so I can plan the next lesson without reconstructing the room from memory — including when I was covering for someone else. `assumption`

- **Context:** Follow-ups may be marked in the middle of a lesson, between conversations, or at the end. An occasional teacher may need to leave a note for the regular teacher. `assumption`
- **Design implication:** The after-class strip shows a small number of follow-ups, each with enough context to act on, and does not rank pupils. `assumption`
- **Signals of success (design targets, not measured):** The teacher can see every follow-up marked during the lesson; the list fits on one screen; the occasional user can leave a note without extra setup. `assumption`
- **Related persona:** Persona A and Persona B. `self-review`

---

## What these stories deliberately leave out

- No story asks for surveillance of pupils' screens, keystrokes or answer text. `self-review`
- No story asks for a public ranking of pupils. `self-review`
- No story asks for AI recommendations or automatic grading. `self-review`
- No story assumes a second product for the projector; Room is a state of Live lesson. `self-review`

These exclusions are design boundaries from the brief, not validated user preferences. `assumption`
