#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import xarray as xr
import pandas as pd
import argparse
from src.physics import analytical_solution, euler_backward_step
from src.data_handling import create_dataset, save_dataset

# Constantes físicas
U = 10  # Velocidad (m/s)
DX = 500  # Espaciado (m)

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
DATA_DIR = os.path.join(OUTPUTS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def run_simulation(dt, nr, method, profile="gauss"):
    """Ejecuta simulación y guarda resultados en NetCDF"""
    Nx = 101
    total_steps = Nx * 2 # cantidad de tiempos, puede ser un numero cualquiera
    CFL = U * dt / DX

    # Coordenadas
    X = [e * DX for e in range(Nx)]
    T = [e * dt for e in range(total_steps)][:]  #[:10] Primeros 10 pasos

    # Simulación numérica
    M_num = []
    Cn = np.array([analytical_solution(x, 0, U, DX, Nx, profile, nr) for x in X])
    for t in T:
        if t != 0:
            Cn = euler_backward_step(Cn, U, dt, DX, Nx)
        M_num.append(Cn.copy())

    # Solución analítica
    M_analytical = [[analytical_solution(x, t, U, DX, Nx, profile, nr) for x in X] for t in T]

    # Crear y guardar datasets
    base_name = f"{method.replace(' ', '')}_dt{dt}_CFL{CFL}_dx{DX}_profile{profile}"
    if profile == 'gauss':
        base_name += f"_nr{nr}"

    datasets = {
        "numerical": create_dataset(M_num, Nx, DX, T),
        "analytical": create_dataset(M_analytical, Nx, DX, T)
    }

    for key, ds in datasets.items():
        ds.attrs.update({
            'simulation_parameters': f"U={U}, Nx={Nx}, DX={DX}, dt={dt}, profile={profile}{f', nr={nr}' if profile == 'gauss' else ''}",
            'CFL_number': CFL,
            'data_type': key
        })
        save_dataset(ds, os.path.join(DATA_DIR, f"{base_name}_{key}"))

    return base_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genera datasets de simulación')
    parser.add_argument('--method', required=True, help='Método numérico')
    parser.add_argument('--dt', type=float, required=True, help='Paso de tiempo (s)')
    parser.add_argument('--profile', choices=['gauss', 'rectg'], required=True)
    parser.add_argument('--nr', type=float, help='Ancho gaussiana (requerido para profile=gauss)')
    
    args = parser.parse_args()
    
    if args.profile == 'gauss' and args.nr is None:
        parser.error("Se requiere --nr para perfil gaussiano")
    
    base_name = run_simulation(args.dt, args.nr, args.method, args.profile)
    print(f"Datasets generados con prefijo: {base_name}")