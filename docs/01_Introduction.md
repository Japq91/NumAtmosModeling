# Introduction

Numerical modeling is a fundamental tool in atmospheric sciences, allowing researchers to simulate complex dynamic processes and predict physical phenomena with high precision. According to Randall (2021), numerical models enable controlled experiments that would be impossible under real-world conditions. These models are based on fundamental physical equations such as conservation of mass, momentum, and energy, which are discretized for computational solution.

The one-dimensional advection equation is a simplified but essential example used to investigate the transport of scalar properties in geophysical flows. It is expressed as:

    ∂C/∂t + U ∂C/∂x = 0

where `C(x,t)` represents the concentration of a conserved constituent transported with a constant velocity `U`.

This model captures fundamental aspects of atmospheric and oceanic transport, such as the propagation of pollutants or tracers. Analytical solutions are not always feasible due to complex boundary and initial conditions, making numerical approaches indispensable.

An important factor in the behavior of numerical methods for solving the advection equation is the Courant-Friedrichs-Lewy (CFL) number. It defines the relationship between the time step, spatial resolution, and advection speed, and plays a critical role in ensuring the stability of numerical schemes.

In this project, we evaluate several numerical schemes to solve the 1D advection equation under varying configurations:

- Initial conditions (e.g., Gaussian and rectangular profiles)
- Boundary conditions (periodic, rigid, and radiative)
- Variations in the CFL number to assess stability

"The goal, of course, is to admire how numerical methods almost reproduce the analytical solution, while parameter choices do their best to sabotage stability, accuracy, and any hope of a decent result." gaaa


