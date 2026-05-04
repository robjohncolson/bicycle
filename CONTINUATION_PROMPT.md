# Continuation Prompt — Kilo TT E-Bike Build

## Update (2026-05-04) — RIDE TEST: hills conquered, but SLAM-STALL appears; throttle ramp suspected

**Took the bike out today on the new tune. Hills are confirmed conquered** — the 30A battery / 55A phase ceiling did the job. But a new symptom surfaced: **if you slam the throttle to full from rest, the motor cuts out.** Has to be eased in gently from zero. Once moving, throttle is fully usable.

**Critical diagnostic info captured:**
- **The cutout AUTO-RECOVERS** (release throttle, re-twist, motor works). Does NOT require battery disconnect/reconnect.
- → This rules out Daly OCP latch (latch would require disconnect to reset).
- → This is a **controller-side protection trip**, not BMS.

**Working hypothesis: Throttle Ramp Up Rate is too aggressive (or absent).** Slamming throttle commands an instant 0→100% torque step; current control loop overshoots → controller trips itself. Auto-recover is consistent with Baserunner internal fault behavior.

**Secondary suspect: Low Voltage Rolloff Start may be at default (likely too low).** Pack sag at instant 30A draw can transiently dip pack voltage below the 42V LVC. Without LV rolloff acting as a soft taper above LVC, the cutoff is a cliff — any transient sag below 42V = instant cut.

### Next-session priorities (work-laptop pickup, where Phaserunner Suite + connected Baserunner are)

**1. Find and set Throttle Ramp Up Rate.** Naming varies by Suite version — look for one of:
   - "Throttle Ramp Up Rate"
   - "Throttle Smoothing"
   - "Acceleration Time"
   - "Throttle Filter"

   Likely in the **Throttle** tab already explored, possibly in **Advanced** or **Motor** tab.

   **Set to ~0.4 seconds for 0→100%** as starting point. Unit conversions if the field uses something else:
   - Seconds → 0.4
   - Milliseconds → 400
   - V/s (rate of change) → (3.6 − 1.05) / 0.4 ≈ **6.4 V/s**
   - %/s → 250

**2. Read out current Low Voltage Rolloff Start value.** Ideally should be ~45V (3V above the 42V LVC) so power tapers gracefully under sag instead of cliff-cutting. If at factory default, will likely need adjustment.

**3. Bench test first.** Motor on stand, slam throttle from zero: should now ramp to full in ~half a second instead of jumping. If bench passes, ride-test the slam.

**4. If slam-stall persists after ramp adjustment** → try lowering LVC from 42V to 40V (14S × 2.86V) to give sag headroom. Daly cell-level UVP still protects against true over-discharge.

**5. Pack voltage at rest after the ride** — measure with DMM at Powerpoles. This tells us roughly where the pack's SOC sits and whether sag-into-LVC is plausible.

### What's confirmed working from yesterday's tune (2026-05-03)

- **Hills conquered.** 30A/55A ceiling did the job.
- **Reverse twist is dead.** No regen, no fault, no torque — fully a dead zone.
- **Forward throttle is much punchier** than before — when it doesn't trip on slam.
- **No Daly OCP latch incidents** during this ride. 30A continuous controller cap is well clear of 60A BMS limit.

### State of the build (unchanged from 2026-05-03 update below)

- New fork installed, front end solid.
- 21700 + 200A JK still deliberately on hold. Kilo TT 18650 + Daly is active platform, accumulating ride hours.
- Baserunner direct-USB JST port still bent-but-working. Config saved to file as backup. Future: foam-tape protect the port.
- Superharness TTS port confirmed does NOT carry Phaserunner comms — direct port is the only path.

---

## Update (2026-05-03) — PHASERUNNER SUITE TUNING COMPLETE; new fork installed; reverse-twist regen disabled

**Bike has been ridden over the past week, runs well.** Today's session: full Baserunner V6 Z9 retune via Phaserunner Suite. Reverse-twist regen requested gone (rider preference — "doesn't matter which way you flick the throttle, it goes" minus the regen-on-reverse behavior). New fork installed (replaces the cut-too-short steerer issue from 2026-04-26). Holding off on 21700 commissioning for a bit longer — Kilo TT 18650 build is the active platform.

### Phaserunner Suite connection — Superharness TTS does NOT carry comms

