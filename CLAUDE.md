# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hardware documentation repository for a DIY e-bike battery pack project, specifically a 14S4P (14 series, 4 parallel) lithium-ion battery configuration with a JK BMS (Battery Management System). The repository contains technical documentation, wiring guides, and assembly photographs.

**Warning**: This project involves high-voltage electronics (~52V nominal) capable of delivering dangerous current. All documentation includes critical safety warnings.

## Repository Purpose

This is NOT a software project. It's a knowledge repository for:
- E-bike battery pack assembly documentation
- JK BMS wiring instructions
- Visual documentation of the physical assembly process
- Safety guidelines for high-voltage battery construction

## Key Technical Specifications

- **Battery Configuration**: 14S4P (56 cells total: 14 groups in series, 4 cells parallel per group)
- **Voltage**: ~52V nominal (50.4V-58.8V operating range)
- **Layout**: Linear "snake" configuration with groups arranged end-to-end
- **BMS**: JK BMS with Bluetooth capability
- **Cell Type**: 18700 or 21700 lithium-ion cells
- **Current Capacity**: Designed for 30A+ discharge

## Documentation Structure

### Primary Documentation Files

- **wiring_guide.md**: Comprehensive JK BMS wiring guide with Mermaid diagrams showing the battery configuration, step-by-step wiring instructions, and safety verification checklist
- **battery_config.txt**: Forum-sourced technical guide covering the "Copper-Nickel Sandwich" busbar technique, detailed BMS wiring instructions, and assembly best practices

### Supporting Materials

- **5 JPEG images**: High-quality photographs showing the physical battery pack assembly, BMS mounting, and wiring details

## Working with This Repository

### Adding Documentation

When adding new documentation:
1. Maintain the focus on hardware assembly and safety
2. Include clear warnings for any high-voltage procedures
3. Use Mermaid diagrams for wiring schematics where appropriate
4. Add verification checklists for critical assembly steps

### Image Management

- Store assembly photographs with descriptive filenames
- Keep image files under 500KB each for repository efficiency
- Reference images in markdown documentation when illustrating assembly steps

### Safety Documentation Requirements

All documentation involving battery assembly must include:
- Voltage hazard warnings (52V is dangerous)
- Verification steps before connecting power
- Insulation requirements
- Proper wiring sequence to prevent shorts

## Git Workflow

The repository uses a simple git structure:
- Main branch for all documentation updates
- Commit messages should clearly describe what documentation was added or modified
- Use conventional commit format (feat:, fix:, docs:) when appropriate

## Common Tasks

### Updating Wiring Documentation
Edit `wiring_guide.md` or `battery_config.txt` directly. Ensure all voltage values and safety warnings remain accurate.

### Adding Assembly Photos
Place new images in the root directory with descriptive names. Update relevant markdown files to reference new images.

### Creating New Guides
Create new `.md` files for additional assembly procedures. Include appropriate safety warnings and link from existing documentation.

## Important Safety Context

This project deals with:
- High voltage (52V nominal) capable of causing injury
- High current (30A+) requiring proper gauge wiring
- Lithium-ion cells that can cause fires if mishandled
- Spot welding procedures requiring protective equipment

Always prioritize safety information in any documentation updates.