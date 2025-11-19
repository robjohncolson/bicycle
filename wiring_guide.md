# JK BMS Wiring Guide for 14S4P Linear Battery Pack

This guide provides visual and step-by-step instructions for wiring a JK BMS to a 14S4P battery pack in a linear "snake" configuration.

## ⚠️ Critical Safety Warnings

> [!DANGER]
> **High Voltage Hazard**: A 14S battery pack is ~52V nominal and can deliver dangerous current.
> *   **Never** plug the balance connector into the BMS until **ALL** wires are soldered and verified.
> *   **Insulate** every connection immediately after making it.
> *   **Double-check** polarity before connecting anything.

## 1. Battery Configuration Diagram

The following diagram illustrates the "snake" layout of the 14 groups and the BMS connection points.

```mermaid
graph TD
    subgraph Battery_Pack ["14S4P Linear Pack (Snake Layout)"]
        direction TB
        G1[Group 1 (-)] ---|Series| G2[Group 2]
        G2 ---|Series| G3[Group 3]
        G3 ---|Series| G4[Group 4]
        G4 ---|Series| G5[Group 5]
        G5 ---|Series| G6[Group 6]
        G6 ---|Series| G7[Group 7]
        G7 ---|Series| G8[Group 8]
        G8 ---|Series| G9[Group 9]
        G9 ---|Series| G10[Group 10]
        G10 ---|Series| G11[Group 11]
        G11 ---|Series| G12[Group 12]
        G12 ---|Series| G13[Group 13]
        G13 ---|Series| G14[Group 14 (+)]
    end

    subgraph JK_BMS ["JK BMS Connections"]
        B_Minus((B- Thick Blue)) -->|Connects to| G1
        Balance_0((Wire 0 Black)) -->|Connects to| G1
        Balance_1((Wire 1)) -->|Connects to| G1
        Balance_2((Wire 2)) -->|Connects to| G2
        Balance_3((Wire 3)) -->|Connects to| G3
        Balance_4((Wire 4)) -->|Connects to| G4
        Balance_5((Wire 5)) -->|Connects to| G5
        Balance_6((Wire 6)) -->|Connects to| G6
        Balance_7((Wire 7)) -->|Connects to| G7
        Balance_8((Wire 8)) -->|Connects to| G8
        Balance_9((Wire 9)) -->|Connects to| G9
        Balance_10((Wire 10)) -->|Connects to| G10
        Balance_11((Wire 11)) -->|Connects to| G11
        Balance_12((Wire 12)) -->|Connects to| G12
        Balance_13((Wire 13)) -->|Connects to| G13
        Balance_14((Wire 14 Red)) -->|Connects to| G14
        
        P_Minus((P- Thick Black)) -->|To Controller (-)| Load_Neg[Load Negative]
    end
    
    G14 -->|Main Positive (+)| Load_Pos[Load Positive]
    
    style G1 fill:#e1f5fe,stroke:#01579b
    style G14 fill:#ffebee,stroke:#b71c1c
    style B_Minus fill:#2196f3,color:white
    style P_Minus fill:#212121,color:white
```

## 2. Wiring Steps

### Step 1: Main Power Connections
1.  **B- (Blue/Black thick wire)**: Solder securely to the **Main Negative** terminal (Negative pole of Group 1).
2.  **P- (Black thick wire)**: This is your discharge output. Connect to your connector (e.g., XT90) going to the controller.
3.  **Main Positive**: Connect your discharge connector's Positive wire directly to the **Main Positive** terminal (Positive pole of Group 14).

### Step 2: Balance Leads (The "Thin Wires")
*Route these wires neatly along the side of the pack, taping them down with Kapton tape.*

| Wire Color/Number | Connection Point | Description |
| :--- | :--- | :--- |
| **Black (Wire 0)** | **Group 1 (-)** | Main Negative (Same as B-) |
| Wire 1 | **Group 1 (+)** | Positive of 1st Group |
| Wire 2 | **Group 2 (+)** | Positive of 2nd Group |
| Wire 3 | **Group 3 (+)** | Positive of 3rd Group |
| ... | ... | ... |
| Wire 13 | **Group 13 (+)** | Positive of 13th Group |
| **Red (Wire 14)** | **Group 14 (+)** | Main Positive |

## 3. Verification Checklist (Before Plugging In)

Use a multimeter to measure the voltage between the **Black (Wire 0)** pin on the connector and each subsequent pin.

- [ ] **Pin 0 to Pin 1**: ~3.6V - 4.2V
- [ ] **Pin 0 to Pin 2**: ~7.2V - 8.4V
- [ ] **Pin 0 to Pin 3**: ~10.8V - 12.6V
- [ ] ... increasing by ~3.6V-4.2V each step ...
- [ ] **Pin 0 to Pin 14**: ~50.4V - 58.8V (Total Pack Voltage)

> [!IMPORTANT]
> If any voltage reading is "weird" (e.g., 0V, negative, or double the expected jump), **STOP**. You have a wiring error. Do not plug in the BMS.

## 4. Final Assembly
1.  **Plug in BMS**: Only after passing the checklist.
2.  **Activate BMS**: Some JK BMS units require a charge voltage to be applied to P- and B+ to "wake up" for the first time, or use the button if equipped.
3.  **Insulate**: Wrap the entire BMS and wiring area with fish paper or fiberglass board before shrink wrapping.
