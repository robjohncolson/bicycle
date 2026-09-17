# Surly Straggler 62 × CYC X1 Pro Gen 4 — Drop-bar road bike

**Status:** paused 2026-09-16. Current second bike is **Karate Monkey XL + CYC 32T** (complete + kit both ordered 2026-09-16/17) — see `karate-monkey-cyc-build.md`. Kilo TT stays as-is.
**Brief (historical):** new bike. Track/messenger pedal feel (50/20), torque-sensing PAS, drop bars, mechanical discs.

This file is the drop-bar / 40T / 135 QR / Andra 321 path. Kept; not the order. `kilo-cyc-build.md` and the Kamakiri transplant remain superseded/paused. Kilo bible remains `kilo-tt-ebike-build.html`.

## Why this bike

The Kilo works. Pulling it apart to “upgrade” it wastes a proven platform. This frame is the disc Kilo the industry actually sells: steel, drops, 700c, 68 mm BSA, singlespeed-capable dropouts, size 62.

42/20 on the BBSHD is the **lowest gear the rider can comfortably pedal**. Hills on that bike are a throttle blip, no lug. 50/20 (Schwinn Madison long-distance gear; 44/16 felt quick then beat up the knees) is the honest road ratio. CYC 280 Nm at the crank still makes more wheel torque at 40/16–40/17 than the BBSHD does at 42/20, so the compromise gear can go.

## The bike

| | |
|---|---|
| Frame | **Surly Straggler 700c, 62 cm**, old generation (black). Forward-exit **10 × 135 mm QR** horizontal dropouts, **10 × 100 mm QR** front, **IS 51 mm disc, 160 mm max rotor**, 68 mm BSA, EC34 headset, 27.2 mm post |
| Fit | Rider 190 cm / 6'3", 300 lb. Straggler 62: stack 628 / reach 421 / standover 865. Kilo 63: stack ~606 / reach ~456 / standover **898**. Extra standover is free; a long stem recovers reach if the cockpit feels short |
| Tires | 700 × 38–42 (frame clears ~47–50 without fenders, ~41 with) |
| Brakes | Mechanical disc, **Paul Klampers** (short-pull for drop levers), **160 mm** 6-bolt. Magnetic CYC sensors on the hoods |

160 mm at 300 lb is the class limit on this frameset. Treat ~40 mph as a chosen blast, not a brake-design speed. Same ceiling as Midnight Special / Nature Boy.

## Drive

| | |
|---|---|
| Motor | **CYC X1 Pro Gen 4**, X12, **40T bike ring / 72T motor sprocket** (not 32T/53T). 68/73 mm BSA. **160 mm cranks** (165 mm if Johnny has no 160; not 175) |
| Display | SW102, **36–72 V** |
| Throttle | **Thumb** on a 22.2 mm stub (CYC bores will not fit 23.8 mm road tops) |
| Brake cutoff | CYC magnetic sensors, clamped to the hood levers |
| Battery | 14S4P Samsung 50S 21700 on the 100 A Daly. X12 battery current **70 A** to start. Group-3 under-load sag still open — diagnose before 70 A (see CONTINUATION_PROMPT 2026-06-06) |
| Connector | XT90-S pack side |

### Gearing — 40T + CYC 5-speed, home is 17T

Stock CYC ring is **104 BCD narrow-wide, 9–12 speed** (3/32″ / 11/128″). **Not 1/8″.** Track cogs on the Kilo (screw-on 1.37″ × 24, 1/8″) do **not** fit an HG freehub. Keep them on the Kilo.

Cassette: CYC HD **15–17–20–24–30**, chromoly, HG. Johnny Nerd Out sells **cassette only** (~$179) — do not buy the full HD kit (148 mm hub + flat-bar Advent trigger).

| Cog | Ratio | What it is |
|---|---|---|
| 15T | 2.67 | Madison 44/16 — snap, then knees |
| **17T** | **2.35** | **Home. Closest to 50/20** (a bit easier) |
| 20T | 2.00 | At or under the 42/20 floor — pedal a steep one instead of blipping |
| 24T / 30T | 1.67 / 1.33 | Tractor. Will not be pedaled for fun |

Exact 50/20 is 40/16; the cassette has no 16T. 17T is the honest gear.

**Speeds, 40/17-ish on 700c, 52 V** (40/16 numbers; 17T is a hair slower):

| | ~Speed |
|---|---|
| Pedal @ 90 rpm (50/20 feel) | **~18 mph** |
| PAS spin-out @ 120 rpm | **~24 mph** |
| Throttle rpm wall | **~44 mph** no-load · **~40–43** on the road |

40/15 PAS ~25–26, throttle ~47 no-load. Wider 700×38–40 adds ~1 mph on paper (taller tire), may give it back to aero.

**Hill, throttle:** same pitch that is a blip on BBSHD 42/20. 40/15–40/17 is taller, so more crank torque is required for the same wheel shove (~27% more). CYC still has more wheel torque (~105–112 Nm vs ~76 Nm) and 70 A vs 30 A, and no Power Map foldback at low rpm. It goes up *better*, not merely *still*. First-ride: X12 at low rpm is more sudden than the Baserunner — shorten torque ramp in the app if it lunges.

