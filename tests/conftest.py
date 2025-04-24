import pytest
import numpy as np
from src.physics import gauss, euler_backward_step

@pytest.fixture
def sample_parameters():
    return {
        'u': 10,
        'Nx': 101,
        'dx': 500,
        'dt': 60,
        'nr': 10
    }
