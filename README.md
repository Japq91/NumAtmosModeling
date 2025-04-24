# atMOdel 🌪️
**Modelo Numérico de Advección con Esquema Euler Backward**  
*Simulación de transporte de contaminantes usando métodos numéricos y visualización 3D.*

## 📋 Tabla de Contenidos  
1. [Descripción](#-descripción)  
2. [Estructura del Proyecto](#-estructura-del-proyecto)  
3. [Requisitos](#-requisitos)  
4. [Instalación](#-instalación)  
5. [Uso](#-uso)  
6. [Ejemplos](#-ejemplos)  
7. [Resultados](#-resultados)  
8. [Pruebas](#-pruebas)  
9. [Contribución](#-contribución)  
10. [Documentación Técnica](#-documentación-técnica)  


## 🌟 Descripción  
Este proyecto simula el transporte de un contaminante en un flujo unidimensional usando:  
- **Esquema Euler Backward** para la discretización temporal.  
- **Condiciones periódicas** en los bordes del dominio.  
- Visualización interactiva con `matplotlib` y `xarray`.  

**Aplicaciones**: Modelado atmosférico, dispersión de contaminantes, dinámica de fluidos.  

## 📂 Estructura del Proyecto  
```plaintext
atMOdel/  
├── src/                   # Código fuente principal  
│   ├── physics.py         # Funciones numéricas (e.g., Euler backward)  
│   ├── data_handling.py   # Carga, guardado y metadatos de NetCDF  
│   ├── visualization.py   # Funciones de graficado 3D y superficie  
│   └── main.py            # Ejemplo base de simulación (1 sola corrida)  
├── run_simulation.py      # Script principal con gestión de outputs  
├── gif_image.py           # Script para crear animaciones .gif  
├── outputs/               # Resultados de simulación  
│   ├── data/              # Archivos NetCDF (.nc)  
│   └── figures/           # Imágenes y animaciones  
├── tests/                 # Pruebas unitarias  
│   ├── test_data/         # Datos para pruebas  
│   ├── test_physics.py    # Pruebas del módulo físico  
│   └── ...                # Otros archivos de test  
├── docs/                  # Documentación técnica completa  
│   ├── introduccion.md  
│   ├── ecuaciones.md  
│   ├── metodos.md  
│   ├── criterios_estabilidad.md  
│   ├── experimentos.md  
│   └── referencias.md  
├── requirements.txt       # Lista de dependencias  
├── README.md              # Documento de presentación del proyecto  
└── .gitignore             # Archivos a ignorar por git  
```

## 🛠️ Requisitos  
- **Python 3.8+**  
- Bibliotecas (ver `requirements.txt`):  
```plaintext
numpy>=1.21.0
xarray>=0.20.0
matplotlib>=3.5.0
pandas>=1.3.0
pillow>=9.0.0
```

## ⚙️ Instalación  
1. Clona el repositorio:  
```bash
git clone https://github.com/tu-usuario/atMOdel.git
cd atMOdel
```  
2. Instala dependencias:  
```bash
pip install -r requirements.txt
```

## 🚀 Uso  
### Ejecutar simulación completa (con generación de gráficos y datos):  
```bash
python run_simulation.py
```

### Para pruebas simples o demostración visual:  
```bash
python src/main.py
```

### Parámetros configurables (en `src/main.py` o `run_simulation.py`):  
```python
u = 10       # Velocidad de advección (m/s)  
Nx = 101     # Puntos en la malla  
dx = 500     # Espaciado del grid (m)  
dt = 60      # Paso de tiempo (s)  
```

## 📊 Ejemplos  
### 1. Simulación básica:  
```python
from physics import gauss, euler_backward_step  
Cn = [gauss(x, 0, nr=10, u=10, dx=500, Nx=101) for x in range(101)]  
Cnp1 = euler_backward_step(Cn, u=10, dt=60, dx=500, Nx=101)  
```

### 2. Visualización 3D:  
```python
from visualization import plot_3d_surface  
plot_3d_surface(dataset, metodo="Euler Backward", ti=115, dt=60, CFL=1.2)  
```

## 📌 Resultados  
- Salida en NetCDF con la evolución temporal del contaminante:  
  `outputs/data/*.nc`
- Gráficos 3D generados automáticamente por cada paso temporal:  
  `outputs/figures/EulerBackward/*.png`
- Animación `.gif` con la evolución total del contaminante:  
  `outputs/figures/*.gif`

## 🧪 Pruebas  
Para ejecutar las pruebas unitarias:  
```bash
pytest tests/
```  
Incluye tests para los módulos:  
- `data_handling.py`  
- `physics.py`  
- `visualization.py`

## 🤝 Contribución  
- https://chat.deepseek.com
- https://chatgpt.com/

## 📖 Documentación Técnica  
El directorio [`docs/`](docs/) contiene documentación detallada del proyecto, incluyendo:

- `introduccion.md`: Fundamentos del modelo de advección y su importancia en ciencias atmosféricas.  
- `ecuaciones.md`: Descripción de la ecuación de advección 1D, condiciones iniciales y de frontera.  
- `metodos.md`: Métodos numéricos implementados: Euler Backward, Leapfrog, RK4, etc.  
- `criterios_estabilidad.md`: Criterios de estabilidad, número de CFL, y análisis de Von Neumann.  
- `experimentos.md`: Configuraciones de simulación, condiciones de prueba y criterios de evaluación.  
- `referencias.md`: Bibliografía científica utilizada (formato APA7).


## ✉️ Contacto  
¿Preguntas? ¡Abre un *issue* o contacta a [@Japq91](https://github.com/Japq91).


