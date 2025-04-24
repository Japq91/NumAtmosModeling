import numpy as np
from physics import gauss, euler_backward_step
from visualization import setup_plot_style, plot_3d_surface
from data_handling import create_dataset, save_dataset, load_dataset

# Después de generar 'ds':
if not os.path.exists("../outputs/data/simulacion.nc"):
    save_dataset(ds, "simulacion")
else:
    ds = load_dataset("simulacion")  # Carga datos existentes

# Parámetros globales
u = 10       # Velocidad de advección (m/s)
Nx = 101     # Puntos en la malla
dx = 500     # Espaciado del grid (m)
dt = 60      # Paso de tiempo (s)
nr = 10      # Parámetro de la gaussiana

def main():
    setup_plot_style()
    
    # Simulación
    X = [e * dx for e in range(Nx)]
    T = [e * dt for e in range(Nx * 3)]  # Tiempos de simulación
    CFL = dt * u / dx
    print(f"CFL: {CFL}")
    
    # Almacenar resultados
    M = []
    Cn = np.array([gauss(x, 0, nr, u, dx, Nx) for x in X])
    
    for t in T:
        if t == 0:
            M.append(Cn.copy())
            continue
        Cn = euler_backward_step(Cn, u, dt, dx, Nx)
        M.append(Cn.copy())
    
    # Crear dataset y visualizar
    ds = create_dataset(M, Nx, dx, T)
    plot_3d_surface(
        ds.isel(time=115), 
        metodo="Euler Backward", 
        ti=115, dt=dt, CFL=CFL,
        save_path="../outputs/figures/figura_3d.png"
    )

if __name__ == "__main__":
    main()
