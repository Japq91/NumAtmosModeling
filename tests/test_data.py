import xarray as xr
from src.data_handling import create_dataset
from src.physics import gauss, euler_backward_step

def test_dataset_structure(sample_parameters):
    """Verifica la estructura del dataset generado"""
    p = sample_parameters
    X = [e * p['dx'] for e in range(p['Nx'])]
    T = [e * p['dt'] for e in range(10)]  # Solo 10 pasos para prueba
    M = [[gauss(x, t, p['nr'], p['u'], p['dx'], p['Nx']) for x in X] for t in T]
    
    ds = create_dataset(M, p['Nx'], p['dx'], T)
    
    assert "conc_unids" in ds
    assert ds.dims["time"] == 10
