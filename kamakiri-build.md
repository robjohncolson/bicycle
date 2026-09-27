# Bridgestone Kamakiri × BBSHD — Low-CG Cruiser (transplant build)

**Status:** ACTIVE again 2026-09-27. Fixed cup is out. **The incoming CYC X1 Pro Gen 4 (32T/53T, HK order) is trialled on this bike first**, before it goes anywhere near the new Karate Monkey XL (`karate-monkey-cyc-build.md`). The Kilo keeps the BBSHD set. The BBSHD-transplant tables below are kept as the fallback plan; for the CYC trial: **1/8" chain on the CYC 3/32" ring, 14T 1/8" freewheel stays, wheel stays on** (wide chain on narrow ring runs; narrow chain on a wide freewheel does not). Gearing stays tall — right hand governs; an 18T 3/32" freewheel + 3/32" chain is the later upgrade. Resolve first: throttle-only harness with the shipped full-twist + SW102, pack cradle low on the down tube.
**Goal (unchanged):** a low, upright, calm cruiser to contrast the Kilo. Test mule for the layout; if it proves out, the lesson moves to a rider-rated 20" cargo frame (Globe Haul ST shape).

## The bike

| | |
|---|---|
| Frame | Bridgestone Kamakiri "Selec KS 240 F", hi-ten step-through, red. Steel assumed (stamped-plate dropouts); magnet test pending |
| Wheels | 24 × 1 3/8, Kenda K-40 37-540, 55 psi max. ISO 540 is rare; Schwalbe Marathon 37-540 at max pressure is the upgrade. Rear tire load ~100 kg at 300 lb is at the edge of a 37 mm tire's rating |
| Rear hub | Solid bolt-on axle, horizontal dropouts, **14T 1/8" screw-on freewheel (stays)**, Bridgestone **Dinex enclosed drum brake** on the left (cable, reaction arm clamped to chainstay). Survives a mid-drive; rear wheel does not need to come off except for tires |
| Front | Caliper brake, basket. Upgrade: long-reach dual-pivot + Kool-Stop salmon pads; later a Sturmey Archer XL-FDD drum front wheel |
| BB | 68 mm BSA, cup-and-cone. Drive-side fixed cup was seized (LH thread: clockwise to loosen from the drive side); **removed 2026-09-27** with the bolt clamp below. Shell faces/threads still to clean before the BBSHD goes in |
| Fit | Frame sized for ~155-175 cm; rider is 190 cm. Max seatpost extension and raised bars; respect insertion lines |

## Drive — the Kilo's set, moved whole

| | |
|---|---|
| Motor | Bafang BBSHD (68-73 BSA), stock controller removed |
| Controller | Grin Baserunner V6 Z9 with the current Power Map tune (`z9tune2.xml`); Max Battery Current 55.2 A stays under the pack's 60 A BMS as today |
| Display / harness | Superharness + SW102 (KM5s), DYOL half-twist throttle |
| Battery | 14S4P Sony VTC6 18650 on the 60 A BMS, existing 58.8 V charger |
| Gearing | BBSHD 42T ring → 14T freewheel on a 1.93 m wheel = 5.8 m per crank turn (vs 4.4 m on the Kilo's 42/20): throttle top speed at 160 crank rpm ≈ 56 km/h, more than the brakes want. Options: keep 14T and let the right hand govern, or an 18T 1/8" freewheel (≈ 44 km/h, matches today's Kilo) if the freewheel is ever off |
| Chain | 1/8", as on the Kilo today |
| Chainline | Measure ring-to-centerline and freewheel-to-centerline with the motor mounted; within 2-3 mm. BBSHD ring offset options / BB spacing |
| Pack location | Low on the down tube ahead of the BB in a bolted cradle. Not the rack |

No retuning: the Baserunner tune, LVC, ramps, and Power Map were developed on this exact pack and motor.

## Gates before work

1. ~~Fixed cup out~~ (done 2026-09-27) → shell faces clean.
2. Magnet test on the down tube.
3. Photos still wanted: whole bike drive side (cradle location), front brake and fork crown.
4. Motor mounted → chainline measured → chain cut.

### Fixed-cup puller (hardware-store bolt tool)

- **5/8"-11 × 2" hex bolt** (Grade 5/8; M16 × 50 equiv), matching **nut**, **~6 × 5/8" SAE flat washers** (≈1-5/16" OD; extras stack outside as spacers so the nut lands on thread), **2 split lock washers** against the cup faces for bite. Inside washer must pass the ~1.32" shell ID and sit flat on the cup — test-fit, grind if needed.
- Tools on hand: 1/2" breaker bar + 3/8" ratchet. Buy **15/16" deep socket, 3/8" drive** (inside nut — slim enough for the shell, deep clears the bolt tail) and **15/16" 6-point socket, 1/2" drive** (outside head). No 1/2"→3/8" reducer on the breaker bar — weak link under a cheater pipe.
- **As planned: bolt head on the drive side, nut inside.** (1) Ratchet + deep socket through the non-drive side holds the inside nut. (2) Breaker bar on the outside head, clockwise, clamp hard. (3) Drop the ratchet and keep pulling the head **clockwise** — LH cup thread loosens clockwise, and clockwise on the head also tightens the clamp, so slip only makes it grip harder.
- **As actually done (2026-09-27, worked):** bolt was too short to exit the shell, so the rig ran the other way — **head inside the shell, nut outside on the drive-side cup face**. Same logic: ratchet + socket from the non-drive side holds the inside head only while clamping; then 6-point socket + 1/2" breaker bar on the **outside nut, clockwise**. Clockwise on the outside nut tightens the clamp and loosens the cup at once, so once clamped nothing needs to be on the non-drive side. Do not rock counterclockwise without holding the head — that unwinds the clamp.
- **The rule that mattered: drive whichever piece is outside the shell; only ever *hold* the piece inside.** Driving the inside nut with a socket rounded a face (the socket cocks in the ~1.32" bore). A crescent wrench rounds nuts and is a holder at best.
- Freed cup still needed tapping out from the non-drive side (hammer + flat-blade screwdriver on the cup's inner edge).
- Kroil soaks (days), heat gun, and the cheater pipe were not what freed it; leverage on the correct end was. Keep them as backups: penetrating oil overnight; heat the shell, not the cup; hammer blows on the breaker bar handle; cheater pipe last; brace the frame. Phosphoric acid on the exposed cup ring is pointless — the bind is in the threads and a water-based acid won't wick into an oiled joint.

## Wear and safety habits

- Bolt check before each of the first five rides, then weekly: rear axle nuts, Dinex reaction-arm clamp (threadlocker), BBSHD lockring, stem, seat clamp, rack/basket, pack cradle. Paint-pen witness marks.
- Keep speed up on hills; the Baserunner's I²t foldback is the known limit (Power Map handles it).
- Inspect welds at head tube / down tube, seat tube at post end, chainstays near the BB for paint cracks after the first month.
- 14T takes the full torque; expect faster chain/cog wear.

## Superseded docs in this repo

`karate-monkey-build.md` (gearing math + tool list still valid), `krampus-purchase-guide.html`, `krampus_xl_slow_build_purchase_guide.html`. Kept for reference; not the plan. The earlier version of this file (2026-09-13) put the CYC on the Kamakiri; that moved to the Kilo on 2026-09-14; the Kilo/CYC split itself was replaced on 2026-09-15 by `straggler-cyc-build.md`.
