# E-Bike Project Reference Document: BBSHD + Baserunner V6 Z9 + JKBMS

This document serves as the master reference guide for integrating a Bafang BBSHD mid-drive motor (with stock controller removed) to a Grin Baserunner V6 Z9 motor controller, powered by a 14s (52V) lithium battery pack managed by a JKBMS (Model: JK-BD4A24S-4P). 

***

### Section 1: BBSHD Motor Internals
*Note: The provided Bafang BBSHD manual is a consumer-level mechanical installation guide. It does not contain internal teardown schematics or bare-wire specifications.*

*   **Phase wire colors and gauge:** NOT IN MANUAL - verify independently.
*   **Hall sensor connector pinout:** NOT IN MANUAL - verify independently.
*   **PAS sensor connector pinout:** NOT IN MANUAL - verify independently.
*   **Thermistor details:** NOT IN MANUAL - verify independently.
*   **Version differences (Version A vs B connectors):** NOT IN MANUAL - verify independently.

***

### Section 2: Baserunner V6 Z9 Controller

#### Pinouts

**Z910 Motor Cable Pinout (9-Pin)**
*   **Phase Wires:** Blue Phase, Green Phase, Yellow Phase
*   **Signal Wires:** 
    *   Hall 5V
    *   Hall GND
    *   Blue Hall
    *   Green Hall
    *   Yellow Hall
    *   Speed/Temp (Can be configured for motor speed, motor temperature, or combined speed/temp)

**WP8 Cycle Analyst Plug Pinout (8-Pin Z812 Higo)**
| Pin | Color | Function |
| :--- | :--- | :--- |
| 1 | Blue | Shunt - |
| 2 | Yellow | Speed |
| 3 | Green | Analog Input 2 [Throttle] |
| 4 | Black | Ground |
| 5 | Grey | Temperature |
| 6 | White | Shunt + |
| 7 | Orange | On/Off |
| 8 | Red | Battery V+ |

**Main9 Signal Plug Pinout (9-Pin Cusmade 1109)**
| Pin | Color | Function |
| :--- | :--- | :--- |
| 1 | Grey | Fwd/Rev |
| 2 | Brown | 5V |
| 3 | Purple | RX |
| 4 | White | Disp TX |
| 5 | Green | Analog Input 1 [Torque/Throttle] |
| 6 | Blue | Analog Input 2 [Throttle/Regen] |
| 7 | Red | Battery V+ |
| 8 | Orange | On/Off |
| 9 | Black | Ground |

**6-Pin PAS / Torque Plug Pinout (6-Pin HiGo MiniB Z609)**
| Pin | Color | Function |
| :--- | :--- | :--- |
| 1 | White | Analog Input 1 [Torque] |
| 2 | Blue | N/C |
| 3 | Green | PAS 1 |
| 4 | Red | 12V |
| 5 | Black | Ground |
| 6 | Yellow | PAS 2 (Shares signal with Main9 Fwd/Rev) |

#### Limits & Configurations
*   **Battery Voltage Limits:** 20V - 60V operating range. For a 14s 52V pack, Low Voltage Cutoff should be set to ~40.6V and Max Regen Voltage to ~58.8V. (Absolute max hardware voltage is 60V).
*   **Current Limits (Z9 Model):** 
    *   Peak Phase Current: 55A
    *   Continuous Phase Current: ~30A (varies with airflow/heatsinking)
    *   Peak Battery Current: 55A (Limited to ~30A continuous based on BMS limits, see Section 3)
*   **On/Off Switch Wiring Requirements:** The Baserunner's On/Off wire (Orange) must be shorted to Battery V+ (Red) via either the WP8 plug or the Main9 plug to power up. If battery power is applied without this connection, the controller will not turn on.
*   **Autotune Procedure Summary:**
    1. Prop bike so the powered wheel and cranks can rotate freely forwards and backwards.
    2. Connect via USB/TTL cable and open Phaserunner Software Suite.
    3. Go to `Basic Setup` -> `Autotune`.
    4. Enter estimated KV (10 is a safe guess) and Effective Pole Pairs (Requires calculating BBSHD internal magnet pairs * gear ratio).
    5. Launch `Static Test` (motor will buzz; detects inductance/resistance).
    6. Launch `Spinning Motor Test` (motor spins at half speed for 15s; determines exact KV and Hall sensor pinout/timing).
*   **Key Software Parameters for Mid-Drive Motors:**
    *   **Virtual Electronic Freewheeling:** Injects a small current (10-30W) to overcome internal motor drag, keeping the drivetrain engaged and eliminating windup delay.
    *   **Wheel Speed Sensing:** Since the BBSHD freewheels, the motor RPM is not tied to wheel speed when coasting. Speed computation requires an external speed sensor routed to `Analog Input 3 (Brk2)`.

