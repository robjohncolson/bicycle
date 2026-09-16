# Kilo TT × CYC X1 Pro Gen 4 — Torque-Assist Conversion

> **Superseded 2026-09-15.** The Kilo TT stays on the BBSHD set. CYC is on a **Karate Monkey XL** (`karate-monkey-cyc-build.md`; Straggler path paused). Kamakiri transplant paused. This file is kept for the 32/16 math and the 2026-09-14 decision record. Do not put the CYC on the Kilo.

**Status:** superseded. Kit not ordered.
**Brief (historical):** as bicycle as possible. Torque-sensing pedal assist with a hard launch, full handlebar use on the drops, road hoods, the motor visible but the interface just pedaling. Throttle exists only to carry the bike from spin-out to the motor's RPM ceiling.

The Kilo was going to give up its BBSHD / Baserunner / Superharness / SW102 / 18650 pack as a matched set to the Kamakiri (see `kamakiri-build.md`). That split is off. Frame stays on the Kilo as ridden.

## The order

| Item | Spec |
|---|---|
| Motor kit | CYC X1 Pro Gen 4, **32T bike ring / 53T motor sprocket**, 68/73/83 mm BSA, 160 mm cranks |
| Display | SW102, **36-72 V version** |
| Brake cutoff | CYC magnetic sensors, clamped to the hood levers |
| Throttle | **Thumb** throttle (CYC throttles are 22.2 mm bore; road tops are 23.8 mm, so a twist won't fit) |
| Mount | 22.2 mm accessory stub, 80-100 mm, next to the stem, carrying SW102 + thumb throttle |
| Rear cog | **16T 1/8" fixed cog, on hand** |
| Chain | existing 1/8" style; size with the CYC ring |
| Battery | 14S4P Samsung 50S 21700 on the 100 A Daly. X12 battery current **70 A** to start |

Nothing on the order waits on a measurement.

## Why 32/16

Pedal assist on a mid-drive is cadence-locked: the ring turns with the wheel, and the motor only assists while the cranks push the ring. Ratio therefore sets both launch torque and the pedaled top speed.

| Ring / cog | Launch torque at wheel | Pedal top speed @ 120 rpm | Throttle ceiling @ 52 V |
|---|---|---|---|
| BBSHD 42/20 (today) | 76 Nm | 20 mph | 24-26 mph |
| 40 / 13 | 91 Nm | 29 mph | ~45 mph (power-limited) |
| 40 / 16 | 112 Nm | 24 mph | ~40 mph |
| **32 / 16** | **~150 Nm** | **19 mph** | **~28-30 mph (RPM ceiling)** |

32/16 doubles launch torque, pedals to 19 mph, and the motor's RPM ceiling (~200 ring rpm at 52 V on the 32/53 config) caps throttle speed near 30 mph. The gearing is the speed governor for caliper brakes at 300 lb. Above 19 mph the crank freewheel lets the ring overrun the pedals; soft-pedal and hold the throttle, as on the BBSHD today.

Rejected: 72 V (only raises the RPM ceiling and power at speed; launch torque is phase-current-limited; locks the pack away from the Baserunner). CYC Photon (lighter and quieter but the user wants the Gen 4's torque). New frame (not needed; disc frame + Klampers is a later step). More P (battery current sets how far up the cadence range full torque holds, not launch torque; at 70 A full 280 Nm holds to ~105 rpm after losses, 85 A to ~130; never run 100 A on this pack).

## Setup

1. Pull the BBSHD, Baserunner, Superharness, SW102, throttle, pack. Bag as one set for the Kamakiri.
2. Clean the 68 mm shell faces. Mount the CYC; re-torque the clamp after ride 1 and week 1.
3. 16T cog on, chain sized, chainline measured (ring-to-centerline vs cog-to-centerline within 2-3 mm; single-speed throws chains otherwise).
4. Stub mount, SW102, thumb throttle, brake sensors on the hoods.
5. Pack low in the triangle, XT90-S mate, DMM check first.
6. Ride Control app: assist factor high, torque ramp short, battery current 70 A, then tune down if it lurches at walking pace. Raise toward 80-85 A only if assist sags above 15 mph on climbs; expect the Daly to trip if pushed.
7. Expect the top assist level to surge when stomped; live one level down for cruising.

## Habits

Bolt check after the first five rides then weekly: BB clamp, cog lockring, stem, brake sensors. DMM on the balance connector every few weeks (dumb BMS, no per-group view; the group-3 sag lesson).
