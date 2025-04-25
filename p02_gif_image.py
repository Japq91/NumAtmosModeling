#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
from glob import glob as gb
# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
print(OUTPUTS_DIR)
os.makedirs(os.path.join(OUTPUTS_DIR, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUTS_DIR, "figures"), exist_ok=True)
##################################################################
dt = 40      # Paso de tiempo (s)
nr = 10      # Parámetro de la gaussiana
metodo="Euler Backward"
##################################################################
def gera_gif(fileima):
    # 2. Recortas con Pillow (50% superior)
    img = Image.open(fileima)
    width, height = img.size    
    espacio=7
    top = height // espacio
    bottom = (espacio-1) * height // espacio    
    central_half = img.crop((0, top, width, bottom))    
    central_half.save(fileima.replace('3D','tmp_'))
def run_simulation(dt,nr,metodo):
    # Parámetros de simulación
    u = 10       # Velocidad de advección (m/s)
    Nx = 101     # Puntos en la malla
    dx = 500     # Espaciado del grid (m)
    CFL = dt * u / dx
    print(f"CFL number: {CFL:.2f}")
    # Guardar resultados    
    nmet=metodo.replace(' ','')
    rout="%s/figures/%s"%(OUTPUTS_DIR,nmet)
    i_file= "%s_dt%s_CFL%s_dx%s"%(nmet,dt,CFL,dx)    
    for file in sorted(gb("%s/3D*_%s.png"%(rout,i_file)))[:]:
        # Generar gráfico 3D        
        print(file)
        gera_gif(file)
    print('done')
    os.system('convert -delay 20 -loop 0 %s/tmp*.png %s/figures/%s.gif'%(rout,OUTPUTS_DIR,i_file))
    os.system('rm %s/tmp_*.png'%rout)

if __name__ == "__main__":
    run_simulation(dt,nr,metodo)
