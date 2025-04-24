import numpy as np
from src.physics import gauss, euler_backward_step

def test_gauss(sample_parameters):
    """Verifica que gauss() devuelve valores positivos y el máximo en 51*dx"""
    p = sample_parameters
    x = np.arange(0, p['Nx'] * p['dx'], p['dx'])
    result = gauss(x[51], t=0, nr=p['nr'], u=p['u'], dx=p['dx'], Nx=p['Nx'])
    
    assert result > 0
    assert np.isclose(result, 10.0)  # Valor máximo esperado

def test_euler_backward_conservation(sample_parameters):
    """Verifica que la masa se conserva (aproximadamente)"""
    p = sample_parameters
    Cn = np.array([gauss(e*p['dx'], 0, p['nr'], p['u'], p['dx'], p['Nx']) 
                  for e in range(p['Nx'])])
    Cnp1 = euler_backward_step(Cn, p['u'], p['dt'], p['dx'], p['Nx'])
    
    assert np.isclose(Cn.sum(), Cnp1.sum(), rtol=1e-3)
