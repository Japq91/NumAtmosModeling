#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import xarray as xr
import pandas as pd
import argparse
from src.physics import gauss, rectg, euler_backward_step, analytical_solution
from src.visualization import plot_3d_surface
from src.data_handling import create_dataset, save_dataset

# Constantes físicas
u = 10  # Velocidad de advección (m/s)
ds = 500  # Espaciado del grid (m)

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(os.path.join(OUTPUTS_DIR, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUTS_DIR, "figures"), exist_ok=True)

def run_simulation(dt, nr, metodo, profile="gauss"):
    # Parámetros de simulación
    #u = 10       # Velocidad de advección (m/s)
    Nx = 101     # Puntos en la malla
    #dx = 500     # Espaciado del grid (m)
    total_steps = Nx * 2  # Pasos totales de simulación

    # Coordenadas espaciales y temporales
    X = [e * dx for e in range(Nx)]
    T = [e * dt for e in range(total_steps)][:10]  # Solo primeros 10 pasos
    CFL = dt * u / dx
    print(f"CFL number: {CFL:.2f}")

    # Simulación numérica
    M_num = []
    Cn = np.array([analytical_solution(x, 0, u, dx, Nx, profile, nr) for x in X])  # Condición inicial
    for t in T:
        if t == 0:
            M_num.append(Cn.copy())
            continue
        Cn = euler_backward_step(Cn, u, dt, dx, Nx)
        M_num.append(Cn.copy())

    # Solución analítica (para comparación)
    M_analytical = []
    for t in T:
        M_analytical.append([analytical_solution(x, t, u, dx, Nx, profile, nr) for x in X])

    # Crear datasets
    ds_num = create_dataset(M_num, Nx, dx, T)
    ds_analytical = create_dataset(M_analytical, Nx, dx, T)

    # Añadir metadatos
    for ds in [ds_num, ds_analytical]:
        ds.attrs.update({
            'simulation_parameters': f"u={u}, Nx={Nx}, dx={dx}, dt={dt}, nr={nr}, profile={profile}",
            'CFL_number': CFL,
            'author': 'Japq',
            'created': pd.Timestamp.now().isoformat()
        })

    # Guardar resultados
    nmet = metodo.replace(' ', '')
    o_file = f"{nmet}_dt{dt}_CFL{CFL:.2f}_dx{dx}_profile{profile}_nr{nr}"
    
    # Guardar datos numéricos y analíticos
    save_dataset(ds_num, os.path.join(OUTPUTS_DIR, "data", f"{o_file}_numerical"))
    save_dataset(ds_analytical, os.path.join(OUTPUTS_DIR, "data", f"{o_file}_analytical"))

    # Generar figuras
    os.makedirs(os.path.join(OUTPUTS_DIR, "figures", nmet), exist_ok=True)
    for ti, t in enumerate(T):
        fig_path = os.path.join(OUTPUTS_DIR, "figures", nmet, f"3D{ti:03d}_{o_file}.png")
        plot_3d_surface(ds_num.isel(time=ti), metodo, ti, dt, CFL, save_path=fig_path, profile=profile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dt", type=float, default=40, help="Paso de tiempo (s)")
    parser.add_argument("--nr", type=float, default=10, help="Ancho de la gaussiana (nr*dx)")
    parser.add_argument("--profile", type=str, default="gauss", choices=["gauss", "rectg"], help="Perfil inicial (gauss/rectg)")
    args = parser.parse_args()

    run_simulation(args.dt, args.nr, "Euler Backward", args.profile)