#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from glob import glob as gb
from PIL import Image
import argparse

# Constantes físicas
U = 10  # Velocidad de advección (m/s)
DX = 500  # Espaciado del grid (m)

# Configuración de directorios
BASE_DIR = os.pathdirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

def calculate_cfl(dt):
    """Calcula el número CFL dado dt"""
    CFL = dt * U / DX
    print(f"CFL number: {CFL:.2f}")
    return CFL

def parse_simulation_params(filename):
    """Extrae parámetros del nombre del archivo"""
    patterns = [
        r"(?P<method>[\w\s]+)_dt(?P<dt>\d+)_CFL(?P<cfl>[\d.]+)_dx\d+_profile(?P<profile>gauss)_nr(?P<nr>\d+)",
        r"(?P<method>[\w\s]+)_dt(?P<dt>\d+)_CFL(?P<cfl>[\d.]+)_dx\d+_profile(?P<profile>rectg)"
    ]
    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            return match.groupdict()
    return {}

def generate_gif(input_files, output_path, delay=20):
    """Genera GIF a partir de imágenes"""
    if not input_files:
        print("Error: No se encontraron archivos PNG para generar el GIF")
        return
    
    images = []
    for f in sorted(input_files):
        try:
            images.append(Image.open(f))
        except Exception as e:
            print(f"Error al abrir {f}: {e}")
    
    if not images:
        print("Error: No hay imágenes válidas para generar el GIF")
        return
    
    images[0].save(output_path,
                 save_all=True,
                 append_images=images[1:],
                 duration=delay,
                 loop=0,
                 optimize=True)
    print(f'\n✅ GIF generado en: {output_path}\n')

def main():
    parser = argparse.ArgumentParser(
        description='Generador de animaciones para simulaciones de advección',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('--method', required=True,
                      help='Método numérico usado (ej. "Euler Backward")')
    parser.add_argument('--type', choices=['numerical', 'analytical'], default='numerical',
                      help='Tipo de resultados a animar')
    parser.add_argument('--dt', type=int, required=True,
                      help='Paso de tiempo usado en la simulación (segundos)')
    parser.add_argument('--profile', choices=['gauss', 'rectg'], required=True,
                      help='Perfil inicial usado')
    parser.add_argument('--nr', type=int,
                      help='Ancho de la gaussiana (requerido para profile=gauss)')
    
    args = parser.parse_args()

    # Validación de parámetros
    if args.profile == 'gauss' and args.nr is None:
        parser.error("Se requiere --nr para perfil gaussiano")
    if args.profile == 'rectg' and args.nr is not None:
        print("⚠️  Advertencia: El parámetro --nr no se usa para perfil rectangular")

    # Calcular CFL
    cfl = calculate_cfl(args.dt)
    print(f"\n⚙️  Parámetros de simulación:")
    print(f"- Método: {args.method}")
    print(f"- dt: {args.dt}s")
    print(f"- CFL: {cfl}")
    print(f"- Perfil: {args.profile}")
    if args.profile == 'gauss':
        print(f"- nr: {args.nr}")

    # Buscar archivos
    method_dir = args.method.replace(" ", "")
    search_pattern = (
        f"3D*{args.method.replace(' ', '')}_dt{args.dt}_CFL{cfl}_dx{DX}_profile{args.profile}"
        f"{f'_nr{args.nr}' if args.profile == 'gauss' else ''}.png"
    )
    
    input_files = sorted(gb(os.path.join(OUTPUTS_DIR, "figures", method_dir, search_pattern)))
    
    if not input_files:
        print(f"\n❌ Error: No se encontraron archivos que coincidan con:")
        print(f"Patrón: {search_pattern}")
        print(f"Directorio: {os.path.join(OUTPUTS_DIR, 'figures', method_dir)}")
        return

    # Generar nombre de salida
    output_name = (
        f"{args.method.replace(' ', '')}_dt{args.dt}_CFL{cfl}_dx{DX}_profile{args.profile}"
        f"{f'_nr{args.nr}' if args.profile == 'gauss' else ''}_{args.type}.gif"
    )
    output_path = os.path.join(OUTPUTS_DIR, "figures", output_name)
    
    print(f"\n📁 Archivos encontrados: {len(input_files)}")
    print(f"🎞️  Generando GIF...")
    
    generate_gif(input_files, output_path)

if __name__ == "__main__":
    main()