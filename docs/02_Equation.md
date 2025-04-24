# Equations and Discretization

## Advection Equation
The one-dimensional linear advection equation describes the transport of a conserved scalar quantity:

    ∂C/∂t + U ∂C/∂x = 0

Where:
- `C(x, t)` is the concentration of a tracer
- `U` is the constant advection velocity

This equation models the transport process in fluids without sources, sinks, or diffusion.

---

## Initial Conditions
Two initial profiles are used to initialize the scalar field:

1. **Gaussian Function:**

        C(x, 0) = 10 * exp(-((x - x0)^2) / (nr * Δx)^2)

   Where `x0` is the center of the distribution, and `nr` controls the width.

2. **Rectangular Function:**

        C(x, 0) = 10,  if 250000 m <= x <= 260000 m
                 0,   otherwise

---

## Boundary Conditions
Three types of boundary conditions are considered:

- **Periodic:** ensures conservation by wrapping values from the end to the start of the domain
- **Rigid (fixed):** sets C = 0 at the boundaries
- **Radiative:** allows wave-like perturbations to exit the domain with minimal reflection

---

## Numerical Discretization of Spatial Derivatives

1. **Forward Difference:**

        (∂C/∂x) ≈ (C_{j+1} - C_j) / Δx

2. **Centered Difference:**

        (∂C/∂x) ≈ (C_{j+1} - C_{j-1}) / (2Δx)

3. **Backward Difference:**

        (∂C/∂x) ≈ (C_j - C_{j-1}) / Δx

4. **Fourth-Order Central Difference:**

        (∂C/∂x) ≈ [4(C_{j+1} - C_{j-1}) - (C_{j+2} - C_{j-2})] / (3Δx)

---

## Courant-Friedrichs-Lewy (CFL) Condition
The CFL number is a key stability indicator defined as:

    CFL = U * Δt / Δx

Values of `CFL` must respect the stability limits of each numerical scheme (e.g., CFL ≤ 1 for many explicit methods).

---

## Order of Accuracy
The accuracy of a method is expressed as `O(Δt^n)`, indicating how the numerical error decreases when the time step is reduced:

- Euler Backward:    O(Δt)
- Leapfrog:          O(Δt^2)
- Runge-Kutta (4th): O(Δt^4)

Choosing a higher-order method reduces error but increases computational cost.


