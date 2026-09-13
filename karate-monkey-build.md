> **Superseded 2026-09-12.** The frame decision moved from Karate Monkey to **Surly Krampus XL** (rigid fork, 29 × 3.0, 120 mm max suspension correction), the pack from 20S6P to **20s4p Molicel P50B** on a Daly 150 A BMS, and the wheels to Jones HD/e + DT 350 Hybrid on Velocity Dually 29. The Krampus was itself scrapped on 2026-09-13; the current plan is **`kamakiri-build.md`**. This file is kept for the corrected gearing/thrust math and the tool list, which still apply.

# Karate Monkey / CYC X1 Pro Gen 4 Build — Bill of Materials

**Status:** planning (2026-09-12). Six-month build window, no rush.
**Rider:** 6'3" (190 cm), 300 lb rider + luggage. Frame size **XL**.
**Goal:** torque-first mid-drive on a steel hardtail with the strongest wheels and brakes the frame allows, room for a 20S pack, and rear luggage.

This is a new bike. The Kilo TT build bible (`kilo-tt-ebike-build.html`) stays canonical for the BBSHD bike; nothing here changes it. The BBSHD + Baserunner + 14S pack are earmarked for the 20" mamachari later.

Prices are rough 2026 US retail from memory and search results; treat them as ±20% and verify before ordering.

---

## 1. Why frameset, not the complete bike

