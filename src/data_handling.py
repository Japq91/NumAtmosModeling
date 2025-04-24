import xarray as xr
import os
import pandas as pd
import numpy as np

def create_dataset(M, Nx, dx, T):
    """Crea un dataset xarray a partir de los resultados de la simulación."""
    data_3d = np.tile(np.array(M)[:, np.newaxis, :], (1, 2, 1))
    time = pd.Timestamp('2020-01-01') + pd.to_timedelta(T, unit='s')
    return xr.Dataset(
        {"conc_unids": (["time", "Y", "X"], data_3d)},
        coords={"time": time, "X": np.arange(Nx), "Y": [-dx/2, dx/2]}
    )

def save_dataset(ds, filename, output_dir="outputs/data"):
    """Guarda el dataset en NetCDF con compresión eficiente."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{filename}.nc")
    
    encoding = {
        "conc_unids": {
            "zlib": True,
            "complevel": 4  # Compresión balanceada (1-9)
        }
    }
    
    ds.to_netcdf(path, encoding=encoding)
    return path

def load_dataset(filename, output_dir="outputs/data"):
    """Carga un dataset desde NetCDF."""
    path = os.path.join(output_dir, f"{filename}.nc")
    return xr.open_dataset(path)
