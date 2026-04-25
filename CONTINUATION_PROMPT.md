# Continuation Prompt — Kilo TT E-Bike Build

## Update (2026-04-24) — Original JK BMS Bricked, Swapping to Spare 200A JK

Full 3-test diagnostic completed. Verdict: **original JK BMS is bricked at the MCU / FET-driver level.** Hardware around it is fine.

**Diagnostic results (final):**

| Test | Result |
|---|---|
| Heavy lead joints (B+, B-) | ✅ Verified clean (B+ 0.1Ω; B- continuity 48.4V end-to-end) |
| Test 2 — P1 voltage at MCU | ✅ Staircase 3.4V → 48V, all balance wires good, MCU has full power rail |
| Test 3 — discharge load (100W incandescent in series with DMM ammeter) | ❌ **4 mA** at 48V (expected 700–1000 mA). FETs not conducting; current is body-diode/parasitic leakage only |
| BMS button: 1-sec tap + 5-sec long press | ❌ No ammeter spike, no LED, no Bluetooth, nothing |
| Charger-wake attempt 2 (Matrix 58.8V CV / 2A CC into XT60, polarity verified) | ❌ Matrix ammeter held at 0.00A for 30s, BLE silent |

MCU has every condition it needs to boot and respond — full power rail, working button input, working charge-side reference — and produces zero response on any axis. Not recoverable without component-level repair, which is not worth the time when a free replacement is on hand.

**Action: swap to spare 200A JK BMS.**

Logistics confirmed:
- Spare 200A JK is physically accessible
- Current pack is lightly taped/glued, BMS is easy to remove without unwrapping
- Spare 200A JK is also 14S+ capable (pin compatibility expected; verify P1 pin pitch and count match before committing)
- Spare has dual B- / dual P- heavy leads (designed for parallel FET banks); for 40A application, use only one of each pair, cap the unused pair

**Swap procedure** (next session, immediate):

1. **Disconnect P1 balance harness from dead JK first.** This depowers the dead BMS and prevents transient voltage events on the balance side during heavy-lead rework.
2. **Disconnect heavy leads from dead JK** — screw terminals if present (unscrew), or desolder if soldered. The B- wire (from pack N0) and the C-/P- blue wire (going to Y-split → Powerpoles GND + XT60 GND).
3. **Connect heavy leads to spare 200A JK** — same B- and same C-/P-. **Cap the unused B- and unused P- terminals** with heat-shrink to prevent accidental shorts.
4. **Plug P1 balance harness into spare BMS.** Verify pin alignment first — JK BMS variants can differ in pin pitch and count. If P1 doesn't seat, may need to re-pin or rebuild the connector.
5. **Try charger-wake on the new BMS** — Matrix at 58.8V/2A into XT60, watch ammeter for current rise + BLE for advertise.
6. **Commission via Bluetooth**:
   - Set cell count = 14
   - Verify all 14 cell voltages reading ~3.43V each
   - Set protection thresholds (overvoltage, undervoltage, OCP, OTP — sensible defaults for 14S Li-ion)
   - Disable any default current that's wrong for 40A pack
7. **Re-run Test 3 (discharge load) with new BMS** to confirm FETs conduct.
8. **Hardware Inventory note**: original spare-for-future-build is now in service. The "future high-current build" no longer has a BMS earmarked.

**Still deferred until BMS swap completes:**
- Copper strip reinforcement (B-/B+ pads). Plan stays the same: Option B (copper alongside existing leads) for B-, either option for B+. Ferrule-flatten technique for wire termination.
- Thermistor install on new BMS's P3.
- Button connector decision (external vs. capped).
- Pack wrap.

### Two-pack strategy (2026-04-24, decision)

User has a second 14S4P pack (Samsung high-drain 21700 cells) physically built — cells stacked, nickel welded, balance harness soldered — but no BMS commissioned yet (Scenario B in our earlier triage). Strategy split:

| Pack | Cells | BMS | Status | Timeline |
|---|---|---|---|---|
| **Pack A** (current build) | 14S4P 18650 VTC6 (12 Ah / 624 Wh) | **Spare 200A JK** (in hand) | Plug-and-play swap pending P1 pin compatibility check | This session |
| **Pack B** (future) | 14S4P 21700 Samsung high-drain (~16–20 Ah / 832–1040 Wh) | **Daly common-port 14S 60A** (Amazon B0CZQJ6G39, ordered, arrives Thursday 2026-04-30) | Full commissioning workflow when Daly arrives | Thursday + 1–2 days |

**Rationale**: 18650 pack is 90% built, plug-and-play swap is the fastest path to riding. Daly is right-sized for the Z9 system (30A continuous controller bottleneck means 60A BMS gives 50% headroom — appropriate). Doing one commissioning at a time beats parallel commissioning across two packs. Original 200A "earmarked for future high-current build" plan flexes — for the current Z9 system, 200A on the 18650 is harmless surplus and saves a week of waiting.

**Order tonight (2026-04-24)** before sleep: Daly listing variant verification —
- Cell count: **14S** (not 13S)
- Chemistry: **Li-ion** (not LiFePO4)
- Current: **60A**
- Topology: **common-port** (two heavy leads, not three)
- Prefer **smart/Bluetooth variant** if available at same listing (~$10–20 premium worth it for diagnostic capability)
- Seller: **DALY Official** or reputable reseller

### Pre-swap verification — DRY-FIT P1 BEFORE COMMITTING