- Tried connecting via the **TTS port on the Superharness** first. **It does not route to the Baserunner serial pins on this hardware.** Either the Superharness variant in this build doesn't break out comms, or the TTS port is a CA3 (Cycle Analyst) breakout with a different pinout — same physical JST, different signals. Phaserunner Suite cannot talk through it.
- Working comms path: **direct USB-TTL into the small JST port on the Baserunner controller body.**
- **Baserunner direct port slightly bent** from being wedged near the motor. Currently functional but fragile. **Saved config to file as backup** so if the port dies, settings can be flashed to a replacement Baserunner without redoing the tune. Future: tape foam around the port area to keep it from getting squeezed against the motor again.

### Settings changed (all written + saved)

| Setting | Was | Now | Rationale |
|---|---|---|---|
| Low Voltage Cutoff | **19.5V** | **42V** | Old value was a 6S default — would have allowed cell-destroying over-discharge. 42V = 14S × 3.0V/cell, BMS now never has to act as primary protection. |
| Max Regen Battery Current | 7A | **0A** | Kills regen entirely. Reverse-twist now does nothing. |
| Max Battery Current | 14A | **30A** | Was capping power at ~700W. 30A is the Z910 cable hard ceiling. |
| Max Power Limit | 700W | **1800W** | Was the actual binding limit (14A × 48V ≈ 700W). 1800W keeps Max Battery Current as the active cap. |
| Max Phase Current | 46A | **55A** | Bumped straight to Z9 phase peak (skipped 50A intermediate step). User comfortable with the jump. |
| Throttle Start Voltage | 1.2V | **1.05V** | Just above measured rest of 0.98V — clean zero, no ghost-throttle. |
| Throttle Max Voltage | 3.5V | **3.6V** | Just below measured forward max of 3.7V — full range usable. |
| Throttle Fault Range | 0.8V | **1.5V** | Old value was triggering fault on reverse twist (0.04V below 0.4V threshold). Widened so reverse twist is silent — accepts the tradeoff that low-side fault detection is now disabled (broken throttle wire grounding to 0V can't be distinguished from normal reverse twist). |

**Throttle voltage measurements (DYOL bidirectional):**
- Rest: **0.98V**
- Full forward: **3.7V**
- Full reverse: **0.04V**

**Settings left unchanged:**
- Max Regen Voltage 59.5V (correct — pack peaks 58.8V at full charge, 0.7V regen-cutoff headroom)
- Brake Start 0.85V / Brake Max 0.1V (these are the ebrake input wire — inverse-logic Hall sensor settings — unrelated to throttle reverse-twist; left alone since no ebrake sensor wired)
- Deadband Threshold 0
- Plug braking: **disabled** (BBSHD clutch disengages on coast → no kinetic energy to dissipate; also would re-introduce the reverse-twist-does-something behavior we just removed)

### Fork — replaced

New fork installed (replaces the cut-too-short steerer that produced "not rock solid" front end). Specifics not noted this session — assume Soma Corsa chrome 1" threaded 230mm per the prior plan unless follow-up reveals otherwise. **JIS vs ISO headset verification + upper stack measurement no longer blocking** — fork is in.

### 21700 commissioning — still on hold (deliberate)

Kilo TT 18650 + Daly drivetrain is the active build. 21700 + 200A JK still shelved, cells stacked + nickel welded but no balance harness installed. Resume later (no committed date this session). Mamachari sleeper-build pivot from 2026-04-27 (in `project_mamachari_sleeper_build.md`) is the longer-term context for what the 21700 will eventually power.

### Next-session priorities

1. **Test ride with new tune** — reverse twist should be a dead zone, forward should feel notably more punchy now (30A vs 14A battery limit, 55A vs 46A phase). Hand-temp motor casing after the local hill climb to confirm thermal margin at the new phase ceiling.
2. **Re-test the cutout hill** on 36T cog — 30A continuous is well below the Daly's 60A OCP, expect zero cutouts now.
3. **Tape foam/protection around the Baserunner direct comms port** to prevent further mechanical damage. Port works now but is the only viable comms path.
4. **Ride the bike, accumulate run-time data**, defer 21700 commissioning until Kilo TT proves itself over weeks of normal use.

---

## Update (2026-04-26, evening) — FIRST RIDE COMPLETE; lug cutout characterized; fork replacement planned

**Bike is rideable.** Motor drop damage straightened **with a chisel from the side** (no wedge needed — wedge + C-clamp will be returned when they arrive). First ride happened today.

### Hill behavior — characterized and partially mitigated

- **42-22 (small rear cog) on local hill: full power cutout, required battery disconnect/reconnect to restore.** Latched protection trip. Diagnosed as **Daly OCP latch** — BBSHD lug current at low cadence on a steep grade exceeded 60A momentarily; Daly common-port FETs latched open and required full disconnect to reset.
- **Switched to 36T larger rear freewheel cog → no more cutouts on the same hill.** Hill is still physically hard, but the bike no longer cuts out. Bigger cog = more reduction = lower battery current under lug, stays under Daly's 60A ceiling.
- This is **empirical confirmation** that the BMS sizing assignment (200A→21700 production, Daly→18650 practice) was the right call. On the future 21700 build, lug spikes will rollback at the Baserunner (auto-recovers, no full cutout) instead of latching at the BMS.

### Z9 ceiling correction (important — overrides earlier suggestion)

- Baserunner V6 Z9 with Z910 motor cable is rated **30A continuous battery / 55A peak phase**. The 30A limit comes from the **Z910 cable**, not the controller — cannot be exceeded safely.
- An earlier session-suggestion of "raise Max Battery Current to 40-45A for more torque" was wrong. **30A is the system ceiling.** Don't go above it.
- **Phase current is the only torque lever left** on this fixed-gear single-ratio (42-36) build. In Phaserunner Suite, raise Max Phase Current toward 55A in 5A steps, ride the hill between each, hand-temp the motor casing after each climb to watch for thermal margin.

### Fork replacement — required, planned

- Existing fork's threaded steerer was cut too short during prior install. Insufficient threads for proper top-race + locknut engagement → front end feels "not rock solid." Not fixable without replacement.
- **Crown-race-to-top-of-locknut measurement: 230mm.**
- Plan: **Soma Corsa, chrome, 1" threaded, 230mm steerer.** Specs: 366mm axle-to-crown (~9mm shorter than likely OEM 375mm — slight head angle steepening, acceptable), 42mm rake, 26.4mm crown race seat (**JIS** standard), 50mm of threads on the steerer, drilled for short/mid-reach brake caliper, chromoly. Chrome is the only color Soma offers — classic track-bike look on red-orange.
- **Verifications still required before ordering:**
  1. Confirm existing headset is **JIS** (26.4mm crown race seat) and not ISO (27.0mm). Measure or pull lower locknut and inspect.
  2. Measure **upper headset stack** (top of head tube to top of locknut) — must be ≤45mm so the 50mm of threads gives full engagement. Almost certainly fine on a 63cm frame but worth confirming.
- User has a thread cutter on hand → fallback is a long-steerer threadless steel fork (e.g., Surly Steamroller chromoly, 300mm) threaded down manually. Not needed unless Corsa is unavailable.
- Zero re-cut margin on the 230mm Corsa option (230mm needed, 230mm offered). Future stem-position changes will be constrained.

### Status of original packs

- **18650 + Daly**: rideable. First charge completed. Pack still not formally wrapped — that's fine, it's the practice pack; wrap when fully proven.
- **21700 + 200A JK**: still shelved. Cells stacked + nickel welded, no balance harness yet. Resume after fork swap and Phaserunner phase-current tuning are done on the 18650 build.

### Next-session priorities (in rough order)

1. **Fork verifications**: measure JIS vs ISO headset standard + upper stack height. Then order Soma Corsa chrome 230mm.
2. **Phaserunner phase-current tuning**: bump Max Phase Current from default toward 55A in 5A steps, ride hill, hand-temp motor casing.
3. **Fork swap**: pull old fork, install Soma Corsa, set headset preload, road-test.
4. **Return wedge + C-clamp** when they arrive (no longer needed).
5. **21700 commissioning**: resume after the bike is fully proven on the 18650.

---

## Update (2026-04-26) — Motor Drop Damage: Anti-Rotation Arm Gap Spread with DIY Oak Wedge

**Resolved 2026-04-26: chisel-from-the-side technique straightened the spindle housing without needing the wedge.** Wedge + C-clamp will be returned when they arrive. The plan below is preserved as a record of the field-repair approach in case similar damage recurs on a future BBSHD.

BBSHD was dropped at some point pre-install. Damage assessment after first attempt to mount on frame:

- **Spindle housing slightly bent relative to motor body** — pinched the gap where the anti-rotation arm seats. Bracket couldn't reach its mounting holes; arm wouldn't slide into the gap at all.
- Motor electrically functional; spindle rotates smoothly; bearings appear OK.
- **NOT bending the anti-rotation arm itself** — it must stay flat to grip the chainstay correctly. Fix is on the housing side.

**Field repair plan:** spread the gap 3mm using a DIY truncated hardwood wedge driven by a large C-clamp.

**Wedge spec:**
- Material: oak hobby board (1×3, ~$5 Home Depot)
- Length: 92mm (working-space constraint)
- Tip thickness: 0.55" (slides into 0.6" current gap)
- Thick-end thickness: 0.78" (target = current + 3mm spread + ~1mm overshoot for spring-back)
- Effective taper: ~3.6° — chosen for fine control on cast aluminum
- Width: ~15–20mm (matches gap depth perpendicular to spread)
- Both faces taped with electrical/painter's tape to protect casting finish

