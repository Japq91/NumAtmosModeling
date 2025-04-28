#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import argparse
from PIL import Image
#
# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
#
def crop_image(image_path, espacio=5):
    """Recorta la imagen manteniendo el 3/4 central (tu lógica original)"""
    try:
        img = Image.open(image_path)
        width, height = img.size
        top = height // espacio
        bottom = (espacio-1) * height // espacio
        return img.crop((0, top, width, bottom))
    except Exception as e:
        print(f"Error al recortar {image_path}: {str(e)}")
        return None
######################
# def save_cropped_images(image_paths, temp_dir="temp_cropped"):
#     """Guarda versiones recortadas en carpeta temporal"""
#     os.makedirs(temp_dir, exist_ok=True)
#     cropped_paths = []
#     for img_path in image_paths:
#         img = crop_image(img_path)
#         img = img.resize((width//2, height//2))
#         if img:
#             new_path = os.path.join(temp_dir, os.path.basename(img_path))
#             img.save(new_path)
#             cropped_paths.append(new_path)
#     return cropped_paths

# def create_gif_with_convert(image_paths, output_path, delay=50):
#     """Crea GIF con ImageMagick usando os.system"""
#     temp_dir = "temp_cropped"
#     cropped_paths = save_cropped_images(image_paths, temp_dir)
    
#     if not cropped_paths:
#         print("Error: No hay imágenes recortadas válidas")
#         return
    
#     # Convert delay (ms to centisec)
#     delay_cs = max(1, delay // 10)  # Asegura mínimo 1 centisegundo
    
#     # Construye comando
#     cmd = f"convert -delay {delay_cs} -loop 0 {' '.join(sorted(cropped_paths))} {output_path}"
#     # Ejecuta y verifica
#     if os.system(cmd) == 0:
#         print(f"GIF creado con convert: {output_path}")
#         # Limpieza opcional:
#         for img in cropped_paths:
#             os.remove(img)
#         os.rmdir(temp_dir)
#     else:
#         print("Error al ejecutar convert. ¿Está ImageMagick instalado?")
# ######################
######################
def create_animation_with_crop(image_paths, output_path, duration=20):
    """Crea GIF con recorte de imágenes"""
    if not image_paths:
        print(f"Error: No se encontraron imágenes para animación")
        return
    
    cropped_images = []
    for img_path in sorted(image_paths):
        cropped = crop_image(img_path)
        if cropped:
            cropped_images.append(cropped)
    
    if not cropped_images:
        print(f"Error: No hay imágenes válidas después del recorte")
        return
    
    try:
        # Guardar GIF con tus parámetros originales
        cropped_images[0].save(
            output_path,
            save_all=True,
            append_images=cropped_images[1:],
            duration=duration,
            loop=0,
            optimize=True
        )
        print(f"Animación con recorte creada: {output_path}")
    except Exception as e:
        print(f"Error al guardar GIF: {str(e)}")

def find_image_sequence(method, dt, profile, nr=None, data_type='numerical'):
    """Busca secuencias de imágenes con el patrón correcto"""
    method_dir = method.replace(" ", "")
    pattern = os.path.join(
        OUTPUTS_DIR,
        "figures",
        method_dir,
        f"3D*{method_dir}_dt{dt}_CFL*_dx500_profile{profile}"
    )
    if nr is not None:
        pattern += f"_nr{nr}"
    pattern += f"_{data_type}.png"
    
    return sorted(glob.glob(pattern))

def main():
    parser = argparse.ArgumentParser(
        description='Genera animaciones GIF con recorte de imágenes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # Estructura idéntica a p02_generate_plots.py
    parser.add_argument('--dt', type=float, required=True, help='Paso de tiempo (s)')
    parser.add_argument('--profile', choices=['gauss', 'rectg'], required=True)
    parser.add_argument('--nr', type=float, help='Ancho de la gaussiana (requerido para profile=gauss)')
    
    # Grupo mutuamente excluyente
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--numerical', metavar='METHOD', help='Animación para resultados numéricos')
    group.add_argument('--analytical', metavar='METHOD', help='Animación para solución analítica')
    
    # Opciones adicionales
    parser.add_argument('--duration', type=int, default=50, help='Duración entre frames (ms)')
    parser.add_argument('--espacio', type=int, default=5, 
                       help='Parámetro de recorte (1/espacio superior, (espacio-1)/espacio inferior)')
    parser.add_argument('--engine', choices=['pillow', 'imagemagick'], default='pillow',
                   help='Motor para generar GIFs (default: pillow)')
    args = parser.parse_args()
    
    # Validaciones
    if args.profile == 'gauss' and args.nr is None:
        parser.error("Se requiere --nr para perfil gaussiano")
    
    # Determinar tipo y método
    method = args.numerical if args.numerical else args.analytical
    data_type = 'numerical' if args.numerical else 'analytical'
    
    # Buscar imágenes
    image_paths = find_image_sequence(
        method=method,
        dt=args.dt,
        profile=args.profile,
        nr=args.nr,
        data_type=data_type
    )
    
    if not image_paths:
        print(f"\nNo se encontraron imágenes {data_type} para:")
        print(f"method={method}, dt={args.dt}, profile={args.profile}" + (f", nr={args.nr}" if args.nr else ""))
        return
    
    # Preparar directorio de salida
    output_dir = os.path.join(OUTPUTS_DIR, "animations")
    os.makedirs(output_dir, exist_ok=True)
    
    # Nombre del archivo de salida
    output_name = f"{method.replace(' ', '')}_dt{args.dt}_profile{args.profile}"
    if args.nr:
        output_name += f"_nr{args.nr}"
    output_name += f"_{data_type}_cropped.gif"
    output_path = os.path.join(output_dir, output_name)
    
    # Crear animación con recorte
    print(f"\nGenerando animación con recorte (espacio={args.espacio})...")
    #create_animation_with_crop(image_paths, output_path, args.duration)
    if args.engine == 'imagemagick':
        create_gif_with_convert(image_paths, output_path, delay=args.duration, espacio=args.espacio, max_workers=4)
    else:
        create_animation_with_crop(image_paths, output_path, args.duration)

if __name__ == "__main__":
    main()
