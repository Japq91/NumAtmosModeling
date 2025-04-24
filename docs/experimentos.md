# Experimental Design and Configurations

This document describes the experimental setups used to test numerical methods for solving the 1D advection equation.

## Objectives
- Evaluate how different numerical schemes reproduce the analytical solution.
- Analyze the impact of initial and boundary conditions.
- Study the effect of varying CFL values on stability and accuracy.

---

## Simulation Parameters
- Domain length: 500,000 m
- Grid points: Nx = 101
- Grid spacing: Δx = 5000 m
- Advection velocity: U = 10 m/s
- Time steps: values set to achieve target CFL values

---

## Initial Conditions Tested

1. **Gaussian profile (wide):**
   - Centered at x = 255,000 m
   - nr = 10

2. **Gaussian profile (narrow):**
   - Centered at x = 255,000 m
   - nr = 2

3. **Rectangular profile:**
   - Height = 10, width = 10,000 m
   - Flat top with sharp edges

---

## Boundary Conditions Applied

1. **Periodic:**
   - Signal wraps around the domain

2. **Rigid (fixed):**
   - Boundary values fixed to zero

3. **Radiative:**
   - Allows outgoing waves with minimal reflection

---

## CFL Values Tested

Simulations were run with the following CFL numbers:

    CFL = [0.5, 0.75, 1.0, 1.2, 2.0]

Note: Each method may require specific values for stability (e.g., Leapfrog 4th-order stable only at CFL ≤ 0.729).

---

## Output
- Each configuration produces:
  - NetCDF file with concentration fields over time
  - PNG images for each time step (3D visualization)
  - GIF animation summarizing temporal evolution

---

## Evaluation Criteria
- Visual comparison against analytical solution
- Stability (presence of oscillations or divergence)
- Preservation of wave shape and amplitude
- Numerical diffusion or dispersion effects

These experiments help understand the trade-offs between accuracy, stability, and computational cost across various numerical schemes.


