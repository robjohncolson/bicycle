# Detailed Wiring Diagram - 14S4P Battery Pack with JK-Weld BMS

## Physical Layout Diagram

```mermaid
graph TB
    subgraph Pack["14S4P Linear Battery Pack - Physical Layout"]
        direction LR

        subgraph G1["Group 1 (4P)"]
            direction TB
            C1_1((Cell 1))
            C1_2((Cell 2))
            C1_3((Cell 3))
            C1_4((Cell 4))
        end

        subgraph G2["Group 2 (4P)"]
            direction TB
            C2_1((Cell 5))
            C2_2((Cell 6))
            C2_3((Cell 7))
            C2_4((Cell 8))
        end

        subgraph G3["Group 3 (4P)"]
            direction TB
            C3_1((Cell 9))
            C3_2((Cell 10))
            C3_3((Cell 11))
            C3_4((Cell 12))
        end

        subgraph Dots1["..."]
            direction TB
            dots1[Groups 4-12]
        end

        subgraph G13["Group 13 (4P)"]
            direction TB
            C13_1((Cell 49))
            C13_2((Cell 50))
            C13_3((Cell 51))
            C13_4((Cell 52))
        end

        subgraph G14["Group 14 (4P)"]
            direction TB
            C14_1((Cell 53))
            C14_2((Cell 54))
            C14_3((Cell 55))
            C14_4((Cell 56))
        end
    end

    G1 -.->|Nickel Strip| G2
    G2 -.->|Nickel Strip| G3
    G3 -.->|Series Connection| Dots1
    Dots1 -.->|Series Connection| G13
    G13 -.->|Nickel Strip| G14

    style G1 fill:#e3f2fd,stroke:#1976d2
    style G14 fill:#ffebee,stroke:#d32f2f
```

## BMS Wiring Schematic

```mermaid
graph LR
    subgraph Battery["Battery Pack (14S4P)"]
        B_NEG["B- (Group 1 Negative)"]
        B_POS["B+ (Group 14 Positive)"]

        B1P["Group 1 Positive"]
        B2P["Group 2 Positive"]
        B3P["Group 3 Positive"]
        B4P["Group 4 Positive"]
        B5P["Group 5 Positive"]
        B6P["Group 6 Positive"]
        B7P["Group 7 Positive"]
        B8P["Group 8 Positive"]
        B9P["Group 9 Positive"]
        B10P["Group 10 Positive"]
        B11P["Group 11 Positive"]
        B12P["Group 12 Positive"]
        B13P["Group 13 Positive"]
    end

    subgraph JK_BMS["JK-Weld BMS"]
        BMS_B_NEG["B- Terminal (Blue Wire)"]
        BMS_P_NEG["P- Terminal (Black Wire)"]

        BAL0["Balance 0 (Black)"]
        BAL1["Balance 1"]
        BAL2["Balance 2"]
        BAL3["Balance 3"]
        BAL4["Balance 4"]
        BAL5["Balance 5"]
        BAL6["Balance 6"]
        BAL7["Balance 7"]
        BAL8["Balance 8"]
        BAL9["Balance 9"]
        BAL10["Balance 10"]
        BAL11["Balance 11"]
        BAL12["Balance 12"]
        BAL13["Balance 13"]
        BAL14["Balance 14 (Red)"]
    end

    subgraph Output["Output Connectors (XT90)"]
        XT90_POS["XT90 Positive (Yellow)"]
        XT90_NEG["XT90 Negative (Black)"]
    end

    %% Main Power Connections
    B_NEG ==>|"Thick Blue Wire"| BMS_B_NEG
    BMS_P_NEG ==>|"Thick Black Wire"| XT90_NEG
    B_POS ==>|"Direct Connection"| XT90_POS

    %% Balance Wire Connections
    B_NEG -.->|"Balance Wire 0"| BAL0
    B1P -.->|"Balance Wire 1"| BAL1
    B2P -.->|"Balance Wire 2"| BAL2
    B3P -.->|"Balance Wire 3"| BAL3
    B4P -.->|"Balance Wire 4"| BAL4
    B5P -.->|"Balance Wire 5"| BAL5
    B6P -.->|"Balance Wire 6"| BAL6
    B7P -.->|"Balance Wire 7"| BAL7
    B8P -.->|"Balance Wire 8"| BAL8
    B9P -.->|"Balance Wire 9"| BAL9
    B10P -.->|"Balance Wire 10"| BAL10
    B11P -.->|"Balance Wire 11"| BAL11
    B12P -.->|"Balance Wire 12"| BAL12
    B13P -.->|"Balance Wire 13"| BAL13
    B_POS -.->|"Balance Wire 14"| BAL14

    style B_NEG fill:#2196f3,color:white
    style B_POS fill:#f44336,color:white
    style XT90_POS fill:#ffeb3b
    style XT90_NEG fill:#212121,color:white
```

