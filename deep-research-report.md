# Kilo TT Track-to-E-Assist Build Spec and Checklist Reconciliation

## Build snapshot and design envelope

This build converts a classic track-style platform into a throttle-driven e-assist bike by running a controller-removed BBSHD-class mid-drive as a **bare sensored BLDC motor** (3 phases + Hall sensors + optional thermistor) powered by a **Baserunner V6_Z9 field‑oriented controller**, commanded through a **Superharness + KM5s display** stack rather than a Cycle Analyst. That architecture is explicitly supported by the Baserunner V6 manual (Cycle Analyst mode, Superharness / 3rd‑party display mode, and headless mode). citeturn14view0

The system is operating close to the controller’s voltage ceiling: the Baserunner line is specified with **60 V max input** (20–60 V operating range), which corresponds to **14s Li‑ion (58.8 V full charge)** but leaves little margin for regen voltage rise and wiring transients. citeturn13view0turn14view0 This makes “regen settings + BMS charge limits + precharge/anti‑spark practices” a first‑class design constraint, not an afterthought.

A consolidated “total spec” (as confirmed by your notes + authoritative references):

| Subsystem | Your selected hardware | Fit / rating highlights that matter |
|---|---|---|
| Frame & geometry | 63cm Kilo TT platform from entity["company","BikesDirect","online bicycle retailer"] / entity["company","Cycles Mercier","bicycle brand"] | 120 mm rear spacing; 68 mm BB; threadless 1″ headset; stock seatpost spec is 26.8 mm; fork offset for 55–63 sizes is 28 mm; head tube angle 75° for 55–63 sizes. citeturn26view0turn25search11turn25search0 |
| Fork | entity["company","Wound Up Composites","bicycle fork maker"] Zephyr 1″ (steel steerer) | 35 mm rake, 368 mm axle‑to‑crown; max recommended spacer stack 44 mm; 1″ steel steerers use 26.4 mm race diameter. citeturn12view0turn2search0turn2search3 |
| Motor | entity["company","Bafang Electric (Suzhou) Co., Ltd.","ebike motor maker, suzhou cn"] BBSHD-class mid motor run as external‑controller BLDC | Official Bafang M615/MM G320 750/1000 family lists up to 1000 W rated and 160 N·m max torque (vendor naming can vary; treat thermal limits conservatively). citeturn11search7turn5search3 |
| Motor controller | entity["company","Grin Technologies Ltd","ebikes.ca maker, vancouver bc"] Baserunner V6_Z9 | 20–60 V operating range; Z910 motor plug; Z9 model is characterized as 55 A peak phase / ~30 A continuous and “perfect for small 250–500 W hub motors,” implying you’re using it in a non‑typical (higher torque) application and must current‑limit accordingly. citeturn13view0turn14view0turn13view1 |
| Harness & UI | Superharness + entity["company","Star Union","ebike display maker"] SW102 (KM5s) + DYOL bidirectional throttle | Baserunner manual explicitly supports “3rd party display hookup with Superharness” and notes compatible KM5s‑style ecosystems. citeturn14view0turn7search0turn7search1 |
| Battery & BMS | 14s4p 18650 pack + JK‑BD4A17S4P (active balance) from entity["company","Chengdu Jikong Technology Co., Ltd.","jk bms maker"] | BD4AxxS‑4P manual: “charging activation mode” with charger voltage ~2 V higher than pack; default Bluetooth password behavior; configurable charge/discharge MOS control. citeturn15view0 |
| Wheels | entity["company","Shimano","bicycle components maker"] Dura‑Ace 7600 track hub (fixed/fixed) + entity["company","H Plus Son","bicycle rim brand"] TB14 rims | Track hubs use stepped threads and a left‑hand lockring thread; TB14 published specs include 14.1 mm depth, 23 mm outer width, ERD 610, ~490 g. citeturn24view0turn24view1turn28view0 |
| Tires | entity["company","Panaracer","bicycle tire maker"] Pasela 700×23 | 23 mm tires are compatible with the stock frame and far below the Zephyr’s 700×28 max clearance; pressure and ride feel depend on your casing and load. citeturn2search0turn5search2 |
| Brakes | entity["company","Dia-Compe","bicycle brake maker"] Gran Compe 9000Ti calipers | Commonly listed reach is 39–49 mm (some listings show 39–51 mm); you should measure your actual bolt‑to‑rim track distance with your wheel/tire before final fork cut. citeturn5search1turn21view0 |
| Saddle & seatpost | entity["company","Berthoud Cycles","french saddle maker"] Galibier + entity["company","Nitto","japanese bicycle components"] S‑83 (26.8) | Galibier: intended for low/aggressive positions; weight varies by source/hide; S‑83 exists in 26.8 and 27.2 diameters and 250/300 lengths, with 44 mm clamp width. citeturn23search17turn23search0turn22view0turn22view1 |

