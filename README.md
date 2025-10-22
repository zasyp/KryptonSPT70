# Plasma Parameters Calculation for Hall Effect Thruster (SPD)

This project contains calculations for plasma parameters in a Stationary Plasma Thruster (SPD) using krypton as the working gas.

## Overview

The code calculates various plasma parameters including:
- Particle velocities (electrons, ions, neutrals)
- Particle concentrations
- Plasma parameters (Debye radius, plasma frequency, Coulomb logarithm)
- Collision cross-sections and frequencies
- Mean free paths
- Hall parameters

## Input Parameters

The calculations are based on experimental data for three measurement points at distances of 10, 20, and 30 mm from the thruster:

- **Distances**: 10, 20, 30 mm
- **Plasma potential**: 199.3, 186.1, 75.5 V
- **Magnetic field**: 5.56, 38.6, 154.8 Gs
- **Electron current**: 2.59, 2.23, 0.5 A
- **Ion current**: 0.108, 0.475, 2.19 A
- **Electron temperature**: 4, 7.01, 2.47 eV
- **Elastic collision time**: 0.764×10⁻⁷, 0.506×10⁻⁷, 1.84×10⁻⁷ s
- **Inelastic collision time**: 7.23×10⁻⁶, 1.44×10⁻⁶, 2.44×10⁻⁶ s
- **Neutral temperature**: 400 K
- **Volume flow rate**: 0.55×10⁻⁶ m³/s

## Physical Constants

The code uses standard physical constants:
- Boltzmann constant: 1.38×10⁻²³ J/K
- Electron mass: 9.11×10⁻³¹ kg
- Elementary charge: 1.6×10⁻¹⁹ C
- Permittivity of free space: 8.85×10⁻¹² F/m
- Krypton mass: 83.798 × 1.66×10⁻²⁷ kg
- Krypton atom radius: 198×10⁻¹⁰ m
- Krypton ionization potential: 13.99 eV
- Bohr radius: 0.529×10⁻⁸ m

## Key Calculations

### 1. Particle Velocities
- **Electron velocity**: Based on electron temperature
- **Ion velocity**: Based on plasma potential
- **Neutral velocity**: Based on neutral temperature

### 2. Particle Concentrations
- **Electron concentration**: From electron current and velocity
- **Ion concentration**: From ion current and velocity
- **Neutral concentration**: From mass flow rate and velocity

### 3. Plasma Parameters
- **Debye radius**: Characteristic length scale of plasma shielding
- **Plasma frequency**: Natural oscillation frequency of electrons
- **Coulomb logarithm**: Parameter for collision calculations

### 4. Collision Parameters
- **Collision cross-sections**: For different particle interactions
- **Collision frequencies**: Rate of collisions for each particle type
- **Mean free paths**: Average distance between collisions

### 5. Hall Parameters
- **Electron Hall parameter**: Ratio of cyclotron frequency to collision frequency
- **Ion Hall parameter**: Indicates magnetization level of particles

## Usage

1. Run the Python script:
```bash
python calculations.py
```

2. The script will:
   - Calculate all plasma parameters
   - Display key results in the console
   - Save detailed results to `plasma_calculations_results.txt`

## Output Files

- **`plasma_calculations_results.txt`**: Detailed results with all calculated parameters, units, and explanations

## Dependencies

- NumPy
- Math (standard library)


## Notes

- The code assumes krypton as the working gas
- Calculations are performed for three spatial points
- Results are saved with timestamps for reference
- All intermediate calculations are included in the output file

## Author

Course work project for plasma physics calculations.
