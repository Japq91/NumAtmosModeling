#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import xarray as xr
import pandas as pd
from src.physics import gauss, euler_backward_step
from src.visualization import plot_3d_surface
from src.data_handling import create_dataset, save_dataset
# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(os.path.join(OUTPUTS_DIR, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUTS_DIR, "figures"), exist_ok=True)
def run_simulation():
    # Parámetros de simulación
    u = 10       # Velocidad de advección (m/s)
    Nx = 101     # Puntos en la malla
    dx = 500     # Espaciado del grid (m)
    dt = 60      # Paso de tiempo (s)
    nr = 10      # Parámetro de la gaussiana
    total_steps = Nx * 3  # Pasos totales de simulación

    # Coordenadas espaciales y temporales
    X = [e * dx for e in range(Nx)]
    T = [e * dt for e in range(total_steps)]
    CFL = dt * u / dx
    print(f"CFL number: {CFL:.2f}")

    # Simulación
    M = []
    Cn = np.array([gauss(x, 0, nr, u, dx, Nx) for x in X])

    for t in T:
        if t == 0:
            M.append(Cn.copy())
            continue
        Cn = euler_backward_step(Cn, u, dt, dx, Nx)
        M.append(Cn.copy())

    # Crear dataset xarray
    ds = create_dataset(M, Nx, dx, T)
    
    # Añadir metadatos
    ds.attrs.update({
        'simulation_parameters': f"u={u}, Nx={Nx}, dx={dx}, dt={dt}, nr={nr}",
        'CFL_number': CFL,
        'author': 'Tu Nombre',
        'created': pd.Timestamp.now().isoformat()
    })

    # Guardar resultados
    nc_path = os.path.join(OUTPUTS_DIR, "data", "simulation_results.nc")
    save_dataset(ds, nc_path)
    print(f"Dataset guardado en: {nc_path}")

    # Generar gráfico 3D
    fig_path = os.path.join(OUTPUTS_DIR, "figures", "3d_surface.png")
    plot_3d_surface(
        ds.isel(time=115), 
        metodo="Euler Backward",
        ti=115,
        dt=dt,
        CFL=CFL,
        save_path=fig_path
    )
    print(f"Gráfico guardado en: {fig_path}")

if __name__ == "__main__":
    run_simulation()