The current build-bible HTML you provided is the baseline for this reconciliation. fileciteturn0file0

## Motor controller and controls stack

The **Baserunner V6** is a field‑oriented controller that “must be tuned to your motor for proper operation,” with the Z9 model described as intended for “smaller motors” using the Z910 plug. citeturn14view0turn13view0 That’s the key engineering mismatch in your design: the controller will *run* a sensored BLDC if you provide correct phase/Hall wiring and tuning, but the platform narrative (“250–500 W hub motors”) means you should treat battery and phase current limits as a protection strategy for controller thermals, connectors, and wiring. citeturn13view0turn14view0

Superharness mode is explicitly supported as a Baserunner wiring strategy; in this mode the display provides assist-level UI and power control, while the Superharness provides signal conditioning so you can mix throttle and braking devices without reconfiguring the controller. citeturn14view0turn13view0turn7search5 The SW102 is a KM5s display and is sold as a compatible display option for Baserunner OEM systems. citeturn7search0turn13view0

Firmware and software remain gating items for a successful “display + Superharness” setup:
- The Baserunner ecosystem uses the Phaserunner software suite, and Grin’s product pages explicitly warn that Superharness setups require newer software versions (and historically required firmware updates when pairing with third‑party displays). citeturn13view0turn14view0  
- Grin also documents a known KM5s measurement scaling issue in their Superharness documentation (display current/watts not matching actual under certain firmware). citeturn8search0  

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Grin Baserunner V6 Z9 controller photo","Grin Superharness Main9 harness photo","SW102 KM5s ebike display photo","DYOL bidirectional ebike throttle"],"num_per_query":1}

Speed sensing remains the biggest “mid‑drive gotcha.” The Baserunner manual is explicit that for mid‑drives (and freewheeling/geared systems), motor RPM is *not* directly tied to wheel speed and you need another speed input if you want correct vehicle speed and speed limiting behavior. citeturn14view0turn13view0 In practice, that means either adding a wheel magnet pickup (1 pulse/rev) or using a supported combined temp/speed signal mode if you also want temperature on the same line. citeturn13view0turn14view0

## Frame, fork, and cockpit interface constraints

Your frame choice has several hard constraints that strongly shape the build:

The Kilo TT listing explicitly calls out a **threadless 1″ headset**, **68×108 sealed cartridge BB**, **120 mm dropout spacing**, a **26.8 mm seatpost**, and a seat clamp torque spec of **6 N·m** (stock configuration). citeturn26view0 The official geometry table shows that size 55–63 uses a **75° head tube angle** and **28 mm fork offset**, and the 63 cm size has a 630 mm top tube and 1023 mm wheelbase. citeturn25search11turn25search0

Your fork swap changes handling in a predictable way: Zephyr uses **35 mm rake** at the same 368 mm axle‑to‑crown as the stock geometry expectations. citeturn12view0turn2search0turn25search11 With a 75° head tube angle and ~668 mm tire outer diameter (700×23), trail computes to ~60.5 mm with 28 mm offset (matching BikeInsights’ derived trail), and about **53.3 mm** with 35 mm offset—a reduction of ~7.25 mm. citeturn25search0turn25search11turn10search30  
Because trail is widely treated as a primary steering stability factor (more trail → more self-centering; less trail → quicker steering), this change supports your report’s warning that loaded riding should be tested progressively. citeturn25search14turn24view1

Cockpit fit is unusually “spec‑sensitive” on your chosen bar:
- The B263-family bullhorn spec is **25.4 mm handlebar clamp** and **17 mm inner diameter** (bar-end), which constrains aerobar clamps and bar‑end brake lever options. citeturn21view0turn21view1  
- The B263AA listing also explicitly states the lever clamp section is **22.2 mm**, which is favorable for most e‑bike throttles and MTB-style controls. citeturn21view1  

## Wheels, brakes, tires, and drivetrain reality checks