***

### Section 3: JKBMS Integration (JK-BD4A24S-4P)

*   **Communication Protocols:** Bluetooth (Standard, via App), UART (Standard GPS/Display interface), RS485 (Optional), CAN (Optional).
*   **Voltage and Current Output Signals:**
    *   **B- (Black):** Connects to the total negative of the battery pack.
    *   **P- (Black):** Connects to the load negative (Baserunner Battery Negative) and charger negative.
    *   **B+ (Red):** The battery's total positive connects directly to the load positive (Baserunner Battery Positive). The BMS strictly manages the negative path.
*   **Temperature Sensor Connections:** Features up to 4 external temperature sensors (NTC) via ports P3 and P4 (T1A/B, T2A/B, T3A/B, T4A/B) to monitor cell/pack temps.
*   **Balance Current Specs:** 0.4A active equalizing current.
*   **Wiring for Baserunner / Cycle Analyst Integration:** 
    *   The JKBMS does *not* natively communicate data directly to the Baserunner or Cycle Analyst via digital comms. 
    *   The Cycle Analyst will rely on the Baserunner's internal 1.00 mΩ shunt for current measurement.
    *   The BMS acts as a standalone hardware protection layer inline with the battery's negative terminal.

***

### Section 4: Wiring Cross-Reference

| Source: BBSHD Internal Component | Target: Baserunner Z910 Connector | Notes |
| :--- | :--- | :--- |
| Phase A / B / C | Blue / Green / Yellow Phase Pins | Colors NOT IN MANUAL. Map directly, FOC will correct order. |
| Hall 5V+ | Hall 5V | NOT IN MANUAL - verify independently. |
| Hall GND | Hall GND | NOT IN MANUAL - verify independently. |
| Hall Sensor A / B / C | Blue / Green / Yellow Hall Pins | Colors NOT IN MANUAL. |
| Thermistor | Speed/Temp Pin | BBSHD thermistor specs NOT IN MANUAL. If equipped, route here and configure Baserunner demux chip. |
| **Source: JKBMS** | **Target: Baserunner** | **Notes** |
| P- (Load Negative) | Battery Ground (Negative) | Connects via custom XT60/Anderson or direct solder. |
| Battery Total Positive (B+) | Battery V+ (Positive) | Bypasses BMS switching directly to the controller. |

***

### Section 5: Troubleshooting Reference

*   **Common Error Codes (Baserunner LED Flashes):**
    *   `1-1`: Controller Over Voltage
    *   `1-2`: Phase Over Current
    *   `1-6`: Motor Hall Sensor Fault
    *   `2-2`: Instantaneous Phase Over Current
    *   `2-4`: Throttle Voltage Outside of Range
    *   `2-6`: Internal Error
*   **Common JKBMS Alarms (via App):**
    *   Charge/Discharge Overcurrent, Charge/Discharge Overtemperature, Cell Overvoltage/Undervoltage, Short Circuit Protection.
*   **Hall Sensor Testing Procedure:**
    *   Open the `Dashboard` tab in the Phaserunner Software Suite. Manually turn the motor backwards one revolution and monitor the "Toggling Hall Signals" transitions to verify hall sensors are reading properly.
*   **Phase Wire Swap Procedure (If motor runs backwards):**
    *   *Do not physically swap the phase wires.* Re-run the Autotune `Spinning Motor Test`. Check the box labeled **"Flip Motor Spin Direction on Next Autotuning?"** and relaunch the test. The Baserunner will correct the rotation in software.
*   **Thermal Protection Settings:**
    *   **Baserunner:** Internal thermal rollback triggers at 90°C (casing ~70°C). External motor rollback is configured in the `Temperature` tab using a 6-point voltage-to-temperature map. 
    *   **JKBMS:** Default Charge/Discharge over-temperature protection is 70°C (configurable in the JK App).

***

### Section 6: Key Specifications Summary

| Specification | Value / Limit |
| :--- | :--- |
| **Max Voltage** | Baserunner: 60V Max (Ideal for 14s/52V packs). JKBMS: 100V Max. |
| **Max Battery Current** | Baserunner: 55A Peak. JKBMS: 40A Continuous, 80A Peak. |
| **Max Phase Current** | Baserunner: 55A Peak, ~30A Continuous. |
| **Wire Gauges Required** | JKBMS: 7 AWG (for B-/P- as shown in diagram). BBSHD/Baserunner specifics NOT IN MANUAL - verify independently. |
| **Connector Types** | Baserunner: HiGo Z910 (Motor), Z812 (WP8), Cusmade 1109 (Main9), Z609 (PAS). JKBMS: HY2.0-15P (Balance), HY2.0-4P (Temp). |
| **Temperature Limits** | Baserunner: 90°C internal before rollback. JKBMS: -30°C to 70°C operating temp. |