**Why DIY over off-the-shelf:** sharp-tipped wedges in 92mm length force a steep ≥11.7° angle. Truncated wedge with 0.55" flat tip lets the angle drop to 3.6° — much more controllable on cast aluminum where overshoot = crack. Off-the-shelf wedges always start sharp; can't buy this geometry.

**Process:**
1. C-clamp drives wedge in eighth-turns (not quarter-turns — 3.6° taper is shallow but cast aluminum is unforgiving)
2. Measure gap with calipers after each turn
3. Bright LED on inside corners of the gap to watch for crack initiation
4. Stop at 0.78" gap (overshoot for spring-back)
5. Release clamp slowly, measure relaxed gap, test-fit anti-rotation arm
6. **Verify spindle still rotates smoothly after spread** — binding = bearing alignment shifted, back off immediately

**Why this is logged:** if drivetrain weirdness (chain drop, BB bearing wear, chainline drift) shows up in the next 6+ months, the motor drop + housing spread is the prime suspect. Future-you needs to know this happened.

**Status:** wedge not yet fabricated. Next session: Home Depot run for oak hobby board, fabricate wedge, execute spread, mount motor.

---

## Update (2026-04-25, evening) — 18650 + Daly ELECTRICALLY COMMISSIONED, First Charge In Progress

