# Design system — Desk & Room

The Pass 2 design system is a small token pipeline plus a static component gallery. It covers the same teacher board in two modes: **Desk** on a laptop and **Room** on the class projector. It is a design-process artefact, not a component library or a compliance claim.

- [Open the static component gallery](../../gallery/index.html)
- [Read the generated contrast table](contrast.md)

---

## Token pipeline

`tokens.json` is the source of truth. It holds the light colour theme, the 8 px spacing scale, type sizes and weights, radii, focus ring, motion durations, status metadata and the two mode profiles.

`scripts/build_tokens.py` reads that file and writes `styles/tokens.css`:

- base custom properties in `:root`;
- mode overrides in `[data-mode="desk"]` and `[data-mode="room"]`;
- a `@media (prefers-reduced-motion: reduce)` block that sets the motion durations to `0ms`.

The output is deterministic: object keys are sorted and no timestamp is written. Do not edit `styles/tokens.css` by hand.

```bash
python3 scripts/build_tokens.py          # regenerate styles/tokens.css
python3 scripts/build_tokens.py --check  # exit 1 if the CSS is out of date
```

## The two modes

| Mode | Body text | Minimum target | Layout intent |
|---|---:|---:|---|
| **Desk** | 15 px | 32 px | Dense laptop view with private pupil labels. |
| **Room** | 32 px | 64 px | Projected view, seat codes instead of names, at most six pupils visible per page. |

Both modes share the same tokens. Only the mode values change, so the components keep their shape and behaviour when the teacher switches view. Room is a state of the Live lesson screen, not a separate product.

## Status is shape + label, never colour alone

Each status has a colour role, a distinct shape and a text label in `tokens.json`. The gallery repeats the shape and label beside every status so the meaning survives greyscale, low colour vision and a washed-out projector.

| Status | Shape | Label | Colour role |
|---|---|---|---|
| On track | circle | On track | `status-ok` |
| Stuck | triangle | Stuck | `status-stuck` |
| Idle | square | Idle | `status-idle` |
| Not started | dashed circle | Not started | `status-not-started` |

The contrast table checks the colour layer only. It is a design check, not a claim that the interface is compliant.

## Focus and motion

- The focus ring uses `--focus-width` and `--focus-offset` from the tokens; it is never removed.
- Motion uses the duration tokens and the shared easing token.
- With `prefers-reduced-motion: reduce`, durations become `0ms`, transitions are removed and the loading skeleton becomes static.
- The gallery is static HTML/CSS. It works without JavaScript; both modes are shown side by side.

## Contrast

`scripts/contrast_table.py` computes WCAG 2.x relative-luminance contrast ratios for every text and status colour against `bg` and `surface` in both modes. Normal text is checked at 4.5:1, large text at 3:1, and non-text UI used as the only indicator at 3:1.

Room mode marks its body text as large, so the large-text target applies to its text and status-label pairs. Desk mode uses the normal-text target. **AA is treated as a design target here, not a compliance claim.** If a pair fails, adjust the colours in `tokens.json`, not the thresholds.

```bash
python3 scripts/contrast_table.py          # writes docs/design-system/contrast.md
python3 scripts/contrast_table.py --check  # exit 1 if the table is out of date
```

## Run the checks

```bash
python3 scripts/build_tokens.py
python3 scripts/contrast_table.py
python3 -m unittest discover -s tests -v
```

The tests cover the contrast function, every required contrast pair, the two mode scales, the status shapes and labels, and the generated CSS being up to date.

## What is not here

- No interactive prototype and no clickable lesson board yet.
- No reusable component library or package.
- No dark theme.
- No compliance or legal claim. Accessibility is shown as a design target checked on these screens.