The single biggest discrepancy to correct in your earlier text is the **track hub threading explanation**. Track hubs use a stepped thread: the sprocket thread is the standard 1.37″×24 TPI, and outboard is a smaller **left‑hand** lockring thread commonly specified as **English/ISO 1.29″×24 TPI**. citeturn24view0turn24view1  
This matters because your plan includes running **fixed on one side and a freewheel on the other**: the freewheel compatibility is real (same main thread standard), but you should not generalize it as “1.37×24 both sides” without also respecting the lockring function and the need to verify shoulder/spacer clearance. citeturn24view0turn24view1

Your TB14 rim spec numbers are well supported: published TB14 details include 14.1 mm depth, 23 mm outside width, ERD 610, and ~490 g. citeturn28view0 If your rims are anything other than TB14 (or if they are upgraded from the frame’s stock wheelset), ERD must be verified before ordering spokes.

Brake system fit is still “measure, then commit.” Retail sources commonly list the Dia‑Compe 9000Ti reach as 39–49 mm, but you can find 39–51 mm in other listings; the safe approach is to measure bolt‑to‑brake‑track distance with your installed wheel/tire on both fork and frame. citeturn5search1turn21view0

Tire choice is compatible but potentially limiting: 700×23 is well below the Zephyr’s maximum 700×28 clearance and aligns with a track-style build, but for a cargo‑capable e‑assist configuration you should be aware that smaller tires generally provide less pneumatic suspension and can feel harsher at higher loads; Pasela’s published information supports the high‑pressure “road” intent of the 23 mm size. citeturn2search0turn5search2

## Battery system and BMS integration

Your battery system is a 14s4p Li‑ion pack (58.8 V full charge), governed by a JK BD4A-series active balancing BMS that is explicitly described as a “charging activation mode” device (no physical power switch) requiring charger voltage about **2 V higher than battery voltage** to wake. citeturn15view0 This aligns with your plan to commission the battery side by connecting a charger first, before attaching the controller under load.

Two safety-critical electrical implications follow from the manuals:

The GPS/UART-style auxiliary port on JK BMS families is commonly documented with a **VGPS pin described as “voltage close to B+”** and UART TX/RX at **3.3 V logic**, meaning that careless handling can put near-pack voltage on small-pitch connector pins adjacent to logic pins. citeturn20search6 Even if you do not intend to use telemetry immediately, this is worth calling out in the checklist as a “cap/insulate and ignore unless needed” item.

Charge-current limits must be reconciled across controller + BMS: the Baserunner is explicitly programmable for regen voltage/current behavior and supports powerful regen; the BMS has configurable maximum charging current and will open the charge MOS on a charge overcurrent event (as described in the JK manual behavior). citeturn14view0turn15view0 In practice, you should treat regen as **disabled or tightly limited** until (a) the mid-drive drivetrain proves it can backdrive the motor and (b) the BMS charge-current and overvoltage thresholds are set with intention.

Your attached pack photos are valuable for checklist enforcement: they show the pack in an “open” state with the BMS mounted and harnesses routed, and a “wrapped” state with the main discharge lead exiting to a yellow high-current connector. The updated HTML checklist below embeds these photos directly so you can use them as a “compare against this” reference before final closure.

## Discrepancy log and what changed in the updated build-bible HTML

These are the actionable discrepancies (or “potentially misleading simplifications”) that required correction:

The rear hub threading description needed to be upgraded from a simplified “1.37×24 both sides” phrasing to the stepped-thread + lockring reality (and the lockring’s role in safety). citeturn24view0turn24view1

JK BMS “activation headroom” is not universal across all JK documents. Your BD4AxxS‑4P manual says ~+2 V (charger above pack), while other JK documentation families sometimes state higher; the corrected guidance is “start at +2 V, and if it won’t wake near full charge, adjust conditionally without exceeding cell limits.” citeturn15view0turn6search3

Saddle weight claims vary by seller and hide; Berthoud’s own product page cites ~365 g (acknowledging hide variability), while Rene Herse lists 345 g in its specs, and a Berthoud comparison article states 346 g. The corrected spec is “~345–365 g depending on leather and version,” not a single fixed number. citeturn23search17turn23search0turn23search12

The build’s steering geometry effect is now quantified using the published Kilo TT geometry (75° / 28 mm offset) and Zephyr spec (35 mm rake), producing an estimated ~7.25 mm reduction in trail with a 700×23 tire diameter consistent with the BikeInsights build model. citeturn25search11turn12view0turn25search0turn10search30

The output file you asked for—a comprehensive HTML “build bible” that includes total spec + checklists + a discrepancy section and the embedded pack photos—has been updated accordingly.

[Download the updated build spec & checklist HTML](sandbox:/mnt/data/kilo-tt-ebike-build_v2.2.html)