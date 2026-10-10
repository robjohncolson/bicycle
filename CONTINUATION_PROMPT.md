# Continuation Prompt — Kilo TT E-Bike Build

## Update (2026-10-10) — COMMERCIAL PACK DECLINED; 4P → KILO, 10P STAYS THE PLAN; COPPER-COMB TERMINALS; KM TOOLS

**Battery decision (rider):** looked at Johnny Nerd Out 72 V 50 Ah (20S10P, 42.5 lb, $1,299 — declined: >60 V kills the Baserunner, motorcycle pack) and the **52 V 31.8 Ah triangle** (14S6P Samsung 53G, 80 A BMS, BTBGT2170 case, ST3 charge port, XT90S discharge; $789.98 with their 1–5 A / 80-90-100 % charger; Grin sells the same pack at $780 bare with a 60 A BMS and UL 2271). **Declined.** Reasons: 53G is a ~9.8 A energy cell (6P ≈ 59 A, so the CYC would be capped ~55 A anyway); 1.65 kWh is less than the planned DIY; and every commercial option breaks the connector rule (ST3 / mini-XLR chargers, adapters, second charger). ST3 ≠ mini-XLR — JNO chargers end in mini-XLR and need a per-pack adapter. Rider has commuted on self-welded packs and is not worried about build risk. **Stay 14S, stay DIY, stay XT60-charge.**

