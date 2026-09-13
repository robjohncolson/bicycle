# Bridgestone Kamakiri × CYC X1 Pro Gen 4 — Build Plan

**Status:** planning, 2026-09-13. Replaces the Karate Monkey, Krampus, and Big Dummy plans (all scrapped the same day).
**Goal:** a low-center-of-gravity, upright, hill-strong cruiser to contrast the Kilo TT, built for the price of a motor kit and a chain. It is a test mule for the layout; the CYC moves to a rider-rated 20" cargo frame (Globe Haul ST shape) if the layout proves out.

## The bike

| | |
|---|---|
| Frame | Bridgestone Kamakiri "Selec KS 240 F", hi-ten step-through, red. Steel assumed (stamped-plate dropouts); magnet test pending |
| Wheels | 24 × 1 3/8, Kenda K-40 37-540, 55 psi max. ISO 540 is rare; Schwalbe Marathon 37-540 at max pressure is the upgrade. Rear tire load ~100 kg at 300 lb is at the edge of a 37 mm tire's rating |
| Rear hub | Solid bolt-on axle, horizontal dropouts, **14T 1/8" screw-on freewheel (stays)**, Bridgestone **Dinex enclosed drum brake** on the left (cable, reaction arm clamped to chainstay). Survives a mid-drive; rear wheel does not need to come off |
| Front | Caliper brake, basket. Upgrade: long-reach dual-pivot + Kool-Stop salmon pads; later a Sturmey Archer XL-FDD drum front wheel |
| BB | 68 mm BSA, cup-and-cone. Drive-side fixed cup seized (LH thread: clockwise to loosen from the drive side). Must be out, faces clean, before the CYC order |
| Fit | Frame sized for ~155-175 cm; rider is 190 cm. Max seatpost extension and raised bars; respect insertion lines |

## Drive

| | |
|---|---|
| Motor | CYC X1 Pro Gen 4, **32T / 53T**, 68/73/83 BSA, 160 mm cranks, SW102 36-72 V, brake sensors, **full-twist throttle** |
| Gearing | 32T → 14T on a 1.93 m wheel = same road-per-crank-turn as the Kilo's 42/20 on 700c. Top speed at 52 V ≈ 57 km/h, more than the brakes want; right hand and current cap enforce the difference |
| Chain | **1/8" KMC e101** (the 14T is 1/8"; a 3/32" e9 will not fit). Size with the wheel forward in the slots, then slide back to tension |
| Chainline | Measure ring-to-centerline and freewheel-to-centerline with the motor mounted; within 2-3 mm or the single-speed throws chains. Fix with CYC ring offset / BB-side spacing |
| Battery | **14S4P Samsung 50S 21700 on a 100 A Daly dumb BMS** (JK broke). X12 battery current cap **60-70 A** (4P × 25 A cell limit). Kilo keeps the 18650 VTC6 pack on its 60 A BMS |
| Pack location | Low on the down tube ahead of the BB in a bolted cradle (4×14 sideways brick ≈ 88 × 308 × 70 mm, ~4 kg). Not the rack |
| Charger | Existing 58.8 V |

Why the CYC over a BBSHD kit: the CYC ships with controller, display, throttle, and brake sensors; the BBSHD path the user would actually build (bare motor + Baserunner + harness + display) lands within a couple hundred dollars and is more work.

## Gates before spending

1. Fixed cup out → shell width confirmed 68, faces clean → **order CYC kit + e101 chain**.
2. Magnet test on the down tube.
3. Photos still wanted: whole bike drive side (cradle location), front brake and fork crown.
4. Motor mounted → chainline measured → ring offset decided → chain cut.

## Wear and safety habits

- Bolt check before each of the first five rides, then weekly: rear axle nuts, Dinex reaction-arm clamp (threadlocker), CYC BB clamp (re-torque after ride 1 and week 1), stem, seat clamp, rack/basket, pack cradle. Paint-pen witness marks.
- Keep speed up on hills; don't crawl. Watch motor temperature in the app after the first hard climbs. Pedal the steepest bits.
- Inspect welds at head tube / down tube, seat tube at post end, chainstays near the BB for paint cracks after the first month.
- DMM on the balance connector every few weeks and after hard rides (dumb BMS gives no per-group view; the Kilo's group-3 sag was a weld).
- 14T takes the full torque; expect faster chain/cog wear. Freewheel is a cheap part.

## Superseded docs in this repo

`karate-monkey-build.md` (gearing math + tool list still valid), `krampus-purchase-guide.html`, `krampus_xl_slow_build_purchase_guide.html`. Kept for reference; not the plan.
