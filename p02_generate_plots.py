#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import argparse
import xarray as xr
from src.visualization import plot_3d_surface

# Constantes físicas
U = 10  # Velocidad (m/s)
DX = 500  # Espaciado (m)

def find_data_file(dt, profile, nr=None, method=None, data_type='numerical'):
    """Busca archivos que coincidan con los parámetros"""
    # Construye el patrón de búsqueda exacto que estás usando
    pattern = f"outputs/data/{method.replace(' ', '')}_dt{dt}_CFL*_dx{DX}_profile{profile}"
    if nr is not None:
        pattern += f"_nr{nr}"
    pattern += f"_{data_type}.nc"
    
    matches = glob.glob(pattern)
    return matches[0] if matches else None

def generate_plots(dt, profile, nr=None, method=None, data_type='numerical'):
    """Genera gráficos adaptándose a tus nombres de archivo exactos"""
    data_path = find_data_file(dt, profile, nr, method, data_type)
    
    if not data_path:
        print(f"Error: No se encontró archivo {data_type} para:")
        print(f"method={method}, dt={dt}, profile={profile}" + (f", nr={nr}" if nr else ""))
        print("\nArchivos disponibles en outputs/data/:")
        for f in glob.glob("outputs/data/*.nc"):
            print(f"- {os.path.basename(f)}")
        return

    try:
        ds = xr.open_dataset(data_path)
        dir_name = method.replace(" ", "") if method else "Analytical"
        os.makedirs(f"outputs/figures/{dir_name}", exist_ok=True)
        
        base_name = os.path.basename(data_path).replace('.nc', '')
        for ti in range(len(ds.time)):
            fig_path = f"outputs/figures/{dir_name}/3D{ti:03d}_{base_name}.png"
            title = f"{method} ({data_type})" if method else "Solución Analítica"
            plot_3d_surface(
                ds.isel(time=ti),
                title,
                ti,
                float(dt),
                float(U*dt/DX),
                save_path=fig_path,
                profile=profile
            )
        print(f"Gráficos generados en outputs/figures/{dir_name}/")
        
    except Exception as e:
        print(f"Error procesando archivo: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generador de visualizaciones')
    
    # Parámetros comunes
    parser.add_argument('--dt', type=float, required=True, help='Paso de tiempo (s)')
    parser.add_argument('--profile', choices=['gauss', 'rectg'], required=True)
    parser.add_argument('--nr', type=float, help='Ancho de la gaussiana (solo para profile=gauss)')
    
    # Modos de operación
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--numerical', metavar='METHOD', help='Generar gráficos numéricos')
    group.add_argument('--analytical', metavar='METHOD', help='Generar gráficos analíticos')
    
    args = parser.parse_args()
    
    # Validaciones
    if args.profile == 'gauss' and args.nr is None:
        parser.error("Se requiere --nr para perfil gaussiano")
    
    # Ejecutar
    if args.numerical:
        generate_plots(
            dt=args.dt,
            profile=args.profile,
            nr=args.nr,
            method=args.numerical,
            data_type='numerical'
        )
    else:
        generate_plots(
            dt=args.dt,
            profile=args.profile,
            nr=args.nr,
            method=args.analytical,  # Pasa el método para mantener consistencia en nombres
            data_type='analytical'
        )