Shifter: **friction**, downtube (Straggler has the bosses) or bar-end. Not the Advent Trail Pro flat-bar trigger. Roll off throttle, then shift. No gear sensor.

## Wheels

| | |
|---|---|
| Hubs | **Hope Pro 5, 36h, 6-bolt.** Front 100 mm QR. Rear **135 mm QR, Shimano HG Steel** freehub (not alloy). E-bike pawls. Takes the CYC cassette; 5-speed cluster needs **HG spacers** so the lockring clamps and **17T sits near 51 mm chainline** (CYC 40T on 68 mm ≈ 51 mm) |
| Rims | **Ryde Andra 321 Disc, 700c, 36h, both wheels.** 21 mm internal, 23–45 mm tires, disc-only, e-bike/touring load. Same rim front and rear. Fallback: Andra 30 Disc 36h. Not TB14 / Deep V / Araya 720 on this bike (too narrow, not a motor-load rear) |
| Build | 36h, **3-cross** both sides, DT Alpine III or Sapim Force, brass nipples |
| Skewer | Steel QR, fully tight, axle parked on the dropout **adjusters** so the rotor stays in the caliper. Horizontal + 280 Nm will walk a cheap QR |

Kilo preference (H+Son/Araya lo-pro front, Araya 720 30 mm V rear) is rim-brake 23–28 mm. Noted; not copied.

## Johnny Nerd Out order (kit)

[CYC X1 Pro Gen 4](https://www.johnnynerdout.com/product-page/cyc-x1-pro-gen-4-mid-drive-motor-3500w-48-72v)

| Dropdown | Pick |
|---|---|
| BB / chainring | **68/73 mm + 40T** (not 32T) |
| Brake sensors | Yes |
| Throttle | Thumb |
| Cranks | **160 mm** if listed, else **165 mm** |
| Display | SW102, 36–72 V |

Plus [CYC HD 5-speed cassette only](https://www.johnnynerdout.com/product-page/cyc-heavy-duty-5-speed-cassette). Derailleur: Microshift Advent clutch short-cage, bought separately. Chain: KMC e9 Turbo.

Print CYC’s 1:1 **40T/72T** chainstay template against the 62’s drive-side yoke before the motor ships. 430 mm stays, 40T is the largest stock ring.

## Why not 32T

32/15 = 2.13 = today’s 42/20. Every cog would feel like a granny. 32T is CYC’s max-torque catalog default. Ignore it.

## Frames considered and dropped

| Frame | Why not |
|---|---|
| Keep CYC on the Kilo (`kilo-cyc-build.md`) | Kilo works. Don’t cannibalize it |
| Midnight Special 60/64 | No 62. 64 is twitchy (74° / ~53 mm trail). 12×142. Endurance road-plus is tire volume, which the Straggler already has at 38–42 |
| Salsa Fargo Ti M | Size M is 5'8"–6'0". Even XL is slack 29er, 36T max 1× ring, carbon fork, 161 kg system cap, ~$3k |
| Steamroller | Actual track geo. No discs |
| Nature Boy Disc 61 | Closest *spirit* (SS CX). Max 61, shorter reach, have to find one |
| Karate Monkey / Krampus / Photon / 72 V | Dropped 2026-09-12–14 |

There is no 63 cm steel **track** frame with discs. Straggler 62 is the disc cousin.

## Torque vs BBSHD 42/20 (~76 Nm at the wheel)

| Setup | Wheel torque | vs Kilo 42/20 |
|---|---|---|
| BBSHD 42/20 | ~76 Nm | 1.0× |
| CYC 40/17 (home) | ~110 Nm | ~1.4× |
| CYC 40/16 (exact 50/20) | ~112 Nm | ~1.5× |
| CYC 40/15 (Madison) | ~105 Nm | ~1.4× |

~30% more *capability* on the same hill, not 30% less hill. Taller gear asks more crank torque at lower rpm; 280 Nm and 70 A still leave more reserve than the Z9 at 30 A / Power Map.

## Setup (draft)

1. Frameset + headset + fork. Confirm JIS/ISO cups (EC34).
2. Print 40T/72T template at the BB and chainstay yoke.
3. Build both 36h wheels (Hope + Andra 321 Disc). Record tensions.
4. Klampers, 160 mm rotors, bed-in.
5. CYC in clean 68 mm shell. Re-torque clamp after ride 1 and week 1.
6. Cassette + spacers (17T at ~51 mm chainline), Advent derailleur, friction shifter, e9 chain.
7. Stub: SW102 + thumb throttle. Sensors on the hoods.
8. Pack low in the triangle, XT90-S, DMM before first mate.
9. Ride Control: assist high, torque ramp short, battery current 70 A. Tune down if it lunges at walking pace. Do not run 100 A on this pack.

## Habits

Bolt check after the first five rides then weekly: BB clamp, cassette lockring, QR skewers, stem, brake sensors, rotor bolts. DMM on the 21700 balance connector every few weeks (dumb Daly, no per-group view; the group-3 sag lesson).

## Safety (same rails as the Kilo bible)

~52 V nominal, 58.8 V full. One-hand rule, DMM before every connector mate, insulated tools on the live stack. XT90-S for the X12 input caps. Floating pack negative unless a later decision bonds it.
