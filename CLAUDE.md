# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hardware documentation repository for a DIY e-bike build: a 63cm Mercier Kilo TT fixed-gear frame converted to a mid-drive e-bike using a Bafang BBSHD motor, Grin Baserunner V6 Z9 controller, Superharness + SW102 display, and a custom 14S4P 18650 battery pack with a JK smart BMS. The repository contains the full build bible, research docs, component specs, wiring references, manufacturer PDFs, and assembly photographs.

**Warning**: This build involves high-voltage electronics (~52V nominal, 58.8V full charge) capable of delivering 40A continuous and 60A peak current. All documentation includes critical safety warnings.

## Repository Purpose

This is NOT a software project. It's a knowledge repository for:

- Complete e-bike build checklist (18 sequential assembly steps: mechanical + electrical + commissioning + tuning)
- BBSHD mid-drive integration with Baserunner V6 Z9 controller (phase/Hall wiring, Autotune)
- 14S4P 18650 battery pack assembly with JK BMS wiring and Bluetooth commissioning
- Throttle-only signal path via Superharness + SW102 display (no PAS, no regen, no speed sensor)
- Safety guidelines for high-voltage battery construction and first power-on

## Key Technical Specifications

- **Frame**: Mercier Kilo TT 63cm (fixed-gear / track conversion)
- **Motor**: Bafang BBSHD mid-drive (Anderson Powerpole phase wires)
- **Controller**: Grin Baserunner V6 Z9 (sinusoidal FOC, 60V max, 40A continuous)
- **Battery**: 14S4P 18650 Sony/Murata VTC6 (~12 Ah / 624 Wh), ~52V nominal, 58.8V full charge. Cell-level headroom 120A cont / 240A peak — BMS and controller are the bottlenecks, not the cells.
- **BMS**: JK-BD4A17S4P smart BMS (Bluetooth, active balance, common-port, 40A cont / 60A peak)
- **Drivetrain**: 42T chainring / 20T fixed cog primary, 36T freewheel spare on flip side
- **Display**: SW102 via Superharness (KM5s protocol)
- **Throttle**: DYOL half-twist bidirectional (forward = accel, reverse = regen signal). Regen bench-verified 2026-04-23: electrically active when motor spins under power (trips bench supplies that can't sink regen current). Pure-coast regen still expected non-functional (BBSHD clutch disengages). Set to 0A for commissioning; optionally re-enable at ~5A on-bike.

## Documentation Structure

### Primary Documentation

- **`kilo-tt-ebike-build.html`** — the build bible. Single-file HTML with embedded CSS, 18-step assembly checklist (progress-tracked via localStorage), spec tables, ASCII wiring diagrams, battery assembly photo gallery, and safety callouts. **This is the canonical source of truth.** Open in a browser to use.
- **`deep-research-report.md`** — research on BBSHD + Baserunner integration, clutch/regen behavior, thermal considerations
- **`ebike-component-spec.md`** — component-by-component spec sheet with model numbers and sourcing notes
- **`CONTINUATION_PROMPT.md`** — session handoff document. Read this at the start of a new session to understand current build state, open decisions, and immediate next actions.

### Supporting Materials

- **5 JPEG images** (`188492-*.jpg` through `188497-*.jpg`) — battery pack assembly reference photos. Sourced from Endless Sphere thread #118426 ("14S4P in linear configuration, BMS balance and copper-nickel sandwich"). Attribution is inline in the HTML photo gallery.
- **Manufacturer PDFs** — Baserunner V6, Superharness, Bafang BBSHD / BBS02, BBSHD→Z9 wiring reference, power supply manuals

## Working with This Repository

### The build bible is authoritative

When build details conflict between `kilo-tt-ebike-build.html` and any other file (including this one), the HTML wins. If you change a build decision, update the HTML first, then propagate to `CONTINUATION_PROMPT.md` and any other affected docs.

### LocalStorage-backed checkboxes

Checkbox IDs follow `sNx` where N is the step number (1–18) and x is a sub-letter. Keys are `'kilo_' + cb.id`. Renaming or removing checkbox IDs orphans any previous check state in the user's browser — avoid churning IDs unless there's no state to lose.

### Adding documentation

When adding new documentation:

1. Prefer editing `kilo-tt-ebike-build.html` over creating new files
2. Maintain focus on hardware assembly, safety, and commissioning
3. Include clear warnings for any high-voltage procedures
4. Use the existing `.diagram`, `.callout`, `.spec`, and `.checklist-section` classes for visual consistency
5. Add verification checkboxes for critical assembly steps

### Image management

- Store assembly photographs with descriptive filenames
- Keep image files under 500KB each
- Reference images in the HTML photo gallery, including attribution if sourced externally

### Safety documentation requirements

All documentation involving battery or motor assembly must include:

- Voltage hazard warnings (~52V is dangerous)
- DMM verification steps before any power-up or connector mating
- Insulation requirements and one-hand-rule callouts for live connections
- Proper wiring sequence to prevent shorts
- Charger-first BMS activation note (JK BMS needs charger V > pack V + ~2V to wake)

## Git Workflow

- Main branch for all documentation updates
- Conventional commit format (`feat:`, `fix:`, `docs:`) as appropriate
- Commit messages should clearly describe what was added or modified

## Common Tasks

### Updating build steps

Edit `kilo-tt-ebike-build.html` directly. Preserve checkbox IDs where possible to retain user progress state.

### Updating wiring documentation

Edit the "System Topology" and "Baserunner V6 Z9 → BBSHD Wiring Reference" sections in the HTML. Both the compact POWER PATH diagram and the ASCII BATTERY POWER PATH diagram must be kept consistent when details change.

### Adding assembly photos

Place new images in the root directory with descriptive names. Update the photo gallery section in the HTML to reference them, including forum attribution if sourced externally.

### Session handoff

Update `CONTINUATION_PROMPT.md` whenever significant decisions or state changes occur. It should reflect what's done, what's in progress, any HTML deviations not yet written back, open decisions, and immediate next actions.

## Important Safety Context

This build deals with:

- High voltage (~52V nominal, 58.8V full charge) capable of causing injury
- High current (40A continuous, 60A peak) requiring proper gauge wiring
- Lithium-ion cells that can cause fires if mishandled
- Spot welding procedures requiring protective equipment
- Pack+ wires that become live hazards the moment they land on the pack
- BMS FET body diodes that can cause false polarity readings when the BMS is asleep
- No main fuse in this build — BMS OCP is the only overcurrent protection

Always prioritize safety information in documentation updates. Never advise a build step that puts the user in a position where a single fault could become a dead short or a fire.

## Non-Standard Build Decisions

The user has deviated from common e-bike build conventions. These are intentional and documented in `kilo-tt-ebike-build.html`:

- **No main fuse** — BMS OCP only, slower than a fuse and requires BMS awake
- **Anderson Powerpoles (not XT90-S) on discharge** — loses inrush precharge; contacts will arc slightly on first mate each ride
- **Y-split pack output** — Powerpoles (discharge) + XT60 (charge) both tie to Pack+ (N14) and BMS C-
- **Commission BMS pre-wrap** — step 8 includes Bluetooth cell-count setup and fault verification before the pack is sealed in step 9
- **Throttle-only** — no PAS, no speed sensor. Regen bench-verified capable 2026-04-23 when motor is under power (not inert as originally assumed); set to 0A for commissioning, optionally re-enabled at low current on-bike for descent braking. Pure-coast regen still expected non-functional.
- **Floating battery negative** — NOT bonded to frame. E-bike system is single-fault tolerant only while kept floating.