## Wire Gauge and Connection Table

| Connection Type | Wire Color | Wire Gauge | Purpose | Current Rating |
|-----------------|------------|------------|---------|----------------|
| B- Main | Blue | 10-12 AWG | Main negative to BMS | 30A+ |
| P- Discharge | Black | 10-12 AWG | BMS to XT90 negative | 30A+ |
| Main Positive | Red/Yellow | 10-12 AWG | Group 14 to XT90 positive | 30A+ |
| Balance Wires | Multi-color | 22-24 AWG | Cell voltage monitoring | <1A |
| Nickel Strips | Silver | 0.15-0.2mm | Series connections | 30A+ |

## Physical Assembly Notes

Based on your photos:

1. **Battery Layout**: Linear configuration with cells arranged in a single long line
2. **BMS Position**: Mounted on top of the battery pack, centered
3. **Shrink Wrap**: Blue/teal heavy-duty shrink wrap for protection
4. **Output Connector**: XT90 connector (yellow = positive, black = negative)
5. **Insulation**: Kapton tape visible on connections, fish paper between BMS and cells

## Connection Sequence (CRITICAL)

```mermaid
graph TD
    A[1. Spot weld all parallel groups] --> B[2. Connect groups in series with nickel strips]
    B --> C[3. Solder B- wire to Group 1 negative]
    C --> D[4. Solder all balance wires to respective points]
    D --> E[5. Verify voltages with multimeter]
    E --> F{Voltages Correct?}
    F -->|No| G[Fix wiring error]
    G --> E
    F -->|Yes| H[6. Connect balance plug to BMS]
    H --> I[7. Connect P- wire to output]
    I --> J[8. Connect main positive to output]
    J --> K[9. Insulate and shrink wrap]

    style A fill:#e8f5e9
    style E fill:#fff3e0
    style F fill:#ffebee
    style K fill:#e3f2fd
```

## Safety Verification Checklist

Before connecting the BMS:

- [ ] All parallel groups show identical voltage (±0.05V)
- [ ] Series connections verified with multimeter
- [ ] Balance wire 0 to wire 1: ~3.6-4.2V
- [ ] Balance wire 0 to wire 2: ~7.2-8.4V
- [ ] Balance wire 0 to wire 3: ~10.8-12.6V
- [ ] Continue pattern for all 14 balance wires
- [ ] Balance wire 0 to wire 14: ~50.4-58.8V (total pack voltage)
- [ ] No shorts between adjacent balance wires
- [ ] All connections insulated with Kapton tape
- [ ] Fish paper installed between BMS and cells

## Current Flow Paths

```mermaid
graph LR
    subgraph Discharge["Discharge Path"]
        D1[Group 1 Neg] --> D2[BMS B-]
        D2 --> D3[BMS Internal FET]
        D3 --> D4[BMS P-]
        D4 --> D5[XT90 Negative]
        D6[Group 14 Pos] --> D7[XT90 Positive]
    end

    subgraph Charge["Charge Path"]
        C1[Charger Negative] --> C2[XT90 Negative]
        C2 --> C3[BMS P-]
        C3 --> C4[BMS Protection]
        C4 --> C5[BMS B-]
        C5 --> C6[Group 1 Neg]
        C7[Charger Positive] --> C8[XT90 Positive]
        C8 --> C9[Group 14 Pos]
    end

    style D1 fill:#2196f3
    style D6 fill:#f44336
    style C1 fill:#4caf50
    style C7 fill:#ff9800
```