Before disconnecting anything from the dead JK, **dry-fit P1 against the spare 200A's balance socket**:
1. Pin **count** matches?
2. Pin **pitch** matches (2.54mm vs 2.0mm — close-but-different will appear to fit but won't seat)?
3. Pin **orientation** matches (B- and B14+ on the same physical sides)?

If yes → genuine plug-and-play, proceed with swap.
If no → P1 needs re-pinning to new connector geometry. ~1 hour with crimper + new pins. Stop and re-plan before committing.

### After 18650 commissioning — set 21700 work for the Daly arrival

While waiting for the Daly:
- 21700 pack pre-flight: heavy lead pull tests, voltage verification, balance harness staircase. **Do this proactively before the Daly arrives** so commissioning day is uninterrupted.
- Don't install the Daly until it physically arrives — no point speculating on its connector geometry.

---

## Update (2026-04-23, evening) — Heavy-Lead Verification Complete, BMS Wake Still Blocker

Copper strips arrived. Before reinforcing, did a full DMM verification pass on existing heavy leads to decide which joints need rework.

**Heavy-lead verification results:**
- **B+ / Pack+ at N14 path**: resistance 0.1Ω after subtracting 0.3Ω DMM lead resistance. **Clean. No rework needed.**
- **B- wire continuity**: Pack N14 to N0 directly = 48.39V; Pack N14 to B- wire at BMS end = 48.4V. **B- wire has full continuity from N0 all the way to the BMS terminal. Solder joint is GOOD.** Earlier suspicion that B- had failed again was wrong — voltage anomaly is BMS-internal, not joint-related.
- **Powerpole V+ to GND reads 41V** (not 48V). Exact leakage-artifact signature from the original BMS wake failure. Voltage drop is across BMS internals (off-state FETs / body diodes), confirming MCU is not running and FETs are not enabled.

**DYOL blue-blip reinterpretation:** when Powerpoles were connected to the bike earlier, DYOL lit blue for one instant then died. Originally thought this meant BMS briefly conducted. Actually almost certainly a **capacitor discharge transient** — residual charge in Baserunner input caps from the earlier bench-supply session drained through the Superharness → lit throttle for a moment → gone. Not a BMS conduction event. BMS is still dead-to-the-world.

**Copper strips now deferred** until BMS is sorted. No point reinforcing pads on a pack that can't power a load. When time comes: B- gets Option B (copper *alongside* existing lead — don't re-reflow the known-vulnerable joint since verification now confirms it's holding); B+ either option.

**Ferrule-crimp trick for heavy-lead termination** (when copper-strip pass happens): user has ferrules + crimper. Plan: crimp ferrule on wire, **flatten with pliers/vise** to convert cylindrical ferrule into a flat tinned-copper pad, then solder the flattened pad flat to the copper strip. Functionally equivalent to a ring lug, uses parts already on hand.

**Critical next-session action: Test 2 of the original 3-test diagnostic — P1 balance harness voltage check.**

The MCU gets its power from the P1 balance connector (B14+ and B- sense lines), not from the heavy leads. If P1 is loose or a balance wire has failed, MCU won't boot no matter how healthy the heavy leads are.

Procedure:
1. **Reseat P1 firmly** (unplug, inspect pins for bend/debris, re-seat until latched).
2. DMM across P1 on BMS side: red probe P1 pin 15 (B14+), black probe P1 pin 1 (B-). Expect **~48V**.
   - **~48V** → MCU has power but still not booting. MCU may be dead or firmware locked. Proceed to Test 3 (discharge-side load test).
   - **0V** → P1 connector lost contact. Reseat, retry.
   - **Weird fraction (30V, 41V, etc.)** → balance wire(s) in chain have broken continuity. Probe N0→B1 (expect 3.43V), N0→B2 (6.86V), ... N0→B14 (48V). First mismatch = broken balance wire.
3. Touch BMS case — warm after 30s = MCU drawing some current; cold = MCU not running.
4. Short (1-sec) tap of BMS button — any status LED activity?

---

## Update (2026-04-23) — Baserunner Bench Commissioning Complete

Baserunner V6 Z9 fully commissioned on Matrix bench supply (50V, 5A limit). Independent of the ongoing JK BMS blocker.

**What got done today:**
- Connected Phaserunner Suite via USB (COM8). Discovery: Baserunner needs SW102 ignition to wake — battery voltage alone is not enough. Plug Superharness + press SW102 power button before expecting comms.
- Loaded Superharness default profile, saved as baseline.
- **Autotune complete** — Hall-to-phase mapping written. Motor responds smoothly and proportionally to throttle, zero cogging or stutter.
- **Regen finding (important, build-doc-affecting):** DYOL reverse twist triggered regen, which dumped current back onto the bench-supply rail and overvoltage-tripped the Baserunner. **Regen is capable on this build** during active-motor braking (contradicts original "clutch makes it inert" assumption). Updated `kilo-tt-ebike-build.html` and `CLAUDE.md` accordingly. Pure-coast regen still expected non-functional (clutch disengages, no rotor motion).
- Current plan: **Regen Current = 0A** for remaining commissioning (bench supplies can't sink). Option to re-enable at ~5A on-bike with Max Regen Voltage 57.6V for gentle descents.

**Copper-strip reinforcement plan:** copper strips ordered for widening B+ (N14) and B- (N0) heavy-lead solder pads only. Balance sense leads B1–B13 carry mA, don't need reinforcement and stiffening them risks stress risers on the nickel-cell welds. Technique: solder the copper on top of the nickel (spot-welders can't weld copper on a hobby rig anyway, plus live-pack safety). Per-joint drill: 60W+ iron, pre-tin both surfaces, heat-sink alligator clip on the nickel between joint and cell, in-and-out under 5 seconds, pull-test. For B- (already reworked once), prefer Option B: add copper *alongside* the existing lead rather than re-reflowing the known-vulnerable joint.

**Still blocked:** JK BMS wake (see original section below). Baserunner side is ready and waiting; pack is the only thing between you and a ride.

**Next-session priorities:**
1. Run the 3-test BMS diagnostic (polarity → P1 voltage → discharge-side load) to decide JK repair vs. Daly replacement.
2. Solder copper reinforcement strips to N0 and N14 (when strips arrive).
3. Throttle min/max calibration in Suite (cosmetic — defaults are fine, can tune when bike is on stand with pack).
4. Thermistor install + button-connector decision before wrap.

---

## Original State (2026-04-13)

**Phase:** Battery pack pre-wrap commissioning BLOCKED — JK BMS will not wake. Physically in the middle of step 8 (`kilo-tt-ebike-build.html`). Pack is NOT wrapped yet. Today's job is to definitively diagnose whether the JK is dead or salvageable.

### What's physically done

- BBSHD ↔ Baserunner Z9 phase/Hall wiring (prior sessions)
- 14S4P pack stack assembled
- Balance harness soldered to pack nodes, DMM staircase verified, **P1 plugged into JK BMS**
- P2 extension balance header intentionally **unplugged** (14S pack, firmware will ignore unused positions once cell count is set)
- **GND pigtail built**: BMS blue (P-/C-) → Y-split → Anderson Powerpoles GND + XT60 GND, both in housings
- **V+ pigtail built**: heavy-gauge red → Y-split → Powerpoles V+ + XT60 V+, both in housings
- **BMS B- (black) soldered to pack N0** — had to be **resoldered once**. Original joint was cold and failed continuity. This is a known-vulnerable spot; verify continuity before any future rework.
- **Pack+ soldered to pack N14**
- True pack voltage confirmed at ~48V (3.43V/cell, ~30% SOC) — 18650 VTC6s depleted slightly during the debug session

### What's NOT done yet (deferred when BMS wake failed)

- **Thermistors**: not installed yet. Must happen before wrap.
- **Button connector**: decision still pending (install external momentary or cap).
- **Charger-first BMS wake**: **FAILED** (see below).
- **Bluetooth pair + cell count = 14 setup**: blocked by wake failure.
- **Pack wrap**: blocked by wake failure (correctly — commissioning gate is holding).

## The Blocker — JK BMS Will Not Wake

Symptoms from yesterday's session:

1. **Charger (AFU AF6000, 58.8V 10A)** plugged into XT60: LED1 red (power on), LED2 **green immediately** (normally means "charged / idle"). Pack is at 48V, so green-at-48V is wrong.
2. **Matrix bench supply** set to 58.8V CV, output enabled: reports **0A current**. Pack isn't drawing anything.
3. **BMS case cold** — no MCU activity heat signature.
4. **Bluetooth scan silent** — JK app finds nothing.
5. **Button press** (onboard PCB button? external button?) — no response.
6. **DMM at Powerpoles** with charger off reads ~48V true pack voltage (not the earlier 41.85V leakage artifact — that was a symptom of the B- disconnect, now fixed).

The B- cold solder joint is definitively repaired (voltage reading now reflects real pack state). So the wake failure is somewhere else in the chain: polarity, charger output, firmware state, or a dead BMS.

## Immediate Next Actions — 3-Test Diagnostic

**Do not reorder, do not skip steps. Each test takes ~2 minutes and rules out a specific failure mode.**

### Test 1: Matrix bench supply polarity at the leads (60 seconds)

- Matrix output ON, leads **NOT connected to pack**
- DMM: red probe on the red banana lead, black probe on the black banana lead
- Must read **+58.8V** (positive)
- If negative → leads are swapped. Swap them and retry the wake test — this alone may solve it.
- Also confirm **current limit is set above 0A** (1–2 A minimum) and the **Output Enable button** is actually pressed (Matrix supplies have a separate enable button from the main power).

### Test 2: Balance harness voltage at P1 (30 seconds)

- DMM across the P1 connector pins on the BMS side:
  - Red probe: **B14+** (pin 15)
  - Black probe: **B-** (pin 1)
- Must read **~48V** (true pack voltage)
- If 0V or wildly off → P1 connector has lost contact (or a balance wire failed). Reseat P1. Without B-/B14+ voltage at P1, the MCU has no power and nothing else will work.
- If ~48V cleanly → MCU *should* be getting power. Proceed to Test 3.

### Test 3: Discharge-side load test (60 seconds) — THE DECISIVE ONE

- Disconnect the Matrix supply entirely
- Touch a **12V incandescent bulb** OR a **~100 ohm / 5W resistor** briefly (1–2 seconds) across the Powerpoles V+ and GND
- **If the bulb lights / resistor warms / DMM ammeter shows current** → discharge FET is conducting → BMS is alive on the discharge side. Run Bluetooth scan immediately after the load event (some JK firmware wakes on load). Even if charge-side is broken, a live discharge side means the BMS is salvageable.
- **If nothing, zero current, no glow** → both FETs non-conductive → BMS is bricked (dead MCU, dead FETs, or unreachable firmware lockout). Replacement time.

### Also worth doing: AFU charger sanity check (30 seconds)

Independent of the JK, the AFU's behavior yesterday was suspicious (green at 48V). DMM the charger output directly:

- Wall AC ON, XT60 **unplugged from pack**
- DMM across the XT60 pins on the charger pigtail
- Should read **~58.8V** (or whatever the labeled output is)
- If it reads 54.6V → it's a 13S/48V charger, not 14S — wrong charger for this pack
- If it reads ~48V or lower → charger has wrong CV setpoint, it's faulty
- If it reads 58.8V cleanly → charger is fine, the "green at 48V" was a symptom of the BMS blocking current, not a charger fault

Knowing this separately matters because if the JK is replaced, you need a working charger for the new BMS.

## Decision Tree Based on Test Results

| Test 1 | Test 2 | Test 3 | AFU Check | Conclusion | Next Action |
|---|---|---|---|---|---|
| Polarity wrong | — | — | — | User error, easy fix | Swap Matrix leads, retry wake. Update memory to note polarity caught us. |
| Polarity OK | P1 reads 0V | — | — | P1 connector loose | Reseat P1, retry wake. JK probably fine. |
| Polarity OK | P1 reads 48V | Load conducts | — | Charge-side fault only | JK salvageable — either buy time with bench-charging + app config via button/discharge wake, or replace if firmware charge-disable can't be fixed via app |
| Polarity OK | P1 reads 48V | Zero current | 58.8V correct | **JK is bricked** | Return/warranty JK, order Daly replacement |
| Polarity OK | P1 reads 48V | Zero current | Charger wrong | JK possibly bricked + charger wrong | Replace both, new build with a known-good Daly + a known-good 14S charger |

## Open Decisions (waiting on you)

1. **Daly replacement BMS** — Amazon listing `B0CZQJ6G39` ("DALY 4S-16S BMS 15A-200A Protection Board with Balance Wire and Temperature Sensor, Li-ion 14S 48V 60A"). Needs variant-selector verification before ordering:
   - Cell count dropdown must say **14S** explicitly (not 13S)
   - Chemistry **Li-ion** (not LiFePO4)
   - Current **60A**
   - **Common port** topology (two heavy leads out, not three)
   - **Non-smart / standard** (no Bluetooth) — listing doesn't mention Bluetooth, presumed good
   - Seller should be **DALY Official** or a reputable Daly reseller; avoid random third-party
   - Temperature sensors included in box (listing says yes)
   - Paste listing title, currently-selected variant, seller name, and price into the next session for verification — Amazon blocks programmatic page access.

2. **HTML + CLAUDE.md Baserunner current limit correction** — pending. Baserunner V6 Z9 manual (page 2 of `Baserunner_V6_Manual_Rev0.pdf`) authoritatively states **30 A continuous / 55 A peak phase** on the Z910 motor cable, and the factory default in the Phaserunner Suite is **30 A Max Battery Current** (page 12, section 6.4). Current `kilo-tt-ebike-build.html` says "40A continuous" in the spec table and step 16a references "JK BMS 40A" as the system bottleneck — both wrong. The real bottleneck is the Baserunner Z9 at 30A, NOT the BMS at 40A. Fixes ready to apply:
   - `kilo-tt-ebike-build.html` spec table row 731 + 734: add Baserunner phase/battery current row (30/55 A), clarify that Baserunner is the system bottleneck
   - `kilo-tt-ebike-build.html` step 16a: reword from "well below JK BMS 40A continuous" to "at or below Baserunner Z9 factory default 30 A (start ~15–20A and ramp)"
   - `kilo-tt-ebike-build.html` step 16d: emphasize 55 A phase peak under anti-lug conditions since battery side is now the tighter limit
   - `CLAUDE.md` Key Technical Specifications: change Baserunner line from "40A continuous" to "30A continuous phase / 55A peak / 30A default battery current (Z9 variant)"
   - Say "yes update" to push these.

3. **Thermistor count** — how many NTC probes do you actually have on hand? 1, 2, or 4? Placement plan depends on count. Still needed before wrap.

4. **Button connector** — install external momentary on the battery bag exterior, or cap and tuck inside wrap? Decision not made.

5. **14S8P future pack via combining** — you have a second 14S4P pack (21700 cells, separate from this build's 18650s) and the 200A JK BMS. Floated combining 18650 + 21700 into a 14S8P. **Gentle flag raised**: mixing cell formats at the parallel-group level has drawbacks (mismatched internal resistance, capacity, aging). Deferred for a rested conversation. Not blocking anything for the Kilo TT build.

## Hardware Inventory (for future reference)

See `memory/project_hardware_inventory.md`:
- Spare JK BMS, 200A capable (dual B- / dual P- heavy leads) — earmarked for a future high-current build, not this one
- Second 14S4P pack, 21700 cells — separate from current build, combination into 14S8P flagged with cell-mixing caveat

## Safety Rails (still current)

- **B- heavy lead cold solder joint was the initial failure mode.** Any future heavy-lead rework must get the pull-test treatment (firm tug on the wire — if it moves, redo). Use a 60W+ iron, pre-tin both surfaces, apply heat to the work (not the solder), let cool undisturbed 3–5 seconds. A cold joint wrapped inside a sealed pack will fail from vibration in service and brick the pack.
- **JK BMS color convention on heavy leads** (verify by silkscreen or continuity): black = B-, blue = P-/C-. Both on the negative side. Pack+ runs direct from N14 to load, not through BMS.
- **Powerpoles have no precharge** — first mating each ride arcs slightly into Baserunner input caps. Accept contact wear or add external precharge later.
- **No main fuse** — BMS OCP only. Slower than a fuse, requires BMS awake. Tradeoff accepted.
- **Floating battery negative** — NOT bonded to frame. E-bike single-fault tolerant only while floating.
- **DMM polarity reference** = Pack+ vs pack N0 / B- directly, NOT vs BMS C- (asleep BMS floats C- via FET body diodes, gives false reversed readings).
- **Pre-wrap commissioning gate is holding for a reason** — yesterday's cold-joint catch is exactly what it exists for. Do not wrap until BMS is verifiably alive and configured.

## Key Paths

- **Build bible**: `kilo-tt-ebike-build.html` (canonical source of truth, note line 744 forum attribution)
- **Research**: `deep-research-report.md`
- **Component spec**: `ebike-component-spec.md`
- **Baserunner manual**: `Baserunner_V6_Manual_Rev0.pdf` — section 2 has motor cable current ratings, section 6.4 has battery limits, section 12 has specifications
- **Forum source** (battery photos + copper-nickel technique): https://endless-sphere.com/sphere/threads/14s4p-in-linear-configuration-bms-balance-and-copper-nickle-sandwich.118426/
- **Amazon Daly candidate**: https://www.amazon.com/dp/B0CZQJ6G39

## Environment

- Platform: Windows 11, Git Bash
- Repo: `github.com/robjohncolson/bicycle` (main branch)
- Hardware documentation repo — no build tools, no tests

## Pick a Thread

First-thing-today priority: **run Tests 1, 2, 3** on the JK BMS before doing anything else. If any of them reveal a non-dead-BMS failure (polarity, loose P1, or discharge-side conducting), don't order the Daly yet. If all three confirm the BMS is bricked, return/warranty the JK and paste the Amazon Daly listing details for verification before ordering.

Everything else (HTML fixes, thermistor install, button decision, 14S8P discussion) can wait until the BMS path is resolved.
