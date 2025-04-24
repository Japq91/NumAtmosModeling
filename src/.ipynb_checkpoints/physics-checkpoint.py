import numpy as np

def gauss(x, t, nr, u, dx, Nx):
    """Calcula una gaussiana centrada en 51*dx con condiciones periódicas."""
    x0 = (x - u * t) % ((Nx - 1) * dx)
    return 10 * np.exp((-(x0 - 51*dx)**2) / ((nr*dx)**2))

def rectg(x, t, u, dx, Nx, co=10):
    """Genera un pulso rectangular entre 50*dx y 52*dx."""
    x0 = (x - u * t) % ((Nx - 1) * dx)
    a = x0 >= 50*dx
    b = x0 <= 52*dx
    return np.where(a & b, co, 0)

def euler_backward_step(Cn, u, dt, dx, Nx):
    """Avanza un paso en el tiempo usando el esquema Euler backward."""
    Cnp1 = np.zeros_like(Cn, dtype=float)
    for j in range(Nx):
        Cnp1[j] = Cn[j] - (u * dt / dx) * (Cn[j] - Cn[j-1])
    return Cnp1
