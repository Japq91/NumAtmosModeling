import matplotlib
from src.visualization import create_custom_colormap

def test_custom_colormap():
    """Verifica que el colormap personalizado tiene línea negra"""
    cmap = create_custom_colormap()
    assert cmap(0.5) == (0, 0, 0, 1)  # RGBA para negro en el centro