**Plan reaffirmed:** finish the **14S4P 21700 / Daly 100 A** now (most likely stays on the Kilo, built to be Monkey-capable at 70 A) → CYC lands ~2026-10-12, mount it, read max battery current in the app → **holders ordered 2026-10-10, earliest arrival 2026-11-05** (Heyiarbeit 21.7 mm hole / 22.3 mm pitch, B092PYWVPT: one 2-pack 9×10, two 2-packs 5×6, optional third for a practice cut — 21.7 mm version only, P50B won't enter 21.3) → P50B cells ~end of October after a couple of weeks on the 4P → **14S10P folding over the winter, no deadline** (~$1,400 all-in with tools). 8P plan dropped. Class T fuse size (125/150 A) waits on the app reading.

**Nickel sizing settled (0.2 × 10 mm strip, 2 mm², ~15 A per layer on a short cell-backed span):**
- Series bridges, one per cell: **single layer** on both packs (4P at 70 A = 17.5 A/strip, acceptable; 10P at 125 A = 12.5 A/strip). Optional second short layer on the 4P bridges only if an IR-thermometer / mV-drop check after a hard ride says so.
- Parallel cross strip: single layer — carries balance current only **while every cell has its own bridge**. Where 10P front-group geometry leaves a cell un-bridged, that strip carries 12.5 A per un-bridged cell it feeds; double where >~15 A/layer.
- Terminals: 4P = the 8-strip stacked finger tab (2 layers × 4 cells, ≤30 mm free) **or** the copper comb below. 10P N0 / N14 and both sides of the 5–6 junction = copper comb. Nickel link losses are negligible next to cell IR (~25 W per 4P group at 70 A); only the terminal, where all current converges into one unsupported tab, needs the heavy build.

**Copper comb (settled, no solder on the pack, no copper under the welder):** copper bus with 0.2 × 10 nickel flags soldered to it **off-pack** at cell pitch, flag teeth hanging off one long edge; comb laid on the group and each flag spot-welded (2 spots) to the group's ordinary welded parallel strip, **weld spots ≥ 8–10 mm from the solder** and copper ≥ 5–8 mm back from the cell ends. Flags are 0.2 mm, not 0.1 (one cell's share at 125 A is 12.5 A; 0.1 × 10 is good for ~6–7 A). Kapton both faces + fish paper under; only flag roots and the bolt end bare; M6 hole punched/drilled, Daly lug directly on the copper, washers, nyloc, heat-shrink. **Scrap test first** (weld a soldered flag to scrap strip on a dead cell, peel, confirm the solder joint didn't move). Rider wants to **practice this on the 4P before the 10P** — 4P uses it at N0 / N14. Bus stock: **order ~1 ft of 1 × 10 mm (or 0.8 × 12) copper bar** for the 10P (2 mm² foil is 62 A/mm² at 125 A — too thin). For the 4P, the leftover **uxcell 0.2 × 10 mm copper foil, two layers** is fine: tack the layers only at the four flag positions (flag soldered through both) and at the bolt — no need to sweat the full length. Record after the practice: welder behaviour with copper ~10 mm from the electrodes, solder-to-spot distance that holds, how much the comb lifts.

**Charger / aging note:** 10 A on the 18650 pack was 2.5 A/cell (VTC6 standard charge 3 A) — not the cause of the aging. Likely causes in order: charging cold at school after a cold ride (plating), one weak group (group 3), sitting at 58.8 V, resistive joints. The planned per-group voltage-drop test discriminates. New habit regardless: don't charge a cold pack; let it warm indoors first.

**Karate Monkey crank / CYC tools (Deore 12-sp Hollowtech II, 73 mm BSA):** Park BBT-19.2 (16-notch, 44 mm — also the CYC manual's BB tool), BBT-10.2 or Shimano TL-FC16 preload cap tool, 5 mm hex (pinch bolts), rubber mallet, long/T-handle **8 mm hex** + **3 mm hex** (CYC manual), adjustable wrench, torque wrench to 50 N·m, blue Loctite, grease, zip ties. Crank puller (CCP-22) only for later CYC crank removal. **Drive-side cup is reverse thread (clockwise to loosen); left cup normal.** CYC 73 mm spacer stack: 7 mm + 3 mm on the left, none on the right (68 mm stack differs — don't mix). CYC lock-ring torque not published — snug, ride, re-check; ask support@cycmotor.com. Chain: rider's **Park CT-5 handles 12-speed** (Park Q&A confirms SLX/XT/XTR 12-sp); Shimano 12-sp joins with a single-use quick link — keep a spare SM-CN910 / KMC 12-sp link; close by pedal-and-brake, open with a cable loop, no pliers needed.

## Update (2026-10-06) — KILO ON 36T: HILLS FINE, SAME LATCH AT THE SAME DISTANCE → SOC-DEPENDENT, NOT LOAD

**Field result (rider):** commuted on the 18650 pack with the 36T freewheel. Climbed every hill without trouble, then the same dark-display latch hit at the same point as before — near the end of the 9-mile leg into Lynn.

**Read:** the 36T roughly halves lug current and the hills passed, yet the trip landed at the same mile. A fault that ignores gear and current and keys on distance is an *energy* fault: one weak or resistive group reaches the Daly's cell UVP (~2.5–2.8 V) once ~400+ Wh have come out of the pack, while the other 13 groups still sit at ~3.4 V and the pack reads ~47 V — above the Baserunner's 45 V rolloff, so the controller never tapers; the Daly just opens. Earlier entries treated "dark + needs replug" as OCP-only and "UVP self-releases in ~1 min" — too strong. With the Baserunner still hanging on the output the Daly can hold UVP; unplugging removes the load and it releases, which looks identical to a latch. The 2026-09-30 "unstable joint" theory is not dead (a resistive series joint lowers that group's voltage under load and makes it hit UVP first), but it no longer needs vibration or a current spike to explain the timing. The 2026-10-03 "aging out" theory fits better than scored there: the pack only has to be short on one group, not all 14, and a 2024-practice VTC6 pack at 300 lb / 45 Wh·mi⁻¹ is at the edge of a 9-mile hilly leg anyway.

**Rider constraints (2026-10-06):** no voltage readout on the bike (SW102 shows no usable voltage; TRRS comm port still broken), and the balance plug is inside the polyolefin heatshrink, so no per-group readings without opening the pack. **Never trips in the first 3 miles on a full charge** → SOC confirmed. Open question is only *whole pack too small* vs. *one weak group*.

**Tests that settle it (outside the wrap, DMM at the XT60 charge port):**
1. XT60 rested at full charge (expect 58.8 V); XT60 right after the trip, before replug (common-port Daly → ~0 V while it holds the trip = BMS opened, not controller); XT60 a minute after replug, no throttle. ≤ ~48 V = pack genuinely deep. ≥ ~50 V with the trip still happening = one group far below the rest.
2. Wh returned by the charger at school (Kill-A-Watt / energy smart plug, ÷ ~0.88 for charger loss). ≥ ~550 Wh = whole 624 Wh pack drained, too small for the leg. ≤ ~400 Wh = weak group cutting off with energy left in the other 13.
3. Buy a 60 V inline watt meter for the discharge lead (V, A, Ah, Wh, min-V record) — stands in for the missing display, transfers to the 21700 pack.

**Implications:** the 36T stopgap does not buy a full leg; a mid-route top-up or a smaller "pedal the last mile" plan is needed until the 21700 pack is on. The 21700 A/B test stays the decisive step, and the group-3 joint fix before it goes on matters more now, since the same mechanism would bite that pack through group 3. Stay on 36T for the gentler current until the pack is inspected.

**Next:** run tests 1–2 on the next commute (both directions). Finish the 21700 pack per the 2026-10-04 plan.

## Update (2026-10-07) — KM CHAINSTAY / CYC FIT CONCERN

Rider looked at the assembled Monkey's drive-side stay and worried the CYC won't fit. Resolved on paper: the motor mounts to the 73 mm shell and down tube, nothing near the stays. Stock ring is **30T** (not 32T as earlier notes said). The only clearance question is the **53T motor sprocket (~140 mm, cover ~150 mm) vs the yoke** — it sits inboard of the bike ring and is diameter-equivalent to a 35–37T ring on a 32T-max frame. **Next:** paper-disc template at the BB (140/150 mm, ~42–46 mm from centreline) before the HK kit lands (late Oct / early Nov). Fallbacks if it kisses: run without the cover, CYC chainline spacers. **The BBSHD is NOT a safe fallback for the Monkey:** a 2020 KM owner's 68 mm BBSHD + Luna Eclipse 42T hit the chainstay (electricbike.com thread 106744) — deep-offset 42/46T rings tuck ~10 mm inboard toward the yoke and the gearbox boss wants ~66 mm BB-centre-to-stay. BBSHD on the KM would need shell spacers + a low-offset ring (chainline ~58–60 mm, loses the low 3–4 cogs). Neither motor has a confirmed yes on a Karate Monkey. Details in `karate-monkey-cyc-build.md` § Why 32T.

## Update (2026-10-04) — ZnCl2 ARRIVED; ALL 21700 NICKEL FLAGS TINNED

**Done (rider):** ZnCl2 arrived 2026-10-04 and **all nickel flags for the 14S4P 21700 / Daly-100A pack are tinned** with ZnCl2 flux, loose on the bench, nowhere near the pack. Method as run: ZnCl2 in distilled water (glass bottle, glass stir rod; ~1:2 to 1:1 by weight is enough — true saturation is a ~4 g/mL syrup and not needed), scuff → dab with a horsehair brush → tin → hot water + toothbrush → **ethanol** second rinse (no IPA on hand; fine, it only chases the water). Rider confirmed: every flag washed and fully dry, weld ends bare (no flux, no solder), solder flowed flat (= real nickel).

**Order of operations changed (rider, supersedes 2026-09-23 step 2–3 and the 2026-09-26 "flag sequence"):** solder the leads onto the tinned ends **first**, loose on the bench with rosin, **then** spot-weld the bare ends to the pack. Upside: no iron ever comes near a cell. Added hazards and their controls:
- A bare flag hanging on a wire can bridge two adjacent group strips → **tape or sleeve every waiting flag, uncover one at a time.**
- Each plug pin goes live as its flag lands → **balance plug stays unplugged from the Daly for all welding** (weld pulses through a connected BMS can kill it). Weld N0 first, then N1..N14.
- Staircase voltage check on the loose plug before it goes near the Daly. Hot-glue strain relief after each weld, fillet inspected first.

**Open — power leads on flags:** rider plans to solder the **power** wires to nickel flags as well as the balance wires. The 2026-09-23 plan (step 4) put N0 / N14 on a welded thick copper pad or multi-layer nickel with solder kept out of the 70 A path. A single small flag is a balance-current part, not a 30–70 A part. Settle the N0 / N14 termination (flag size, layers, number of welds) **before** those leads are soldered. **The Daly 100 A's B- and P- leads end in factory-crimped ring lugs** (the old pack had bare wire soldered to nickel). Proposed, not yet agreed: keep the lugs; B- bolts to a multi-layer nickel terminal tab built off-pack (fingers welded across all 4 cells of group N0, free ends stacked past the pack edge, punched, bolt + washers + locknut, lug face directly on the nickel, fully insulated, wire strain-relieved); P- bolts lug-to-lug to the Powerpole / XT60 Y-split and is heat-shrunk. Rider's strip is **0.2 × 10 mm** nickel (~10 A continuous per layer): one strip per N0 cell covers the Kilo's 30 A (7.5 A each); **two layers per cell (8 strips), free length ≤ ~30 mm**, for the Monkey's possible 70 A. Same build for N14. **Daly lugs are stamped SC16-6** (16 mm² cable ≈ 5 AWG, M6 hole) → **M6 hardware**: M6 × 16–20 mm steel/stainless bolt, flat washer each side, nyloc nut. Strip ends get a 1/4" (6.35 mm) hole with a hand metal punch, punched off-pack before welding, 1–3 layers at a time against a marked distance, deburred flat. Strips weld to the pack one layer at a time (each weld only fuses the new layer to the one below; offset the spots; scrap-stack peel test first). Still unknown: whether the Daly leads have a lug on both ends or only on the BMS end. **Daly manual is now `BMS.pdf`** (Mini-red hardware BMS, K series 40/60/100 A): screw torque 8–10 N·m; B- cable ≤ 40 cm; blue = B-, black = P-; **NTC must be plugged in or the BMS blocks charge and discharge**; after plugging the sampling cable, B+→B- must equal B+→P- or the wiring is wrong.

**Output connector changed (rider, 2026-10-04): XT90, no Powerpoles** (rider: Powerpoles melt) — supersedes the Powerpole discharge half of the Y-split wherever it appears below. Female (shrouded) half on the pack. V+ lead: **8 AWG** silicone, **SC10-6** lug (M6, matches the Daly's SC16-6 hole) on the N14 tab → XT90 + cup. 10 AWG (SC6-6 lug) is enough for the Kilo's 30 A but runs warm at the Monkey's possible 70 A inside the EVA wrap — 8 AWG preferred. SC lugs need a hex or hammer crimper (Engineer PAD-11 is signal-pin only). Open: how P- reaches the XT90 (lug-to-lug pigtail vs. cut the Daly lug), where the charge branch tees off, XT90-S or plain.

**Scheduled:** lead soldering + welding some time in the week of 2026-10-05. Then: fix the group-3 joint while the pack is open → Daly 100 A wiring order (2026-09-23) → bench-commission → onto the Kilo as the A/B test against the 18650 latch. The 18650 pack stays closed until the 21700 is working (sequencing rule, 2026-10-03).

**Bible write-back still owed:** Daly-100A step 7–8 variant, flag / ZnCl2 tap method (with the solder-then-weld order), heater subsection, EVA / fire-bag packaging.

## Update (2026-10-03) — KARATE MONKEY ASSEMBLED; KILO NOW ON 36T; KM STREET TIRES OPEN

**Karate Monkey:** assembled by the rider. Stock Dirt Wizard 27.5×3.0 judged too knobby for street. Rider bought an **SKS 75 mm U-stay fender**, which is narrower than a 3.0 (~76 mm) tire, so the plan is urban tires that fit under it: **27.5 (584), ~2.4–2.6" / 62–65 mm** on the WTB ST i40 rims. Candidates: Schwalbe Super Moto-X 27.5×2.4 (62-584), Schwalbe Pick-Up 27.5×2.6 (65-584), Maxxis Hookworm 27.5×2.5. Not yet ordered. Narrower tires need narrower tubes (the 3.0 tubes will not carry over) and drop circumference ~3 % (~2.30 m → ~2.23 m), so the gearing table in `karate-monkey-cyc-build.md` shifts slightly lower.

**Kilo:** 36T freewheel is now on (the 2026-09-30 stopgap is done). Everything else in the 2026-09-30 entry still stands: inspect the 18650 pack before going back to 20/22T.

**Rider's alternate theory: the 18650 pack is aging out.** Poor fit: aging raises internal resistance and cuts capacity, it does not lower the full-charge voltage, and it shows up as sag → self-releasing UVP, not a latch. With the Baserunner capped at 30 A battery current, sag cannot push current to the Daly's 60 A trip. Not ruled out until measured. No-open tests: rested full-charge voltage (58.8 V pack, ~4.20 V × 14 at the balance plug); SW102 voltage at rest vs. on a climb (expect ~2–3 V sag at 30 A; much more = resistive pack); per-group voltages under load (uniform drop = aging, one group = joint or weak group).

**Sequencing rule (rider):** the 18650 pack does not get opened until the ZnCl2 has arrived and the 21700 pack is reassembled and working — never be without a rideable pack.

**18650 diagnosis method (agreed, not yet run):** voltage drop under load, not ohms. Load = the bike itself (stand + rear brake drag for per-group readings at the balance plug, rest vs. load; then SW102 voltage on the hill) or a resistive appliance / incandescent bulbs in lamps on a plain power strip (~3–5 A). Outlier group = open there; wiggle leads under load for the intermittent. Rider now reports rosin fully wets the nickel, so targeted reflow of the high-current joints is acceptable (rosin only on the pack, <3 s, everything else masked). Full tear-off/re-tab of all strip is NOT a weekend job on the only rideable pack — defer until the 21700 is in service. Rider does not ride again until Tue 2026-10-06.

**Replacement Baserunner (leaning, not ordered):** TRRS jack is broken, so a new controller restores comms and lets the 30 A cap be verified. Rider regrets not buying the **L10** originally and is leaning L10 over Z9 (more phase current = more hill torque at the same battery current). L10 needs an L1019 motor pigtail with phase + Hall re-spliced, edited phase limits (not a straight `z9tune2.xml` load) and a fresh Autotune; battery cap stays 30 A for the Daly 60A. Old Z9 becomes the spare / goes to a possible second BBSHD build on the mamachari. Verify L10 specs on Grin's site before ordering. **Revised same day:** the Kilo's BBSHD has the Z910 connector soldered onto the motor leads and the rider does not want to redo that — so the Kilo replacement is another **Z9** (plug-in; Superharness is on Main9 and unaffected either way); the **L10** is for a fresh motor on the possible mamachari build.

**KM bag:** Revelate Designs **Rifter, XL (rider believes)** — listed 17.25" top tube × 14" seat tube × 19.5" down tube (438 × 356 × 495 mm), 8.5 L, vertical divider + mesh pocket in the main compartment, full-length left side pocket, wire exit port, Velcro straps, no published weight rating. Paper estimate (unmeasured): ~520 cm² usable after a 20 mm inset → roughly 70–90 cells crosswise at 22 mm pitch before BMS space, so **14S5P (70) is the likely fit, 14S6P (84) a stretch**. Make-or-break unknown is interior width (cells crosswise need ~80 mm). A 70-cell pack is ~5.5–6 kg — strap load is a concern.

**Rifter measured (rider, 2026-10-03):** confirmed XL; gusset is **72 mm all round**; divider is Velcro-in, removable. Cells fit crosswise but with ~no spare thickness (70.3 mm cell + strip + insulation + wrap ≈ 72–73 mm): no face foam, no BMS or heater pad on a face — BMS and main leads go in-plane, face protection is thin rigid sheet (~0.5–1 mm FR4/polycarbonate), not EVA. Target stays 14S5P.

**Rifter outline, tape-measured (rider, 2026-10-03; supersedes the listing dims):** pentagon A top-rear, B top-front, C bottom of head stub, D front of bottom stub, E bottom-rear. AB 48, BC 9, CD 46, DE 9.3, EA 32.3, diagonals AC 49.5, AD 34 (cm). Solved coordinates (cm): **A(0,0) B(48,0) C(48.7,−9.0) D(9.3,−32.7) E(0,−32.3)** — corner A is square, B ≈ 94°. Area ≈ **1120 cm²**. Hex-packing count (21.2 mm cells, whole cell inside the margin): 20 mm margin / 22.5 mm pitch → ~175 cells; 15 mm / 21.7 mm → ~199. **Geometry is no longer the limit** — 14S6P (84), 8P (112) and even 10P (140) fit; weight on the Velcro straps (~70 g/cell), cost and the cell's current rating decide the P count. **Rider correction:** corners A, B and E are all 90° (the off-square solve was tape error) → use the squared outline **A(0,0) B(48,0) C(48,−9) D(9.3,−32.3) E(0,−32.3)**, a 48 × 32.3 cm rectangle with the lower-front corner cut off; area ≈ 1100 cm², down-tube edge computes to 45.2 cm (measured 46). Cell counts drop ~2 %, conclusion unchanged. Unconfirmed whether the tape measurements are the bag's inside or outside. P count not yet chosen.

**KM PACK DECIDED (rider, 2026-10-03): 14S8P 21700 (112 cells), 52 V** — stays 14S so it swaps with the Kilo (redundancy over performance); 8P over 10P for component room. The measurements are of a cardboard template that fits the bag tightly (= interior). Stencil: `km-rifter-14s8p-stencil.svg` (1:1 mm) — 14 columns × 8 rows honeycomb at 22 mm pitch, ~318 × 155 mm block in the top-rear corner, ≥13 mm edge clearance, group 1 (seat-tube end) = Pack+, group 14 = Pack−. Written into `karate-monkey-cyc-build.md` § Battery pack. Open: cell model, BMS choice/dimensions, strap reinforcement for ~8.5 kg, print + test-fit the stencil on the cardboard.

**Holder option under consideration (not bought):** Aicosineg 8×9 21700 square-grid holders (Amazon B09R9X7S28, 5 pcs, 21.7 mm holes, 23 mm pitch). Alternate stencil `km-rifter-14s8p-stencil-square.svg`: L-shape, groups are rows of 8 — rear stack 8×9 (one uncut holder, groups 6–14) + front stack 8×5 (groups 1–5), ~368 mm wide × 207 mm deep, holder edge ≥10 mm from every bag edge; one fold strip (5–6) across the full 16-cell top row. Unknown: holder lip over the cell ends (72 mm gusset). The honeycomb stencil stays the default until a holder is chosen.

**8P re-confirmed after looking at 10P** (`km-rifter-14s10p-stencil-square.svg`, declined). Foam, lead routing via the bag's exit port, adjustable-trip BMS (~200 A hardware, OCP ~100 A), recommended main fuse, XT90-class connector + Powerpole adapter, and the no-heater / never-charge-below-0 °C rule are all in `karate-monkey-cyc-build.md` § Battery pack. Still open: cell model, holder purchase + lip measurement, BMS model, fuse yes/no, full-thickness dummy test-fit through the zipper.

**Staging idea (rider, 2026-10-03, not committed):** run the Monkey first on the existing **14S4P 21700 / Daly 100A** pack with foam fill in the Rifter, and build the 8P (or 10P) pack later once the bag, mounting and wiring have proven out. Rider also has a **JK 200 A BMS** that stopped working on the 14S4P pack, suspected cause bad soldering rather than a dead BMS — candidate for the big pack **only after a bench check** (app connects, all 14 cell readings correct, charge/discharge FETs switch, OCP set and verified). Note the 4P pack is also the Kilo A/B test pack and is still apart awaiting ZnCl2.

**LATEST STATE (end of 2026-10-03 session) — supersedes the 8P lines above:** rider charges at school, commute is 9 hilly miles each way, so the Monkey **starts on the existing 14S4P 21700 pack** lying along the down-tube edge with yoga-block foam above it (`km-rifter-14s4p-foam-cuts.svg`; 4 EVA blocks to order). **Final pack = 14S10P, "when, not if"**, built as two folding sub-packs joined by flexible 8 AWG links at the 5–6 junction (`km-rifter-14s10p-stencil-square.svg`). Nothing ordered yet; no cells to buy until the 4P pack has done measured commutes. Details in `karate-monkey-cyc-build.md` § Battery pack.

**END OF SESSION 2026-10-03 — ALL PURCHASES ON HOLD until the CYC motor arrives (rider decision, budget).** Nothing was ordered. The settled shopping list, for when it resumes: 140 + a few spare **Molicel P50B** (18650batterystore bulk price $7.50 ea at qty 140; $1,143.94 with shipping + tax on this date); **Heyiarbeit 21.7 mm / 22.3 mm-pitch holders** (Amazon B092PYWVPT: one 2-pack 9×10, two 2-packs 5×6, consider a third for a practice cut); **Class T fuse**, 125 A or 150 A (Blue Sea 5114 = 150 A, 160 V DC, 20 kA; or Littelfuse JLLN / Mersen A3T), mounted with ring lugs + heat-shrink, no fuse block; **4 EVA yoga blocks** for the 4P pack's foam fill. Pack stays **14S** (72 V considered and declined again: Kilo swap, charger/BMS, >60 V hazard). CYC max battery current still unconfirmed — read it in the app; it decides 125 vs 150 A fuse. Brake upgrade (4-piston, 203 mm front) advised before full power. Unchanged and still first in line: Kilo 18650 voltage-drop test before Tue 2026-10-06, finish the 4P 21700 pack when the ZnCl2 lands, bench-check the JK 200 A.

**KM pack prototype (superseded by the line above):** rider will fit the triangle bag in the Karate Monkey and measure it to stencil a new 21700 pack. Wanted: cardboard tracing of the bag's usable interior, inside width at the crank-pass point, zipper side, cable exit. Plan on ~22 mm cell pitch, ~80 mm finished thickness with cells crosswise, space reserved for the BMS and ~10 mm padding; cell count in multiples of 14 (56 / 70 / 84).

## Update (2026-09-30) — KILO: LATCHED HILL STALL ON A WARM DAY → NOT TEMPERATURE; 36T COMMUTE STOPGAP

**Field result (rider):** 18650/Daly-60A pack insulated and carried in the battery bag, ridden on a warmer day — **still stalled on the hill it used to climb fine.** Symptom: **display dark, needed unplug/replug** = Daly **latch** (OCP/SCP), same signature as 2026-04-26, not the ~1 min self-releasing UVP. Temperature is ruled out as the primary cause. **Heater is NOT installed yet** (Tue 09-29 install did not happen) — so it is not a factor.

**Cog:** rider unsure whether the rear is **20T or 22T** — confirm by counting. That gearing had been fine for months, so the failure is **new**.

**Ranked causes:**
1. **Unstable solder/weld joint in the pack (rider's theory, best fit).** An intermittent series joint that opens/recloses under vibration + load makes sharp current transients → Daly SCP trips in µs and latches. Explains new-and-worsening. Find it: group voltages at the balance plug right after a stall; rest vs. steady load on the bench (outsized drop spans the joint); hand/IR check of nickel and bus joints right after a hard climb (hot spot).
2. **Baserunner Max Battery Current drifted/reset above 30 A** — can't check until comms are restored (below).

**Stopgap (rider decision):** flip to the **36T freewheel** as the cold-weather/hill gear. Motor-only (42/36 too low to pedal), boring, but the reliable way to get to school — the April 36T switch stopped the same latch. It masks the joint, not fixes it: ride gently, feel for pack hot spots, open and inspect the pack before going back to 20/22T. No fuse on this build — a worsening joint is a fire risk.

**TRRS comm jack snapped off the Baserunner** (the 09-19 torn pigtail). Not the cause of the latch (0–5 V serial, can't pull 60 A), but repairing it is the only way to verify the 30 A cap, reload `z9tune2.xml`, and log current/voltage on a hill run. Plan: pack unplugged + DMM 0 V; if conductor stubs remain outside the potting, splice a 3.5 mm **TRRS female** pigtail, individually heat-shrunk, overall sleeve + zip-tie strain relief. **Get the TRRS pinout from Grin before plugging in the USB-TTL cable** (not in `Baserunner_V6_Manual_Rev0.pdf` §2.7); ground can be found by continuity to battery negative, do not guess the rest. No usable stub → Grin repair/replace.

**Range on 36T (corrected):** not worse. Lower gear = higher motor RPM, less torque/current on climbs (I²R losses fall with current²), and the ~11–12 mph flat-out top speed cuts aero drag. Only offsets: no pedal contribution, and the commute takes ~50 % longer — leave earlier.

**Next:** count the cog → flip to 36T and commute on it → repair TRRS + check Max Battery Current → **ZnCl2 arrives Fri 2026-10-02: finish the 21700 / Daly-100A pack** per the 2026-09-23 plan + 2026-09-26 tinning notes (scrap flag first; fix the group-3 joint while it is open). Bench-commission, then swap onto the Kilo as the A/B test: if the latch stops on the 21700, the 18650 pack is confirmed as the fault. Bench the 18650 for the bad joint after it comes off.

## Update (2026-09-27) — 18650 PACK HEATER: PARTS CONFIRMED, INSTALL BY TUE 2026-09-29 AM

**Target pack: the 14S4P 18650 VTC6 on the dumb Daly 60 A** (the pack on the Kilo now, still unwrapped — pads bond straight to the cell walls). The 2026-09-26 heater plan applies unchanged; the 21700/Daly-100A pack gets the same treatment later.

**Parts in hand (Amazon):**
| Part | ASIN | Spec | Use |
|---|---|---|---|
| DERNORD silicone pads, 4 pcs | B0C73D8GLC | 12 V 20 W, 50 × 150 mm each | **2 per pack** (40 W). 18650 pack now, 21700 pack later — do not put a third on one pack. |
| HiLetgo W1209 w/ case, 2 pcs | B07VDRGK9F | 12 V DC, -50…110 °C NTC, 10 A NO relay | **One per pack** (18650 now, 21700 later). No spare — the bimetal cutoff is the only independent backup. |
| Yancincny buck w/ fuse | B0FSDSVJC1 | 24–72 V in → 12 V 5 A (60 W), waterproof | 58.8 V full charge is inside the input range. 40 W pads + W1209 ≈ 3.5 A = 70 % of rating. |

**Check on the physical parts before wiring** (listing text was not readable): the buck's built-in fuse rating and which side it sits on (if it is ≥5 A on the input, add a 2 A on the 52 V side anyway); whether the pads have adhesive backing (if not: thin Kapton + thermal-adhesive or a strip of 3M VHB at the edges, never epoxy); pad lead length.

**Still to source / dig out of the bin (Monday morning):** normally-closed bimetal cutoff — **order MECCANIXITY KSD9700 60 °C NC 10 A metal 5-pack (Tue Sep 29 delivery); the SENRISE B07RSF27VS in the cart ships Oct 5–9, drop it**. Need two (one per pack). Tuesday's first ride goes without it: leave a 5 cm loop in the pad line, splice it in Tue evening, P6 = 45 is the only guard that day, unplug the buck when parked; 2 A fuse + inline holder for the 52 V leg; Powerpole housings/contacts for a third leg on the pack Y-split (or a Powerpole splitter); ~1 m 18 AWG silicone wire; heat-shrink; Kapton tape; 5 mm EVA sheet (on hand).

**Wiring (all after the Daly P- FETs, nothing on cells or the balance plug):**
```
Pack Y-split (Powerpoles) ──► 2 A fuse ──► buck IN (52 V side; keep this end up/sealed)
buck OUT +12 V ──► W1209 +12 V
buck OUT +12 V ──► W1209 relay K0
W1209 relay K1 ──► NC bimetal cutoff (taped to pad 1) ──► pad 1 + pad 2 in PARALLEL ──► buck OUT GND
buck OUT GND ──► W1209 GND
NTC probe ──► mid-pack cell wall (group 6–8), under the foam, on the side OPPOSITE pad 1, Kapton'd
```
Pads in parallel (series would give 6 V each = 10 W total). Relay switches the +12 V line only. The "switch" on the heater branch is unplugging the buck's Powerpole leg — a 60 V DC-rated toggle is not in the bin, and a 12 V automotive rocker on the 52 V side is not acceptable. Unplug it any time the bike sits more than a day (buck idle draw + W1209 ≈ 20–30 mA).

**W1209 setup** (hold SET ≥5 s for the menu, short-press SET to edit the setpoint): P0 = **H** (heat; ships as C = cool, which would run the pads when *warm*), P1 hysteresis = **3**, P2 upper limit 30, P3 lower limit 0, P4 offset 0 (correct against the DMM thermocouple if off by >1 °C), P5 delay 0, **P6 = 45** (relay off above 45 °C regardless of setpoint — second software guard). Setpoint **15 °C**. Display shows probe temp = read it before every winter charge (floor 5 °C).

**Pad placement on the 18650 linear pack (~4 cells wide × 14 long):** one pad per broad face, centred on the pack length, long axis along the cells, flush against cell bodies. Keep ≥10 mm from strip edges, balance leads, N0/N14 heavy leads and the Daly. Pads go on first, then the EVA wrap, then the pack goes in the VLITEX bag on the top tube; buck + W1209 case ride outside the EVA but inside the bag, cable-tied so no board edge touches nickel or the 52 V pigtail.

**Monday order of work (~3 h):**
1. Bench the buck alone on the pack Powerpoles: DMM 12.0 ± 0.5 V out, nothing warm.
2. Add W1209, set the menu above, verify relay clicks when the probe is warmed in the hand (H mode confirmed).
3. Wire the two pads through the cutoff, power, clamp-meter ~3.3–3.5 A, pads warm evenly in 60 s. Hair-dryer the bimetal: pads must drop out, then resume as it cools.
4. Bond pads + probe to the pack, EVA wrap, bag it, route the 52 V leg to the Y-split. One hand, DMM polarity check at the buck input before the final Powerpole mate.
5. Tuesday pre-ride: on the charger, heater running (pre-heat at home) → note display temp at departure and again at arrival. Still >~10 °C after the commute = working.

**Bible write-back still owed:** heater subsection (this + 2026-09-26), EVA/fire-bag packaging, tinning method.

---

## Update (2026-09-27) — KAMAKIRI: SEIZED FIXED CUP IS OUT

**Drive-side fixed cup removed** from the 68 mm BSA shell with the hardware-store bolt clamp. Days of Kroil soaks and steady pulling did nothing; the fix was putting the breaker bar on the right end of the rig. What did **not** matter in the end: more Kroil, heat gun, cheater pipe (none used on the winning attempt).

**Rig that worked** (bolt too short to exit the shell, so the nut lives outside on the drive-side cup face, bolt head inside the shell):
1. Clamp: ratchet + socket through the non-drive side holds the inside bolt head; 6-point socket + 1/2" breaker bar on the **outside drive-side nut**, clockwise, as hard as possible.
2. Pull the ratchet out. Nothing needed on the non-drive side once clamped — clockwise on the outside nut both tightens the clamp and loosens the LH cup, so slip only grips harder. Never rock counterclockwise without the head held (that unwinds the clamp).
3. Drive the outside nut clockwise (viewed from the drive side) with the breaker bar. Cup broke free.
4. Cup then needed tapping out of the shell from the non-drive side: hammer + flat-blade screwdriver on the cup's inside edge.

**Lessons:** put the driving torque on the piece that sits *outside* the shell, where a socket seats square. Driving the piece inside the shell rounded a nut face (socket cocks in the ~1.32" bore). A crescent wrench is a holder, not a driver. Phosphoric acid on the exposed cup ring was considered and skipped: it can't wick into an oil-wetted thread and the bind is inside the threads, not on the face.

**Kamakiri gate 1 cleared.** Next: clean the shell faces/threads, magnet test on the down tube.

**PLAN CHANGE (rider, 2026-09-27): the incoming CYC X1 Pro Gen 4 (32T/53T, HK order) goes on the Kamakiri FIRST as a trial**, before committing it to the brand-new Karate Monkey XL. The Kamakiri is the test mule; the KM stays untouched until the CYC has proven out. The Kilo keeps the BBSHD set for now (the 2026-09-14 "BBSHD set moves to the Kamakiri" idea is on hold, not dead). **Chain decision: run a 1/8" chain over the CYC 3/32" ring, 14T 1/8" freewheel stays, rear wheel stays on.** A wide chain on a narrow ring runs (with slop/noise, no narrow-wide retention); the reverse (3/32" chain on the 1/8" freewheel) does not. Gearing 32T→14T on a 24" wheel stays tall for the Dinex drum + caliper — accept for the trial, right hand governs; an 18T 3/32" freewheel + 3/32" chain is the upgrade if the Kamakiri gets ridden hard or when the BBSHD set moves over. Still open: throttle-only wiring with the full-twist + SW102 that shipped; pack mounting low on the down tube per `kamakiri-build.md`. `kamakiri-build.md` updated with the working puller procedure and this status.

---

## Update (2026-09-26) — FLAG TINNING TRIAL (rosin only), HEATER HARDWARE IN HAND

**Tinning trial before the ZnCl2 arrives.** First attempt failed outright: phosphoric-acid pickle → rinse → rosin-in-ethanol dip → heat-gun dry → solder would not wet. Diagnosis: phosphoric acid leaves a passive phosphate conversion film on nickel (parkerizing chemistry) and the heat-gun dry re-oxidised the bare strip before any solder arrived; plain rosin is too mild for nickel anyway; and nickel strip heat-sinks a small iron. Second attempt worked much better: **sand (coarse), wet rosin immediately, hot chisel iron with a wet tip, dwell 2–4 s on cardboard, feed solder at the contact point** — wets, but still partly balls. **Decision: do NOT tin production flags with rosin.** Partial wetting = solder on oxide, no real contact footprint, uninspectable once wrapped. Wait for the ZnCl2 (ordered, in the mail). Drop the phosphoric pickle entirely.

**When the ZnCl2 lands:** tin ONE scrap first. Real nickel flows flat in one pass; still balling under ZnCl2 with a hot iron = the strip is stainless → source new strip before tinning anything. Expect hiss/acid vapour (ventilate, gloves), tip erosion (spare cheap tips bought; wipe/re-tin often; brass wool not a wet sponge), and a hot-water + toothbrush + IPA wash on every flag, fully dry before welding. ZnCl2 off the cardboard — use tile/plywood for that session.

**Flag sequence confirmed:** tin loose (ZnCl2) → wash → **spot-weld the bare end** → solder balance lead onto the tinned end with rosin (<2–3 s) → **hot-glue strain relief**: blob bridges the solder joint + first ~1 cm of wire, wire routed flat along the strip before it turns toward the BMS. Hot glue touching strip/cell is fine. Not silicone sealant (hardware-store silicone is acetic-cure = corrosive to fresh joints; neutral-cure/704 only for cell-to-cell gluing). Check the fillet visually before glueing over it. No heat-sink clip needed — no iron ever sits on strip over a cell in this order (pliers across the strip is the rework fallback).

**Winter heater — hardware received, plan revised from 2026-09-23:**
- **2 × 20 W 12 V silicone pads (40 W total)**, buck converter (**80 V input rated — OK for 58.8 V**), thermostat module (W1209-class; confirm which board). Do NOT upsize the pads: drain and fail-on hazard scale with wattage, and a preheated pack mostly coasts.
- Purpose: range/sag on the ~1 h commute AND keeping cells chargeable. **Preheat at home on the charger** (wall power), thermostat only holds temperature on the ride. Setpoint 15 °C-ish, few °C hysteresis, probe on a mid-pack cell wall under the foam (not on a pad).
- **Pack rides in the VLITEX L fire bag on the top tube** (fiberglass/silicone — fire containment, NOT insulation) — supersedes the frame-triangle-bag note. **Wrap the cell section in 5 mm closed-cell EVA** (The Foamory sheet, ~sleeping-pad R-value) inside the bag; **leave the Daly end unwrapped**. EVA softens ~80 °C / burns → backup cutoff below is mandatory.
- Pads bonded flat to the cell walls, one per side, under the foam, clear of BMS, balance wires and strip edges. Buck + thermostat boxed or shrunk (bare boards next to nickel/52 V pigtail = chafe short). 52 V input side kept up/sealed from rain.
- **Protection chain, all three:** (1) 2 A fuse on the **52 V input** side (two pads pull ~3.4 A at 12 V, so a 2 A fuse on the 12 V side would blow — use 5 A there if fusing the output instead); (2) **normally-closed bimetal cutoff 50–60 °C, or thermal fuse, in series with the pads, taped to a pad** — independent of the thermostat electronics, saves the pack if the relay welds; (3) physical switch on the heater branch (40 W ≈ 4 %/h of the 21700 pack; buck idle draw flattens a stored pack over months). Tap after the Daly discharge FETs, never on cells.
- **Daly is dumb → no low-temp charge cutoff exists.** The thermostat display is the pack thermometer; read it before winter charging (floor 5 °C, comfortable >10 °C). Optional hard block: thermostat relay switches the charger AC instead of the pads.
- Field check after the first cold ride: cell temp on the thermostat display at departure vs. arrival; still >~10 °C after an hour near freezing = foam + pads working.

**Not yet written back to the bible:** all of the above (heater subsection, EVA/fire-bag packaging, tinning method). Add with the Daly-100A step 7–8 variant when the 21700 pack goes onto the Kilo.

---

## Update (2026-09-23) — 21700 PACK: DALY 100A WIRING PLAN, BALANCE-TAP REWORK (nickel flags + ZnCl2), WINTER HEATER

**Balance taps: rip off the copper strips and redo.** The cold-welded copper-on-nickel flags never bonded (hobby spot welders shunt through copper) — they all come off. Replacement method, settled with CC:

1. Cut short nickel flags (~10 x 5 mm). **Tin each flag loose, before it goes near the pack:** scuff with 400-grit → dab saturated **ZnCl2 in distilled water** (~1:2 by weight; stored in a 50 mL glass reagent bottle, PTFE/ground-glass cap, no metal) → hot iron, tin → **hot-water rinse + toothbrush** (ZnCl2 is a salt: alcohol alone does NOT remove it) → alcohol → dry. ZnCl2 never touches the pack; never on strip that sits on a cell.
2. Spot-weld the **untinned** end of the flag to the group strip so the tinned end hangs in air past the cell edge.
3. Balance lead: tin with rosin, rosin on the flag, join in <2 s, heat-shrink where the wire leaves the flag. Iron never sits on strip over a cell (21700 positive cap / CID).
4. Heavy leads (N0 / N14): welded thick copper pad or multi-layer nickel, crimp/solder the lug off the cell surface; keep solder out of the 70 A path where possible.
5. **Resolve the group-3 high-R joint while the pack is open** (2026-06-06 issue) — do not re-seal it.

**Daly 100 A (dumb, common-port) wiring order** (mirrors bible steps 7–8, Daly deltas): DMM all 14 groups at the nickel first → balance harness to the pack FIRST, N0 then N1..N14, one tap at a time → staircase check on the loose plug against the B- pin → confirm B- by continuity to the plug's B- pin (**Daly 60A ran BLUE = B-, BLACK = P-; do not trust colour; Sharpie it**) → solder B- to N0 → P- to the GND Y-split (Powerpoles + XT60, common-port so charge and discharge share P-) → build V+ Y-split off-pack → land V+ on N14 LAST, one hand → polarity check referenced to N0, not P- → plug balance connector in (= power-on; output jumps from ~1–2 V leakage to pack V) → bench load, then first charge with case-touch checks. Count the plug pins (15 for 14S; some 100 A Dalys ship 16 with pin 0 = B-). No B+ board-power pin. NTC probe on a mid-pack cell body. Keep the balance plug reachable post-wrap (only cell visibility). Foam tape / hot glue, not epoxy. Heavy leads are ~8 AWG: PP45 contacts or accept PP30 at its limit at the 70 A cap. Daly OCP is the only overcurrent protection and it latches.

**Cold-weather range loss (rider observation): plan.** (1) Charge/store indoors, mount the pack right before leaving; never charge below 0 °C. (2) **Pack goes in the frame-triangle bag** with closed-cell foam. (3) **12 V silicone heater pad** (10–20 W, ~100 x 150 mm) against the cell bodies, opposite side from the probe, fed by a 60 V→12 V buck off the discharge Powerpoles (NOT the balance plug), **2 A inline fuse** on the 12 V side, a switch/unplug so it never drains a deep-discharged pack. Thermostat: **W1209 / XH-W1209** (12 V, NTC probe taped to a mid-pack cell body, set 15 °C, 2 °C hysteresis, heating mode; box or shrink the bare board) — or a 15 °C normally-open snap-disc in series with the pad if no electronics wanted. Skip PTC "self-regulating" pads. ~15 Wh/hour ≈ 2 % of the 21700 pack. (4) Winter tune: lower battery current, widen LVC rolloff / drop LVC end a couple of volts. Cold exposes the weakest group first — read group spread at the balance plug on a cold morning after a ride to separate whole-pack loss from a bad group.

**Not yet written back to the bible:** a Daly-100A variant of steps 7–8 and the flag/ZnCl2 tap method. Add when the 21700 pack goes onto the Kilo.

---

## Update (2026-09-21) — KILO: P03 RECURS AFTER CONNECTOR REDO; NOW ALSO AT 5 MPH

Redid every connector in the motor plus the Baserunner→battery power lead: **cutout still recurs** on hills after extended riding. New data point: end of the 9-mile commute, turning into a parking lot at ~5 mph (near-zero load), it shut off and would not restart until the battery was unplugged/replugged. (Rider typed "P30"; assumed to be the same P03 — confirm.)

**CORRECTION (same day, after rider clarified) — the Hall read below is superseded.** The display goes **dark**, the code shown is **P30** (not confirmed to be P03; meaning unverified), and there are two behaviours: (a) on hills P30 appears → back off throttle → bike recovers; (b) parking lot: speed display → abrupt black, **would not power on for ~60 s**. Dark display = the battery side dropped the bus. A fixed ~60 s lockout matches a **JK BMS protection trip and its release timer** (confirm the configured release times in the app), not a loose main terminal (which would reconnect at random, not on a timer) and not a controller fault (display would stay lit).

**CORRECTION 2 (rider): the pack on the bike is on the dumb Daly 60A BMS, NOT the JK** — so the JK-timer and group-3 paragraphs below do not apply as written (and the 2026-06-06 "21700 + 200A JK on the Kilo" status is no longer current; confirm which cells are behind the Daly — assumed the 18650 VTC6 pack). Dark display still = the BMS opened or the pack path opened. With a Daly, the ~60 s dead time is not a timer; it is the time for the trip condition to clear. Ranked:
1. **Cell-group UVP on a weak/low group** — best fit. Daly cuts when any one group dips to ~2.5–2.8 V under load and releases only when it rebounds past ~3.0 V, which takes about a minute unloaded. Fits "only after extended riding" (low SOC at mile 9, heavy rider + hills ≈ 40–50 Wh/mi out of ~600 Wh) and fits P30-on-hills-recovers-on-throttle-release (controller seeing sag just before the BMS would cut). No Bluetooth, so it is invisible without a DMM.
2. **Daly over-temperature** — FETs/NTC hot after 9 miles at a 55.2 A battery-current tune on a 60 A BMS; releases on cooling.
3. **Daly OCP** — tune is 55.2 A battery vs. 60 A rating, and this Daly already OCP-latched on hills on 2026-04-26. Usually needs load removed (unplug) to reset.
4. Loose pack terminal / cracked weld — possible but would not produce a consistent ~60 s dead time.

**Code identified (rider lookup): P30 = Error 30 = display↔controller communication lost** (generic Bafang-family description; not Grin-confirmed). Not a Hall code — the 2026-09-19 "P03 = Hall" reading is withdrawn; the code was most likely 30 all along. Two ways to lose comms here: (i) the Baserunner stops answering because it browns out / resets under pack sag (ties into the Daly list above), or (ii) the UART itself is being corrupted. **For (ii) the torn comm pigtail is the prime suspect: the error first appeared in the same window the pigtail tore out, and if that port shares the UART / 5 V with the display link (believed so on Grin controllers — verify with Grin), bare TX/RX/5V/GND stubs touching each other or the frame under vibration would produce exactly an intermittent Error 30, and a 5 V→GND touch would kill the throttle too.** Fix first, it is free: battery unplugged, inspect the stub where it exits the potting, separate and individually insulate every conductor (heat-shrink / liquid tape, then seal against water). Also re-seat the Superharness↔SW102 and Superharness↔Baserunner signal plugs. The generic "isolation test" barely applies — no brake sensors, PAS or lights; the throttle is the only accessory on the 5 V rail. Error 30 does **not** explain the parking-lot blackout (display dark ~60 s = bus power gone), so the Daly tests below still stand; there may be two faults.

**Rider's plan (2026-09-21):** treat Error 30 and the power blackout as separate faults. Finish soldering the **21700 pack with a 100 A BMS** and swap it onto the Kilo as an A/B test for the blackout (if the dark-display cutouts stop, the 18650/Daly pack was the cause). Insulate the torn-pigtail stubs at the same time — the two faults have different symptoms (code with display lit vs. display dark), so changing both does not muddy the result. If this is the same 21700 pack as 2026-06-06, **resolve the group-3 high-resistance joint while it is open** — do not seal it back in. **BMS for the 21700 pack confirmed by rider: dumb Daly 100 A** (not the 200 A JK in older notes) — no cell visibility, so keep the balance plug reachable for DMM checks. Rider's theory for the 18650 pack: a weak solder/weld joint. Consistent with the UVP read above — a resistive *series* joint sits inside one group's sense window, so that group reads low under load, the Daly cuts on cell UVP (display dark), and it releases after the group rebounds (~1 min). Bench-find it after the swap: per-group voltage at rest vs. under a steady load; the group with the outsized drop spans the bad joint.

**Tests (DMM, no pack surgery):** (a) pack voltage at the XT60 charge port on arrival and immediately after a cutout — below ~47 V means it is simply deep in the pack; during the dark period, ~0 V / floating at the output with the pack otherwise healthy = BMS open. (b) Per-group voltages at the Daly balance plug (back-probe adjacent pins, 14 readings) right after arrival — one group well below the rest = the culprit. **Balance plug is live at up to 58.8 V across its ends: fine probes, one hand, never bridge pins.** (c) Feel the Daly right after a cutout. (d) Does it ever happen in the first 2–3 miles on a full charge? If never → SOC/weak group, not a connection.

*Superseded (assumed JK), kept for history:* Prime suspect is now the known open issue from 2026-06-06: the group-3 high-resistance joint in the 21700 pack**, degraded by three more months of ride vibration. It explains both modes: under hill load group 3 sags → pack/cell voltage dips → fault that clears when throttle is released; late in the commute (lower SOC) a bump momentarily opens the cracked joint → group 3 reads below cell UVP → JK cuts discharge → dark → auto-release after ~60 s. Redoing external connectors could never fix this. XT90 resolder is not the fix either.

**Safety:** a worsening resistive series joint is a localized I²R hot spot inside a sealed pack, and the tune cannot be lowered (comm pigtail torn). Treat as ride-gently-or-not-at-all until group 3 is inspected. Follow the 2026-06-06 diagnostic → fix plan and its high-voltage rework warning.

**Next:** (1) JK app immediately after a trip: alarm/protection status, which cell number is lowest, cell delta. (2) Screen-record the JK app on a hill pull — watch cell 3 vs. neighbours when P30 appears. (3) Re-seat group-3 balance lead to rule out a sense-tap artifact. (4) Open the pack at storage voltage and re-weld per 2026-06-06 steps 3–5.

*Superseded first read, kept for history:* both failures are *low motor RPM + warm*, not high current. The Baserunner runs on Halls at low RPM and goes sensorless above it, so a marginal Hall (sensor or its 5V/GND/signal wiring) only bites while lugging a hill or crawling — and a fixed 42/20 means road speed = motor RPM. A 5 mph cutout rules out the high-current path (phase connectors, XT90, battery terminals) as the cause of that event. Heat-dependence points at a Hall sensor going flaky hot, or a joint opening with thermal expansion.

**Open question that splits it:** did the SW102 stay lit during the parking-lot shutoff? Lit + code = controller fault (Hall). Dark = battery side (BMS trip / power connection) — only then is the pack or XT90 a suspect. Unplugging the battery also power-cycles the Baserunner, so "needed a replug" does not by itself implicate the pack.

**Next:** hot Hall test (back-probe each Hall signal at 5 V, turn the motor slowly by hand, each should swing cleanly ~0↔5 V; wiggle the harness while watching), LED flash code before power-cycling, JK app cell-delta under load to clear the pack without opening it. XT90 resolder is cheap but not expected to fix this.

---

## Update (2026-09-19) — KILO: P03 HILL CUTOUT (latched); BASERUNNER COMM PIGTAIL TORN OUT

**New fault.** Climbing the hill home, motor cut out and the SW102 showed **"P03"**. First time. Display stayed lit (so not a BMS trip / power-connector dropout); needed a power-cycle to clear — unlike the 2026-05-05 I²t cutouts, which auto-recovered with no code. In the KT/KM5s code set 03 = **motor Hall signal abnormal** (from memory — Grin's fault→display mapping not confirmed). Working theory: intermittent Hall 5V/GND/signal contact under load + vibration. Not yet ruled out: a Hall going flaky hot, or a different controller fault surfacing as 03 (tune still runs 55 A phase / 55.2 A battery on a Z9).

**Comm pigtail tore out of the Baserunner body.** No Phaserunner Suite connection → no Dashboard Hall view, no fault readout, **no retuning**. Controller is potted; this is a Grin repair/replace, not a field fix. Bike still rides on the stored tune. `z9tune2.xml` is the authoritative export to load onto a repaired/replacement unit (Power Map needs the post-6.025 firmware to stick — see 2026-05-05 evening).

**Rider's read (2026-09-19):** same hill, same tune for months → this is a *new physical degradation*, not a settings problem. A Powerpole pair has already fused once on this bike, so heat-damaged Powerpole contacts / crimps (phase side, and the joints inside the BBSHD cover) are the prime suspect. Settings are off the table until comms are restored anyway.

**Doc deviation — not yet written back to the HTML / CLAUDE.md:** the battery discharge connector is now **XT90-S (anti-spark, with resistor)**, not Anderson Powerpoles. **It still pops audibly on every connect** → either it's being pushed straight through without pausing at the resistor stage, or the precharge resistor has burned open (common XT90-S failure). Test: insert halfway, hold ~1 s, then seat; if it still pops, the resistor is dead — replace the green (female) half. Not a P03 suspect, but arcing pits the contacts over time. Remaining Powerpoles are the three phase leads. `kilo-tt-ebike-build.html` and `CLAUDE.md` "Non-Standard Build Decisions" still say Powerpoles on discharge.

### Next actions

0. **Heat check:** straight after the hill, feel / IR-thermometer every connector (3 phase Powerpoles, XT90, joints under the motor cover). Hotter than the wire beside it = the bad one. Cut out any cooked Powerpole — fresh contact with a ratcheting crimp + solder, or replace with a soldered splice / 5.5 mm bullets / MT60.
1. **Read the Baserunner LED flash code before power-cycling** if it recurs (1-6 Hall, 1-2 / 2-2 phase overcurrent, 2-4 throttle). Only diagnostic left without comms.
2. External first: re-seat the Hall connector, check for backed-out pins, chafe/tension at the BB, phase Powerpoles fully latched and not heat-discolored.
3. Then the BBSHD controller-side cover (where the adapter meets the motor's Hall plug) — **battery disconnected, caps bled, DMM-verify 0 V first**; re-seal the cable entry after. Motor core stays closed unless everything external is clean and the fault tracks heat.
4. Email Grin about the torn pigtail (repair vs. replacement); include photos.

**Karate Monkey (AMG email 2026-09-19):** ships built + test-ridden, **no pedals, no sealant** → assume tubes installed. Pump up and ride; tubeless conversion later (Orange Seal, tubeless valves, valve-core tool; bead seating from scratch may need core-out or a booster tank). Pedals: 9/16", source separately or via AMG.

---

## Update (2026-09-17) — CYC X1 PRO GEN 4 ORDERED (HONG KONG)

See `karate-monkey-cyc-build.md`. Fool’s Gold XL complete still on order from AMG. **CYC kit ordered from CYC MOTOR (Hong Kong), not Johnny Nerd Out.** 73 mm + **32T/53T**, **full-twist**, **SW102**, **no brake sensors**, no cassette. Cranks 160 if the cart had them, else 165. Made-to-order **5–7 weeks**. 2-year factory warranty.

JNO was cheaper / faster ship, but SW102 was out of stock (would force DS103). JNO’s “DS103 required for 72 V” is a 20S rule — this bike stays **14S / 52 V**. 5-speed skipped: CYC HD is HG, stock hub is Microspline.

Motorcycle-style: throttle is the go-pedal. Half-twist dropped (claw the inner sleeve). Thumb dropped (same thumb as Deore). No ebrake, same as the Kilo. Keep ISO (right = rear). Wrist flat/below; soft torque ramp; PAS off or 0.

32T bike ring is what the KM already runs. Leftover check when the complete lands: ~140 mm **cover** vs yoke (a few mm bigger than a naked 32T). If it kisses, pull the cover. Not a 40T/72T problem.

Next: sit on the 660 mm TT; paper-template 32T/53T at the BB; wait for HK ship.

---

## Update (2026-09-16, later) — KM XL ORDERED; ORDER CYC 32T/53T NEXT

**Done 2026-09-17** (kit from CYC HK, not JNO; full-twist, no sensors). Left as the prior next-action.

Fool’s Gold XL complete is on order from AMG. Next: Johnny Nerd Out **73 mm + 32T/53T**, thumb, sensors, 160/165 cranks, SW102 36–72 V. No 40T, no cassette kit. See `karate-monkey-cyc-build.md`.

---

## Update (2026-09-16) — SECOND BIKE IS KARATE MONKEY XL COMPLETE + CYC 32T/53T

**Order details superseded 2026-09-17** (CYC from Hong Kong: full-twist, SW102, no sensors). Frame choice stands.

See `karate-monkey-cyc-build.md`. Kilo TT still stays on the BBSHD set. Straggler 62 × 40T (`straggler-cyc-build.md`) is paused.

**Buy:** AMG Cyclery Surly KM complete, **Fool’s Gold XL, rigid**, ~$1,849 (not the $2,599 FS / dropper, not the Krampus 29×3). Keep Rustler bars, i40 + Dirt Wizard 3.0, 12-speed, M275s. Sit on the 660 mm TT; 30-day return, you pay freight.

**CYC (was Johnny Nerd Out; ordered HK 2026-09-17):** **73 mm + 32T/53T**. **Not 40T/72T** — KM 1× Boost max is 32T; 72T motor sprocket is ~184 mm and likely hits the yoke. Template in hand when the complete arrives.

**Gearing:** stock **11–51**, live in **13T (~50/20 on 27.5×3)** and **15T (~42/20)**. Ignore 11T under power and 18T+. No CYC 5-speed until the Novatec 32h rear dies. Then: Hope Pro 5 **36h 12×148 HG steel** + CYC 15–30 + **27.5"** 36h i40-class rim (not 700c Andra, not 135 QR).

**104 BCD** bike ring can go 32→38/40 later on the **same 53T**. Full 40T/72T still needs yoke space that probably isn’t there.

Droppers: rider history is sag at 300 lb — skip TranzX. Group-3 sag on the 21700 still open before 70 A.

---

## Update (2026-09-15) — KILO STAYS; NEW BIKE IS STRAGGLER 62 × CYC 40T

**Paused 2026-09-16** in favor of the Karate Monkey complete above. File kept.

See `straggler-cyc-build.md`. The Kilo TT is left alone (BBSHD + Baserunner Power Map + Superharness + SW102 + 18650). CYC does **not** go on the Kilo. Kamakiri transplant is paused (`kamakiri-build.md`). `kilo-cyc-build.md` (32T/16T on the Kilo) is superseded.

New bike: **Surly Straggler 700c 62 cm** (old, 135 QR, IS 160 mm) + **CYC X1 Pro Gen 4 40T/72T** (not 32T) + **160 mm cranks** (165 if no 160) + thumb throttle + SW102 36–72 V + magnetic brake sensors + **14S 21700 / 100 A Daly, 70 A cap**. Gearing: CYC HD cassette **15–17–20–24–30** on **Hope Pro 5 36h 6-bolt, 135 QR, HG steel**; home cog **17T** (closest to 50/20; no 16T on the cassette). Shifter: downtube or bar-end **friction**, not the Advent flat-bar trigger. Do not buy the full CYC HD kit (148 mm hub). Rims: **Ryde Andra 321 Disc 36h both** (Andra 30 Disc 36h fallback). Track 1/8″ cogs stay on the Kilo — stock CYC ring is 9–12s narrow-wide.

PAS ~24 mph @ 120 rpm; throttle wall ~44 mph no-load / ~40–43 on the road. Same hill as the Kilo 42/20 throttle-blip still goes, with more reserve. Midnight Special / Fargo Ti M / Steamroller / Nature Boy / 32T all considered and dropped.

Group-3 sag on the 21700 is still open before 70 A.

Order (Johnny Nerd Out): kit 68/73 + **40T**, sensors, thumb, 160/165 cranks, SW102 36–72 V; plus cassette-only.

---

## Update (2026-09-14) — TWO-BIKE PLAN SETTLED: CYC Gen 4 on the Kilo, BBSHD set to the Kamakiri

**Superseded 2026-09-15** by the Straggler plan above. Kept for the record.

See `kilo-cyc-build.md` and `kamakiri-build.md`. The Kilo TT gets a CYC X1 Pro Gen 4 (32T/53T + the 16T fixed cog on hand: torque-assist to ~19 mph, thumb throttle on a 22.2 mm stub to the ~30 mph RPM ceiling, 2x today's launch torque) on the 14S4P 21700 pack / 100 A Daly with the X12 capped at 70 A. The BBSHD + Baserunner (Power Map tune) + Superharness + SW102 + 18650 pack / 60 A BMS move as a set to the 24" Bridgestone Kamakiri (68 mm BSA, seized fixed cup still to remove). Karate Monkey / Krampus / Big Dummy / Photon / 72 V all considered and dropped. Photos: `dinex.jpg`, `rearcog_kamakiri.jpg`.

---

## Update (2026-06-06) — 21700 + 200A JK COMMISSIONED & ON THE KILO TT; group-3 under-load sag (high-IR joint)

**Status change — supersedes every "21700 shelved / on hold / deferred" line in the updates below.** The 14S4P 21700 Samsung 50S production pack is built (balance harness installed) and commissioned on the spare 200A JK smart BMS, and it is now **installed on the Kilo TT, replacing the 18650 + Daly practice pack.** The pack runs well overall.

- **BMS-OCP hill cutout is gone.** The 200A JK has huge headroom over the Z9's 30A battery ceiling, so the Daly-OCP latch that cut power on steep lugs (2026-04-26) no longer happens. Field confirmation of the original "200A → 21700 production, Daly → 18650 practice" sizing call.
- **Platform note:** this pack is **14S4P / 52V** on the existing BBSHD + Baserunner Z9 system. The 20S6P / 84V CYC X1 Pro plan in the memory files is still future — the current pack is *not* that.

### Open issue — group 3 sags under sustained high-amp draw

Under sustained draw, **series group 3 (of 14) dips noticeably in the JK app and recovers to match the other groups at rest.** Under-load-only sag isolated to one group is the signature of **elevated internal resistance in group 3**, not a charge imbalance.

- At ≤30A through the Z910 cable the pack is only at ~7.5A/cell — well under the 50S's 25A/cell (~100A pack). Real per-group sag at that low a load means the resistance is genuinely elevated, not normal droop.
- **Likely cause:** a cold/lifted/vibration-cracked **spot weld on a group-3 series joint** (the 2–3 or 3–4 nickel link — a bad *series* joint shows up in whichever group's sense window spans it, so it may be an adjacent link, not inside group 3), or a **poorly-bonded/unbonded parallel cell** (parallel-portion resistance rises, up to ~33% for a fully-open cell → 3P; a partial bond is more common, same signature), or a corroded cell-to-nickel interface worsened by ride hours. Each reads normal at rest because parallel cells equalize.
- **The JK balancer can't fix this.** Active balance (0.4A) equalizes *resting* voltage only; group 3 reads healthy at rest so the BMS sees nothing wrong, and 0.4A can't offset a several-amp under-load drop anyway.
- **Why it matters:** group 3 hits LVC/UVP first under sustained load (premature cutoff), and a resistive joint dumps I²R heat as a localized hot spot — a real fire/aging concern on a sealed pack.

### Next-session diagnostic → fix plan

1. **Rule out a measurement artifact first** — wiggle/re-seat the group-3 balance leads + connector, then confirm the sag with a DMM *directly across the physical group terminals* under load. A flaky high-R sense tap carries ~0 current (can't cause real load-sag) but throws false app readings — cheapest, most common smart-BMS fault; eliminate before any rework.
2. **Quantify in the JK app** — log group 3's instantaneous voltage vs. neighbors during a known high-draw pull. Bigger delta at a given current = more excess resistance. Compare groups at *similar temperature* (cold cells read higher IR).
3. **Thermal localize** — right after a sustained pull, IR-thermometer the group-3 interconnects (2–3 and 3–4) vs. cells: hot *joint* = series weld; hot *cells* = poorly-bonded parallel cell forcing the others to carry more.
4. **Measure the joint** — milliohm meter across the suspect series link vs. a good group, or DMM voltage drop across it under known load (V/I = R).
5. **Re-weld** — re-flow/add welds on suspect nickel, confirm all four parallel cells bonded, re-measure to confirm the sag delta drops.
6. **Interim** — lower the controller's Max Battery Current ceiling and keep a conservative per-cell UVP; avoid sustained max draw. Group 3 sags deepest and hits cutoff/over-discharge first.

⚠️ **High-voltage rework (mandatory):** steps 4–5 and the probing in steps 1/4 are on a live ~52V series stack. Discharge the pack toward storage voltage, disconnect the BMS and main discharge + charge leads, use insulated tools, observe the one-hand rule, and keep probes from bridging adjacent groups — a slipped probe or weld on an energized pack is a dead-short / arc-flash hazard.

**Do not** chase this with more charge/balance cycles — it's a mechanical/resistance fault, not a state-of-charge imbalance.

The HTML build bible (`kilo-tt-ebike-build.html`) carries this as a Field Update banner at the top plus a Battery & BMS field-diagnostic callout; its spec tables still describe the original 18650 + JK-BD4A17S4P design pack.

---

## Update (2026-05-05, evening) — POWER MAP enabled to address sustained-load I²t cutout

**The 2026-05-05 LVC + ramp tune did NOT solve the field problem.** Real-world ride up the steepest local hill produced cutouts that **auto-recovered, recurred on re-engage with shorter wait → less recurrence with longer wait**. Pack was nearly full and brand new (sag into LVC ruled out). Motor not hot. Baserunner is mounted apart from the motor (not bolted on), so case heat conduction not a factor.

### Diagnosis: controller I²t firmware foldback

The wait-then-trip-again-then-wait-longer-then-no-trip pattern is the signature of a thermal integrator (I²t accumulator), not voltage sag, not Daly latch, not motor temp. The firmware integrator decays on the 300s cooling-time constant (param 103). At low RPM with sustained ~55A phase current, FET heat concentrates because commutation is slow — same FETs carry the load instead of distributing across three phases per rotation. The I²t accumulator builds in firmware regardless of whether the case is physically hot.

**Slam-from-rest cutout** (still occasional after the ramp tune) and **sustained hill cutout** are likely the same root cause hit from different starting points. Slam at 0 RPM = accumulator builds in hundreds of ms; steep hill at low RPM = builds over many seconds.

### Fix: Power Map (params 157–172) — speed-dependent power cap

User did NOT want to lower Max Phase Current (55A — confirmed great hill torque) or push Torque Up Ramp to 3000ms (would feel sluggish). Power Map is the right lever: limits commanded power as a function of motor RPM, so low-RPM operating points get a soft cap that prevents I²t buildup, while mid/high-RPM still gets full 100% power.

**Curve applied** (anchored on the empirical data point: 40% throttle was sustainable at low RPM on the steepest hill):

| # | Speed % rated RPM | Power % rated |
|---|---|---|
| 1 | 0% | 35% |
| 2 | 8% | 45% |
| 3 | 18% | 60% |
| 4 | 30% | 80% |
| 5 | 45% | 95% |
| 6 | 60% | 100% |
| 7 | 80% | 100% |
| 8 | 100% | 100% |

Plus **Features 2 bit 11** (param 174) set to 1 → "Throttle mapping on speed for torque mode" — required to route throttle commands through the map. Param 174 raw value: 32 → 2080.

### How it got applied (Suite GUI doesn't expose Power Map for sw rev 6.025)

1. **First attempt (firmware 6.025):** edited z9tune.xml directly, loaded via File → Open Parameter File, wrote to controller. Read-back into z9tune2.xml showed **all Power Map params reverted to 4096 (100%) — write was silently filtered**. The Power Map params are not in the Suite's writable list at this firmware level.
2. **Firmware update.** User updated Baserunner firmware (specific version not noted — check Suite for current sw rev).
3. **Second attempt (post-firmware-update):** loaded the same modified z9tune.xml, wrote to controller, read back into z9tune2.xml. **All Power Map values stuck.** Curve, speed setpoints, and bit 11 all confirmed in the read-back.

**z9tune2.xml is now the authoritative export.** z9tune.xml is the hand-edited *injection* file from step 1 — **not** a pre-Power-Map baseline.

> **Correction (2026-08-07, from `tools/tune-diff.py`):** diffing the two exports
> shows only two differing addresses — 256 Software Revision (6025 → 16027) and
> 502 Display Walk Command. Params 157–172 and 174 are **identical in both files**:
> z9tune.xml already carries the same 8-point Power Map curve and bit 11 = 1,
> because it is the file that was edited *to* inject them. **No flat-curve export
> exists anywhere in this repo**, so there is currently no file to load if the
> Power Map needs backing out — that would mean re-editing the curve by hand or
> pulling a fresh export off a reset controller.

### Next-session priorities

1. **Bench test before ride.** Wheel off ground, motor on stand:
   - Slam throttle from rest → motor should ramp smoothly (capped at 35% rated power initially), no cut
   - Verify free-spin reaches the same top RPM as before (curve doesn't clip top end)
   - Hand-brake the wheel at full throttle to simulate hill load → motor should fold back gracefully, not cut
2. **Ride the steepest local hill.** This was the empirical failure point on 2026-05-05 morning. Power Map should now sustain it without cutout because low-RPM commanded power is capped below the I²t threshold.
3. **If slam-from-rest still cuts** → curve floor (setpoint 1) too high. Lower from 35% → 25% or 20%.
4. **If hill still cuts** → setpoint 2/3 (low-RPM power) still too aggressive. Lower setpoint 2 from 45% → 35% and setpoint 3 from 60% → 50%.
5. **If midrange feels weird** (sudden power jumps, dead spots between setpoints) → tell me which RPM range, will suggest curve smoothing.
6. **Empirical refinement procedure** if the curve needs tuning: at constant RPM (push against ground/brake), find the throttle % at which cutout starts. Set Power Map at that speed point to ~90% of measured limit. Repeat at multiple speeds.

### Settings unchanged by this session

- **Max Phase Current = 55 A** (kept — confirmed great hill torque)
- **Torque Up Ramp = 800 ms** (the 2026-05-05 morning fix — leave as is)
- **Torque Down Ramp = 100 ms**
- **LVC Start = 45 V, LVC End = 42 V**
- **Max Battery Current = 55.2 A** (intentional — drives hill performance)
- **Max Regen Battery Current = 0 A** (regen disabled per rider preference)

### Reference

- **Phaserunner exports:**
  - `z9tune.xml` — the hand-edited injection file. **Already contains the Power Map**
    (params 157–172, bit 11) — verified by `tools/tune-diff.py`. It is NOT a
    flat-curve fallback, and no flat-curve export exists in this repo.
  - `z9tune2.xml` — current authoritative config, read back off the controller.
  - Diff them with `python3 tools/tune-diff.py z9tune.xml z9tune2.xml`.
- **Software rev:** updated this session. Whatever the Suite reports now is post-update.
- **Throttle Control Mode:** still 2 = Torque Mode With Speed Limiting.

---

## Update (2026-05-05) — SLAM-STALL TUNED OUT; awaiting real-world ride confirmation

**Phaserunner Suite session complete. Three settings changed, bench behavior is clean. The slam-stall only surfaces in real-world conditions, so the fix is provisional until a ride confirms it.**

### What changed (all written + saved; export in `z9tune.xml`)

| Param | Addr | Was | Now | Why |
|---|---|---|---|---|
| Low Voltage Cutoff (Start) | 141 | 42.5 V | **45 V** | Old rolloff window was only 0.5V wide (42.5→42V) — any pack sag past 42V was a cliff. 3V window now lets the controller taper power gracefully under sag instead of cutting. |
| Torque Up Ramp | 220 | 500 ms | **800 ms** | Smooths inrush peak at 0 RPM throttle slam. Torque-mode ramp lever (Throttle Control Mode = 2 = Torque With Speed Limiting). |
| Torque Down Ramp | 221 | 50 ms | **100 ms** | Slight weight/carry on release without going sluggish. Conservative bump (option was up to 200–300 ms; held back for emergency-cut response). |

### What was NOT changed (and why)

- **Max Battery Current stays at 55.2 A** (param 155). User intentionally raised from 30A → 55A and confirms hills feel much better with the higher cap. Don't give back torque to chase a transient. Slam-stall is a sag/protection-window problem, not a steady-state cap problem.
- **LVC End stays at 42 V** (param 142, 14S × 3.0V/cell). Was discussed dropping to 40V (2.86V/cell) as a fallback. Held back because: (a) one-variable-at-a-time discipline — if 45V rolloff alone fixes it, LVC End shouldn't be sacrificed; (b) 40V starts impacting cycle life of the VTC6s under repeated sag. Reserve 40V as the escalation lever if 45V rolloff + 800/1000ms up-ramp doesn't resolve.
- **Regen settings** (Max Regen Battery Current = 0A, Max Regen Voltage = 59.5V) — left alone, dead reverse-twist is the rider preference.

### Diagnostic logic that drove the fix

Slam-stall mechanism: **slam from rest → motor at 0 RPM → no back-EMF → controller demands full battery current immediately → pack sags hard → sag dips through the 0.5V-wide rolloff straight into the 42V hard cutoff → cut. Release throttle → current drops → pack rebounds → controller auto-recovers.**

Auto-recovery (release-and-retwist works) confirmed it was a controller-side protection trip, not a Daly OCP latch (which would require pack disconnect to reset). Two fixes are complementary: widening the rolloff gives the pack room to sag without falling off the cliff; lengthening the up-ramp lowers the peak inrush so the pack sags less in the first place.

### Next-session priorities

1. **Real-world ride test.** Slam-stall only appears under field conditions — bench tests can't reproduce it. Take the bike out and try slamming throttle from rest at multiple SOCs (full charge, mid-pack, near-empty). Note whether the cutout reappears.
2. **If slam-stall persists** → escalate Torque Up Ramp from 800 ms to **1000 ms** before touching anything else.
3. **If still tripping after 1000 ms ramp** → drop LVC End from 42V to **40V** (param 142). Daly cell-level UVP still protects against true over-discharge.
4. **Pack rest voltage at Powerpoles with DMM** at the start of the ride and after — gives a baseline for where SOC sits when the trip does/doesn't happen.
5. **Hand-temp the motor** after a hard climb. Phase ceiling at 55A means thermal margin is the next thing to watch.

### Reference

- **Phaserunner export**: `z9tune.xml` — full Baserunner V6 Z9 parameter dump as of this tune. Reload via Phaserunner Suite → Read From File if a future tune corrupts settings or the direct comms port dies.
- **Software rev**: 6.025 (param 256 in XML).
- **Throttle Control Mode**: 2 = Torque Mode With Speed Limiting (param 11). All "throttle ramp" tuning happens via Torque Up/Down Ramp (params 220/221) — there is no separate "Throttle Ramp Up Rate" field for torque mode.

---

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

2. **HTML + CLAUDE.md Baserunner current limit correction** — ✅ APPLIED 2026-08-07 (user approved; edits below pushed to `kilo-tt-ebike-build.html`, `CLAUDE.md`, and `ebike-component-spec.md`). Original draft kept for the record: Baserunner V6 Z9 manual (page 2 of `Baserunner_V6_Manual_Rev0.pdf`) authoritatively states **30 A continuous / 55 A peak phase** on the Z910 motor cable, and the factory default in the Phaserunner Suite is **30 A Max Battery Current** (page 12, section 6.4). Current `kilo-tt-ebike-build.html` says "40A continuous" in the spec table and step 16a references "JK BMS 40A" as the system bottleneck — both wrong. The real bottleneck is the Baserunner Z9 at 30A, NOT the BMS at 40A. Fixes ready to apply:
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
