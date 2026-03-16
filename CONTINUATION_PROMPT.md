# Continuation Prompt — Kilo TT E-Bike Build

## What to do NOW

The build bible HTML (`kilo-tt-ebike-build.html`) was heavily restructured this session. **Priority for next session: open the HTML in a browser and visually QA the page.** Specific checks:

1. **Progress bar JS** — Checkbox IDs all changed from `m1a`/`ea1`/`c1a` style to `s1a`...`s18b`. The `localStorage` keys use `'kilo_' + cb.id`. Old keys are now orphaned. The progress counter should still work (it counts all `input[type="checkbox"]`), but any previously checked items will appear unchecked. Verify the bar updates when you check/uncheck items.

2. **Collapsed "Already Done" section** — Uses a `<details>/<summary>` element. Confirm it renders correctly, opens/closes, and the disabled checked checkboxes display properly.

3. **Wiring reference diagrams** — The ASCII box-drawing diagrams (throttle signal chain, battery power path) use monospace `<pre>`-like rendering inside `.diagram` divs. Confirm they're not wrapping or misaligned on your screen width.

4. **Clutch bench-test consistency** — Every mention of clutch decoupling should now say "verify via bench-test" or "pending bench-test" or "expected." Grep for `BBSHD clutch` and confirm no unqualified fact-statements remain.

5. **Speed sensor** — Should consistently say "omitted by choice" or "approximate" everywhere. No more "Wheel sensor needed" or "Optional but Recommended."

### If QA passes, next physical build steps are:
- Step 1: Swap stock BB for BBSHD
- Step 2: Mount 42T chainring, 20T fixed cog, clutch bench-test
- Step 3: Shorten chain

## Session Commits

```
3c41d3f docs: reorganize ebike build checklist and correct drivetrain assumptions
```

Major changes in this commit:
- 3 separate checklists (mech/elec/commissioning) merged into 18-step sequential assembly flow
- 36T freewheel demoted to spare; 20T fixed is primary (pedalability math: 42/36 = spin-out)
- All clutch claims made conditional (pending bench-test)
- Hub threading corrected (both sides 1.37x24, flip wheel to switch cogs)
- "Phase Runner" renamed to "Baserunner V6 Z9"
- Speed sensor unified as "omitted by choice"
- Anti-lug tuning added (tall 42/20 gearing = high phase current at low RPM)
- Phase wire connectors = Anderson Powerpoles (user's actual setup)
- Dedicated wiring reference section with ASCII diagrams added
- BMS fault triage restored to full list
- Alternate HTML files (gpt, opus) deleted

## Key Design Decisions (settled this session)

| Decision | Rationale |
|---|---|
| 20T fixed primary | Only pedalable ratio with 42T BBSHD chainring (42/36 confirmed spin-out) |
| 36T freewheel = spare | On opposite hub side, flip wheel to use. Fallback if clutch bench-test fails |
| No PAS sensor | Throttle-only build, 6-pin PAS capped |
| No regen | BBSHD clutch expected to prevent engine braking (pending bench-test) |
| No speed sensor | Rider goes by feel, ~15mph soft target, display speed approximate |
| Anderson Powerpoles | Already on phase wires, verify 45A-rated |
| Solder + heatshrink | Hall/temp wires, staggered splices, adhesive-lined |
| Anti-lug tuning | 42/20 tall gearing → high phase current at low RPM → soft throttle ramp, conservative limits |

## Key Paths

- **Build bible**: `kilo-tt-ebike-build.html` (sole HTML file, 1328 lines)
- **Research doc**: `deep-research-report.md`
- **Component spec**: `ebike-component-spec.md`
- **Memory**: `.claude/projects/C--Users-ColsonR-bicycle/memory/project_build_philosophy.md`

## Environment

- Platform: Windows 11, Git Bash
- Repo: `github.com/robjohncolson/bicycle` (main branch)
- No build tools, no tests — this is a hardware documentation repo
- Latest commit: `3c41d3f`
