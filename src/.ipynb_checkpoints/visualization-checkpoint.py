import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap
import numpy as np

def setup_plot_style():
    """Configura estilos globales para las figuras."""
    plt.rcParams.update({
        'font.size': 11,
        'font.family': 'serif',
        'font.serif': ['Times New Roman'] + plt.rcParams['font.serif']
    })

def create_custom_colormap():
    """Crea un colormap personalizado (coolwarm con línea negra en el centro)."""
    original_cmap = plt.get_cmap('coolwarm')
    colors = original_cmap(np.linspace(0, 1, 256))
    mid_point = len(colors) // 2
    colors[mid_point - 1:mid_point + 1] = [0, 0, 0, 1]  # Negro (RGBA)
    return LinearSegmentedColormap.from_list('custom_bwr', colors)

def plot_3d_surface(ds_t0, metodo, ti, dt, CFL, val_lim=25, save_path=None):
    """Genera y guarda un gráfico 3D de la superficie."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Configuración de ejes, colormap, y visualización
    # ... (código específico de tu gráfico 3D aquí)
    
    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
