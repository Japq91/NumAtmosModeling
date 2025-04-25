import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap
import numpy as np

def setup_plot_style():
    """Configura estilos globales para las figuras."""
    plt.rcParams.update({
        'font.size': 11,
        'font.family': 'serif',
        'font.serif': ['Times New Roman'] + plt.rcParams['font.serif']
    })

def setup_custom_levels():
    """Configura los niveles personalizados para los contornos.
    Returns:
        list: Lista de niveles ordenados para el mapa de colores.
    """
    #p1 = [round((e-1)/3,1) for e in np.logspace(0, 1.6, 15)][1:]
    #p2 = [e*-1 for e in p1[:]]
    #p2.extend(p1)
    #nlevel = sorted(np.array(p2))
    nlevel = [-12, -10, -8, -6, -4, -3, -2, -1.5, -1.2, -0.9, -0.6, -0.4, -0.2,  -0.1, 
              -0.05, 0.05, 0.1, 0.2, 0.4, 0.6, 0.9, 1.2, 1.5, 2, 3, 4, 6, 8, 10, 12]
    return nlevel

def create_custom_colormap(cmap_name='coolwarm', center_color=[0, 0, 0, 1]):
    """Crea un colormap personalizado con una línea central destacada.    
    Args:
        cmap_name (str): Nombre del colormap base (por defecto: 'coolwarm').
        center_color (list): Color RGBA para la línea central (por defecto: negro).    
    Returns:
        LinearSegmentedColormap: Colormap personalizado.
    """
    original_cmap = plt.get_cmap(cmap_name)
    colors = original_cmap(np.linspace(0, 1, 256))
    mid_point = len(colors) // 2
    colors[mid_point - 1 : mid_point + 1] = center_color
    return LinearSegmentedColormap.from_list(f'custom_{cmap_name}', colors)

def plot_3d_surface(ds_t0, metodo, ti, dt, CFL, val_lim=25, save_path=None, profile="gauss"):
    """Genera y guarda un gráfico 3D de la superficie de concentración.    
    Args:
        ds_t0 (xarray.Dataset): Dataset con los datos de concentración.
        metodo (str): Nombre del método numérico usado.
        ti (int): Índice de tiempo a visualizar.
        dt (float): Paso de tiempo.
        CFL (float): Número CFL de la simulación.
        val_lim (float): Límite para los valores de concentración.
        save_path (str, optional): Ruta para guardar la figura. Si es None, no guarda.
    """
    # Configuración de estilos
    setup_plot_style()
    nlevel = setup_custom_levels()
    custom_cmap = create_custom_colormap()
    # Crear figura 3D
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    # Obtener coordenadas y datos
    lon = ds_t0.X.values
    lat = ds_t0.Y.values
    lon_grid, lat_grid = np.meshgrid(lon, lat)
    data = ds_t0["conc_unids"].values    
    # Filtrar valores fuera de los límites
    data[data > val_lim] = np.nan
    data[data < -val_lim] = np.nan    
    # Configuración de la vista 3D
    ax.view_init(elev=25, azim=-100)
    ax.set_box_aspect([2, 1.1, 1])    
    # Graficar superficie
    norm = BoundaryNorm(boundaries=nlevel, ncolors=256)
    surf = ax.plot_surface(lon_grid, lat_grid, data, cmap=custom_cmap, norm=norm, 
                           edgecolor='.1', alpha=0.9, linewidth=0.2)    
    # Configuración de ejes y límites
    ax.set_zlim(-val_lim, val_lim)
    ax.set_xlim(-1, 100)
    ax.set_ylim(-250,250)
    ax.set_xlabel('X')
    ax.set_yticks([])   
    
    # Etiquetas y estilo
    ax.xaxis._axinfo["grid"].update({'color': 'k', 'linestyle': ':', 'alpha': 0.2, 'linewidth': .5})
    ax.zaxis._axinfo["grid"].update({'color': '.5', 'linestyle': '-.', 'alpha': 0.1, 'linewidth': .39})
    # Barra de colores
    fig.colorbar(surf, ax=ax, shrink=0.5, label='Conc. Unids', ticks=nlevel[::2])
 
    # Título con parámetros de simulación
    title = f"{metodo} (Profile: {profile})  dt: {dt}, CFL: {CFL:.2f}\nt: {ti*dt} seg."
    ax.set_title(title, y=0.87, fontsize=12)
    
    # Estilo de fondos 3D
    ax.zaxis.set_pane_color((0.7, 0.7, 0.7, 1.0))  # Plano YZ
    ax.yaxis.set_pane_color((0.9, 0.9, 0.91, 1.0)) # Plano XY
    
    # Guardar figura si se especifica ruta
    if save_path:
        fig.savefig(save_path, dpi=300,) #bbox_inches='tight')
        plt.close(fig)
    else:
        plt.show()