Surly's complete Karate Monkey (Fool's Gold spec) ships with a Deore 12-speed drivetrain, Tektro HD-M275 2-piston brakes with 180/160 rotors, and Novatec 32h wheels on WTB ST i40 rims. Every one of those gets replaced for a 300 lb rider on a 280 Nm motor. The only parts of the complete bike that survive are the frame, fork (which you're also replacing with a suspension fork), headset, seat clamp, and saddle. Buy the frameset.

## 2. Corrected gearing and thrust math

Wheel torque = crank torque × (rear cog ÷ chainring). Thrust = wheel torque ÷ wheel radius.

| Setup | Wheel torque | Thrust | vs. 20% grade need (~345 N at 163 kg) |
|---|---|---|---|
| 40T ring, 20T cog, 210 Nm (earlier estimate, **wrong direction**) | 105 Nm | 284 N | 0.8× — would NOT climb it |
| 32T ring, 30T cog, 280 Nm peak | 262 Nm | 718 N | 2.1× |
| 32T ring, 30T cog, 210 Nm sustained | 197 Nm | 540 N | 1.6× |
| 32T ring, 15T cog, 280 Nm | 131 Nm | 359 N | 1.0× (top gear, flat/road use) |

Wheel radius for 27.5 × 2.8–3.0" ≈ 0.365 m; circumference ≈ 2.29 m.

Top speed is not RPM-limited: the Gen 4 spins > 300 crank RPM. In 32/15 that is ~88 km/h at full RPM, so the motor never runs out of cadence on a 27.5+ wheel. Gear for torque; speed takes care of itself.

**Decision: order the CYC kit with the 32T chainring / 53T motor sprocket.** The chainring option also sets the internal reduction, so 32T is the highest-torque configuration CYC offers. Verify chainstay clearance with CYC's printable scale template against the KM's drive-side yoke before ordering.

## 3. Bill of materials

### 3a. Frame and steering

| Item | Spec | Why | ~Price |
|---|---|---|---|
| Frame | Surly Karate Monkey frameset, **XL**, any color | 4130 steel, 73 mm BSA, Gnot-Boost 12×148, 44 mm head tube, IS 51 mm mounts, 203 mm max rotors, suspension-corrected to 551 mm axle-to-crown (140 mm 27.5+). Rear rack/fender eyelets. | $1,099 |
| Fork | RockShox Lyrik Select+ **29"/27.5+**, 140 mm, Boost 15×110, tapered | 35 mm stanchions, air spring you can run near max pressure with volume spacers for 300 lb. 29er forks clear 27.5 × 3.0; 27.5-specific forks often don't. Alt: Fox 36 Performance 29 140 mm GRIP. Coil alt: Marzocchi Bomber Z1 Coil 29 at 150 mm (10 mm over Surly's spec, slackens head angle ~0.5°) with the firmest spring; spring range may top out below your weight, so air is the safer default. | $650–850 |
| Headset | Cane Creek 40, **ZS44/28.6 upper + EC44/40 lower** (tapered) | Surly's stock spec is EC44/30 for the straight-steerer rigid fork. A tapered suspension fork needs the EC44/40 lower. | $60 |
| Stem | 50 mm, 35 mm clamp, 0–6° (Race Face Chester or Turbine) | XL frame, upright cargo posture. | $50–90 |
| Handlebar | 780–800 mm alloy riser, 35 mm clamp, 20 mm rise (Race Face Chester 35) | Leverage over a 40 kg bike. Alloy, not carbon, at this load. | $60 |
| Grips | Ergon GE1 Evo or Ergon GA2 lock-on | Throttle-only means one hand does a lot of holding on. | $35 |
| Star nut / expander + top cap | Included with fork usually; verify | | $10 |
| Headset spacers | 5/10/20 mm alloy, 1-1/8" | | $10 |
| Seatpost | Thomson Elite 30.9 × 410 mm, 0 setback | Rigid alloy post, proven at heavy loads. Dropper optional later (PNW Loam or OneUp V3 in 30.9). | $100 |
| Seat clamp | Surly stainless 33.1 mm (check if frameset includes) | | $15 |
| Saddle | WTB Volt 142 steel rails, or Brooks Cambium C17 | Volt is fine; Cambium if you want more give on a rigid post. | $50–150 |
| Pedals | DMR V12 or OneUp Composite platform | No PAS reliance; big platform for a heavy rider. | $60–120 |
| Rear thru-axle | Surly 12 mm (included with frameset — verify) | | — |

### 3b. Motor and drivetrain

| Item | Spec | Why | ~Price |
|---|---|---|---|
| Motor kit | **CYC X1 Pro Gen 4** (X12 controller), BSA 68–83 mm, **32T chainring / 53T motor sprocket**, half-twist throttle, DS103 display, magnetic brake sensors (+$18) | 5.6 kg, 6000 W peak, 280 Nm peak, > 300 crank RPM, 36–72 V, Bluetooth Ride Control app, torque sensor. Half-twist matches what you're used to from the DYOL. | $1,900–2,300 |
| Rear drivetrain | **CYC Heavy-Duty Drivetrain**: 5-speed 15/17/20/24/30T chromoly + 7075 cassette (HG spline), Microshift Advent Trail Pro shifter + derailleur, KMC e9 Turbo EPT chain, AlexRims 5SB e-bike hub 12×148 | This is the "beefed-up sprocket" cluster. 15–30T gives 2:1 range; 32/30 bottom gear is your hill gear. **Verify the AlexRims hub's spoke count.** If it is 32h, build the rear wheel on the Hope hub below instead and use the CYC cassette on Hope's steel HG freehub; keep the AlexRims hub as a spare. | $300–380 |
| Chain | KMC e9 Turbo EPT (included) + 1 spare | e-bike rated 9-speed width matches the CYC cassette. Not 1/8". | $40 spare |
| Spare chainring | CYC 32T | Steel ring wears; keep one. | $40 |
| Shift cable/housing | Jagwire Pro or Shimano SP41 kit | | $25 |

**Shift discipline:** no gear sensor on the CYC by default. Roll off throttle to shift. The CYC app supports a shift-sensor input on some firmware; check before adding one.

### 3c. Brakes

| Item | Spec | Why | ~Price |
|---|---|---|---|
| Brakes | **Magura MT5** 4-piston, front + rear (or MT5e with built-in cutoff switch) | 4 pistons, mineral oil, huge pad area. MT7 if you want the 1-finger HC lever; same caliper power class. | $280–360 pair |
| Rotors | Magura MDR-P **203 mm**, front + rear, 6-bolt | Two-piece, thick, made for e-bike heat. KM rear mount maxes at 203, fork post mount takes 203 with adapter. | $60–75 each |
| Adapters | Front: post-mount 180→203 (+23 mm). Rear: IS 51 → post-mount 203 | KM uses IS 51 mm rear. Buy the Magura QM adapters or generic equivalents. | $20–40 |
| Cutoff | CYC magnetic brake sensors (kit option) unless MT5e chosen | MT5e's switch is a plain Higo 2-wire and may need a pigtail to the CYC harness; the CYC magnetic sensors clamp to any lever and are known-compatible. | $18 |
| Pads | Magura 8.P Performance (spare set ×2) | | $30 |
| Bleed kit | Magura Royal Blood + syringes | Mineral oil, not DOT. | $40 |

### 3d. Wheels (hand-built, 36-spoke)

| Item | Spec | Why | ~Price |
|---|---|---|---|
| Rear hub | **Hope Pro 5 E-Bike**, 12×148 Boost, **36h**, 6-bolt, **steel Shimano HG freehub** | E-bike variant has steel freehub and 54 POE ratchet built for driven loads; 36h drilling available. HG spline fits the CYC cassette. | $300 |
| Front hub | Hope Pro 5, 15×110 Boost, 36h, 6-bolt | | $150 |
| Rims | **Velocity Dually 27.5"**, 36h, ×2 | 39 mm internal, 45 mm external, 640 g, double-wall, tubeless-ready, rated 60–80 mm tires. One of the few 27.5+ rims sold in 36h. Alt: Halo Vapour 35 36h (narrower). | $95 each |
| Spokes | DT Swiss Alpine III (2.34/1.8/2.0 triple-butted) or Sapim Force, ×72 + spares | Thick elbow where spokes break; use your existing tension tracker workflow. Length from Hope + Velocity ERD via a spoke calculator after hubs arrive. | $110 |
| Nipples | 14G brass, 12 or 14 mm | Brass, not alloy, at this load. | $15 |
| Rim tape / valves | Tubeless tape 45 mm + valves (if running tubeless knobbies) | | $30 |
| Tires (road/mixed) | **Schwalbe Super Moto-X 27.5 × 2.80**, Double Defense, ECE-R75 | E-50 rated to 50 km/h, 3 mm puncture belt. Wire bead → run tubes. | $65 each |
| Tires (dirt alt) | Surly Dirt Wizard 27.5 × 3.0 or Maxxis Chronicle 27.5 × 3.0 (tubeless) | Keep in mind if you go off-road; not speed-rated. | $80–95 each |
| Tubes | Schwalbe SV21F (27.5 × 2.4–3.0) ×3 | Or Tannus Armour inserts for pinch protection at 300 lb. | $12 each |

Wheel notes: front and rear both 36h. Use 3-cross both sides. Tension rear drive-side to the rim's max. Record in the SA-730-style tracker.

### 3e. Battery (20S6P, 72 V nominal, 84 V full)

| Item | Spec | Why | ~Price |
|---|---|---|---|
| Cells | **Samsung INR21700-50S ×120** (+4 spares) | Same cell as the production 14S4P. 6P = 150 A continuous cell rating vs. X12's 100 A peak battery current. 30 Ah, ~2.16 kWh, ~8.4 kg of cells. | $500–600 |
| BMS | **JK-B2A24S20P** (8–24S, 200 A, 2 A active balance, Bluetooth) | Same family as the 200 A JK you already commissioned; set to 20S in the app. Note the physical size before designing the enclosure. | $130–170 |
| Nickel | 0.2 × 30 mm pure nickel, doubled on series links, or nickel-copper sandwich per the 14S4P photos | 70 A continuous needs more than a single 0.15 strip. | $40 |
| Cell holders | 21700 spacers, 2×6 pattern ×enough for 120 | | $30 |
| Discharge connector | **XT90-S** (anti-spark) pack side + XT90 controller side | The X12 has a large input cap bank; 84 V hot-plug will arc-pit Powerpoles. This is the one place to break from the Kilo TT's Anderson decision. Verify the CYC kit's stock battery connector and adapt. | $15 |
| Charge port | XT60 female, panel-mount | | $8 |
| Main wire | 10 AWG silicone, red/black, 2 m each | | $20 |
| Fuse (recommended) | MIDI/ANL 100 A holder + fuse inline on Pack+ | Kilo TT ran without a main fuse by decision. At 84 V and 2 kWh I recommend one; BMS OCP alone is slow and needs the BMS awake. Your call, documented either way. | $25 |
| Charger | 84 V (20S Li-ion) 5 A, XT60 output | Charger-first wake still applies to JK. | $90–130 |
| Insulation | Fish paper, Kapton, 250 mm PVC heat-shrink, neutral-cure silicone | | $40 |
| Enclosure | Triangle frame bag (custom or Rockgeist/Rogue Panda) or aluminum box | Mock the pack up in cardboard first — see §5. | $100–250 |

Pack layout: 6P groups of 21700 in a 6-wide × 20-long brick are ~129 × 430 × 71 mm. Confirm this fits the XL front triangle above the CYC motor with a cardboard mock-up before welding anything.

### 3f. Luggage and accessories

| Item | Spec | ~Price |
|---|---|---|
| Rear rack | Surly Rear Disc Rack (built for seatstay-mounted calipers on the KM) | $150 |
| Front rack (optional) | Old Man Mountain Divide with Boost 15×110 axle kit — mounts to a suspension fork via the axle | $200 |
| Fenders | SKS or PDW 75 mm-wide for 2.8" tires; rear needs rack-compatible stays | $60 |
| Lights | Outbound Detour (front) + Lumen/Cygolite rear, or a 72→12 V DC-DC converter and a motorcycle-grade headlight | $150–250 |
| Kickstand | Pletscher Twin or Ursus Jumbo double-leg, rated for heavy e-bikes | $60 |
| Mirror | Mirrycle or bar-end | $20 |

### 3g. Tools you don't have from the 1" keirin toolkit

| Tool | Why |
|---|---|
| Headset press for 44 mm cups (Park HHP-3 or Wheels Mfg) | ZS44/EC44 cups; a threaded-rod DIY press also works |
| Crown race setter, 40 mm (1.5" tapered) — Park CRS-15.2 or a PVC slug | Tapered fork crown race |
| Star nut setter (Park TNS-4) | Unless the fork ships with an expander plug |
| Steerer saw guide (Park SG-6/SG-7.2) + fine hacksaw | Cut the alloy steerer |
| HG cassette lockring tool + chain whip | CYC cassette on HG freehub |
| Chain tool that handles 9-speed e-bike chain (Park CT-3.3) + KMC missing-link pliers | KMC e9 |
| Torque wrenches: 2–20 Nm and 10–60 Nm | Thru-axles, stem, rotor bolts, CYC lockring |
| Magura bleed kit | Mineral oil system |
| Rotor truing fork (Park DT-2) | 203 mm rotors warp when hot |
| 6 mm hex (thru-axle), T25 Torx (rotors) | |
| Bike stand rated for ~40 kg (Park PCS-10.3 or Feedback Pro) | The finished bike is heavy |
| CYC BB lockring tool | Usually included in the kit — verify |
| Shift cable cutter | |
| Digital calipers | Chainline and chainstay clearance measurement |

Already have: spoke wrench, tension meter, truing stand, spot welder, DMM, crimper (from the Kilo TT and 21700 builds).

## 4. Rough budget

| Group | ~Total |
|---|---|
| Frame + fork + headset + cockpit + post/saddle/pedals | $2,300–2,700 |
| CYC kit + HD drivetrain + spares | $2,300–2,800 |
| Brakes + rotors + adapters + bleed | $500–600 |
| Wheels (hubs, rims, spokes, tires, tubes) | $900–1,000 |
| Battery (cells, BMS, charger, hardware) | $1,000–1,300 |
| Racks, fenders, lights, stand | $400–700 |
| New tools | $350–500 |
| **Total** | **~$7,800–9,600** |

## 5. Build order (draft — expand into a checklist once parts arrive)

1. Frameset + fork + headset. Press cups, set crown race, cut steerer with 30 mm of spacers left above for later adjustment, install stem/bar.
2. **Cardboard mock-up of the 20S6P brick** in the front triangle with the CYC motor position marked. Decide enclosure before buying cells.
3. **CYC clearance check** with the scale template at the BB and chainstay yoke. Confirm 32T ring clears.
4. Wheels: build both 36h wheels, record tensions. Mount tires/tubes.
5. Brakes: mount calipers with adapters, 203 rotors, bleed, bed-in on the workstand.
6. CYC motor install, cassette, derailleur, chain sized in 32/30 with the derailleur at max wrap. Cable up shifter. Mount display, throttle, brake sensors.
7. Battery build: same 14S4P workflow scaled to 20S6P. Commission the JK-B2A24S20P pre-wrap, verify per-group voltages **under load** (the group-3 lesson), then wrap.
8. First power-on with the pack on the bench: XT90-S mate, app connection, throttle response with the rear wheel off the ground, brake cutoff verified before any ride.
9. Racks, fenders, lights, kickstand.
10. Shakedown rides at reduced current in the app, then step up. Retest wheel tension after 50 km.

Same safety rules as the Kilo TT bible apply and the voltage is higher: 84 V full-charge, one-hand rule, DMM before every connector mate, insulated tools on the live stack.

## 6. Open questions

- Which color; XL availability at local shops vs. online.
- AlexRims hub spoke count in the CYC HD drivetrain (32h → use Hope; 36h → could use it, but Hope is stronger).
- Whether the CYC Gen 4 kit's battery lead is XT90 as shipped.
- Fuse: yes or no. Recommend yes at 84 V.
- Front rack: needed, or is rear rack + bar bag enough?
- Dropper post later?