Daly install went plug-and-play. Pack is alive, motor spins on the real pack, charging now.

**What worked:**
- Daly P1 connector pitch matched the existing 18650 harness (both 2.0mm). No re-pin needed.
- Heavy leads joined via inline **PP30 Anderson Powerpoles** (matching the existing motor-side connectors) — replaced the brass connectors that were originally suspected as a JK culprit (probably weren't, but bad for 30A path regardless).
- **Color convention is FLIPPED on the Daly side:** **BLUE = B-, BLACK = P-** (opposite of JK convention). Sharpie note on the Daly recommended for future-you. Powerpoles wired blue-to-blue and black-to-black across the inline pair — internally consistent.
- **Daly is dumb — no app, no wake ritual.** Plugging P1 *was* the power-on. FETs enabled instantly, Powerpoles went from 1.6V leakage (FETs off) to 48V real (FETs conducting) the moment the balance harness seated.
- Hooked to Z9 → motor spins smoothly under throttle.
- **Regen blip on real pack: no downside.** Reverse-twist of DYOL throttle dumped current back into the pack cleanly — pack absorbed it (unlike the Matrix bench supply that overvolted on the same test 2026-04-23). **Regen is now real-pack-verified.** Can re-enable regen current beyond 0A on-bike for descent braking whenever desired.
- AFU 58.8V/10A charger connected, charging in progress.

**Currently doing (during charge):**
1. DMM cell-group spread mid-charge (~54V): probe each B(n)→B(n-1), expect 3.86V ± 50mV
2. Touch Daly case every 15 min — cool/warm OK, hot = stop
3. Watch for clean termination at 58.8V (charger LED2 green when CV holds and CC tapers <0.5A)
4. Let pack sit 1 hour post-charge, re-check cell spread for drift

**BMS mounted with double-sided foam tape / hot glue (NOT epoxy)** — Daly is removable if it ever fails. Balance harness routed with service loop so P1 can be unplugged without cutting tape.

**Deferred items resolved/skipped (dumb-BMS choice):**
- ~~Thermistor install~~ — Daly has internal OTP, no app to display external thermistor data, skip
- ~~Button decision~~ — Daly has no external button, nothing to decide
- **Copper strip reinforcement** — defer or skip; heavy leads verified holding, can add later if voltage sag observed under load

**Still to do before pack is ride-ready:**
1. Verify clean charge termination at 58.8V
2. Re-check cell spread post-charge (1 hour rest)
3. **Short test ride** with light throttle, monitor for sag/heat/regen behavior
4. Then full pack wrap (shrink-wrap or sealed bag) — only after one full charge cycle + test ride proves the pack

**21700 + 200A JK still shelved** until 18650 is wrapped and rideable. Resume per Update (2026-04-25 morning) plan below.

---

## Update (2026-04-25) — Daly Arrived 5 Days Early, 18650 + Daly Is Now Active

Daly 60A common-port Li-ion 14S BMS shipped early — in hand 2026-04-25 (was ETA 2026-04-30). **Plan flip:** instead of using the 6-day window to commission the 21700 + 200A JK first, jump straight to 18650 + Daly. 21700 + 200A JK shelved cleanly (no balance harness installed yet — nothing to undo).

**Why flip:** the 21700 plan was filling dead time. With Daly here, the fastest path to a rideable bike is the 18650 pack — it's already 90% built, balance harness in place, heavy leads verified clean.

### Immediate next actions (Daly + 18650)

1. **Eyeball Daly's P1 connector pitch** vs. existing 18650 harness plug. Existing is 2.0mm (PH). If Daly matches → plug-and-play. If 2.54mm (XH) → re-pin or rebuild harness. **Decision gate before any wiring.**
2. **Heavy leads onto Daly**: B- to N0 wire (existing solder joint, verified holding 2026-04-24 — pull-test before committing), P- to existing Y-split (Powerpoles + XT60 GND).
3. **Plug P1 balance harness.** Daly is dumb by intentional choice — no app, no commissioning workflow, no wake ritual, no Bluetooth handshake. Hardware-fixed thresholds for the 14S Li-ion 60A model.
4. **Verify pack live**: DMM at Powerpoles → expect ~48V real. (If you see 41V, that's the leakage artifact from the dead JK era — should NOT happen with the Daly because its FETs default to conducting on a healthy pack. If you see 41V, something is wrong.)
5. **Test 3** (100W incandescent + DMM ammeter in series across Powerpoles V+/GND): expect 400–800 mA. Confirms FETs conduct.
6. **Thermistor install** (count TBD: 1, 2, or 4 on hand?), **button decision** (external momentary on bag exterior or capped/tucked), **copper strip reinforcement** on B+/B- pads (Option B alongside existing leads, ferrule-flatten technique on wire ends).
7. **Wrap pack** — only after Test 3 passes. Pre-wrap commissioning gate is holding for a reason.

### 21700 + 200A JK — deferred, clean state

Pack is in a good state to resume later: cells stacked + nickel welded, no balance harness installed (nothing to undo). When 18650 is wrapped and rideable, return to this:

1. Pre-flight 21700 (visual welds + DMM staircase N0→N14, cell spread <50mV)
2. Build fresh 2.54mm JST-XH balance harness (15 wires)
3. Install heavy leads + Y-split discharge
4. Mount 200A JK, cap unused dual B-/P- pair
5. Charger-wake → JK app commission (cell count=14, OVP 4.20V/cell, UVP 2.80V/cell, OCP 80A, OTP 60°C)
6. Test 3 load test, then wrap

---

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

### P1 dry-fit FAILED — pitch mismatch (2026-04-24, late)

User dry-fit existing P1 plug against spare 200A's balance socket: **pin pitch is larger on the 200A**. Likely 2.0mm (PH) on the dead JK / existing 18650 harness, 2.54mm (XH) on the 200A. **Plug-and-play killed.**

### Plan flipped back — Option 2 locked in (200A → 21700, Daly → 18650)

The pitch mismatch eliminated the only reason to put 200A on 18650 (speed). Reverting to original gut-instinct assignment:

| Pack | Cells | BMS | Why |
|---|---|---|---|
| **Pack A: 18650 VTC6** (12 Ah, 624 Wh) — **practice pack per user intent** | Existing build, dead JK removed | **Daly 60A common-port** (Amazon B0CZQJ6G39, ETA Thursday 2026-04-30) | Right-sized for 30A Z9 system. May plug-and-play if Daly is also 2.54mm; may need re-pin if Daly is 2.0mm. Acceptable risk on a practice pack. |
| **Pack B: 21700 Samsung high-drain** (~16–20 Ah, 832–1040 Wh) — **production pack** | Cells stacked + nickel welded, no balance harness installed yet | **Spare 200A JK** (in hand) | High-current BMS rightly paired with high-capacity high-drain cells. Build balance harness FRESH to match 200A's 2.54mm pitch from scratch — no re-pinning friction. |

**Why this is better than re-pinning the 18650 harness:**
- No crimper purchase / wait
- 21700 commissioning is happening anyway (user committed to second pack)
- Each BMS lands on its naturally-matched pack
- 18650 stays "as-is" until Daly arrives, no work disturbed
- 6-day Daly window used productively to commission the 21700

### Tonight (2026-04-24)

1. ✅ **Daly already ordered** — non-smart variant chosen intentionally to sidestep firmware/Bluetooth/wake-failure modes. Arrives Thursday 2026-04-30.
2. **Set 18650 pack aside cleanly**: disconnect dead JK from heavy leads, insulate bare wire ends with heat-shrink or tape (Pack+ at N14 stays live, don't let dangling B-/C- leads find it).
3. **Stop for the night.** Long debug session — diminishing returns past this point.

### Tomorrow / next session — start 21700 commissioning

1. **Pre-flight the 21700 pack** (assumes cells stacked + nickel welded but no balance harness):
   - Visual inspect: nickel welds look uniform, no missing welds, no scorch marks
   - Pull-test on existing pack-level joints (Pack+ heavy lead, B- heavy lead — if installed)
   - DMM staircase across cell groups directly on the nickel: N0→N1, N0→N2, ... N0→N14. Each step adds the cell voltage. Confirm monotonic climb to ~48V.
   - Cell voltage spread: all 14 within 50mV? If one is 100mV+ off, that group has a problem — investigate before BMS install.
2. **Build balance harness fresh** — sized for 2.54mm JST-XH pitch (200A's connector). 15 wires, B0 through B14, terminated in a 16-pin XH shell with one position blanked (or 15-pin if available). Match wire colors to the existing 18650 harness convention for muscle-memory consistency.
3. **Install heavy leads** on 21700 pack — Pack+ direct from N14, B- to BMS B- terminal. Y-split for discharge (Powerpoles + XT60) per existing topology.
4. **Install 200A JK** — connect heavy leads, **cap unused B- and unused P- pair** (200A has duals; for 40A application use only one each). Plug fresh balance harness into P1. Don't plug P2 (14S only uses P1).
5. **Charger-wake** Matrix at 58.8V/2A into XT60 charge port → watch for ammeter rise + BLE advertise.
6. **Commission via JK app**: cell count = 14, verify all 14 cells reading correctly, set protection thresholds (OVP 4.20V/cell, UVP 2.80V/cell, OCP 80A — give 200A some headroom, OTP 60°C).
7. **Re-run Test 3** (100W bulb + DMM ammeter across discharge connector). Expect 400–800 mA. Confirms FETs conduct.

### Thursday (2026-04-30) — Daly arrives, 18650 swap

1. **Inspect Daly's balance connector** — what pitch? If 2.54mm, may match Daly's pinout to existing 18650 harness directly. If 2.0mm, may match the existing 18650 harness directly (since old JK was likely 2.0mm). If neither matches, may need fresh balance harness on the 18650 too.
2. **Connect Daly to 18650**: heavy leads (B- to N0 wire, P- to discharge harness), balance harness via P1.
3. **Commission**: Daly is **non-smart by user choice** (no Bluetooth, no app, no firmware-config gate). 14S variant is hardware-fixed for cell count and protection thresholds — wire it up and it works. No commissioning workflow needed. This was an intentional choice to sidestep the firmware-failure modes that bricked the JK.
4. **Test 3** on 18650 with Daly. Expect FETs conduct under load.
5. **Wrap both packs.**

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
