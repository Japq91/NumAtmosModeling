# atMOdel 🌪️
**Modelo Numérico de Advección con diferentes Esquemas**  
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
├── p01_run_simulation.py      # Script principal con gestión de outputs  
├── p02_gif_image.py           # Script para crear animaciones .gif  
├── outputs/               # Resultados de simulación  
│   ├── data/              # Archivos NetCDF (.nc)  
│   └── figures/           # Imágenes y animaciones  
├── tests/                 # Pruebas unitarias  
│   ├── test_data/         # Datos para pruebas  
│   ├── test_physics.py    # Pruebas del módulo físico  
│   └── ...                # Otros archivos de test  
├── docs/                  # Documentación técnica completa  
│   ├── 01_Introduction.md  
│   ├── 02_Equation.md  
│   ├── 03_Methods.md  
│   ├── 04_Stability.md  
│   ├── 05_Experiments.md  
│   └── 06_Referenc.md  
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
### Configuración básica  
Los scripts aceptan parámetros clave para personalizar la simulación:  
- `--dt`: Paso de tiempo (default: `40`)  
- `--nr`: Ancho de la gaussiana (default: `10`)  
- `--profile`: Perfil inicial (`gauss` o `rectg`, default: `gauss`)  

---

### Paso 1 – Ejecutar la simulación  
```bash
python p01_run_simulation.py [--dt 40] [--nr 10] [--profile gauss|rectg]
```  
**Ejemplos**:  
```bash
# Gaussiana estrecha (nr=2)
python p01_run_simulation.py --nr 2 --profile gauss

# Pulso rectangular
python p01_run_simulation.py --profile rectg
```  

**Salidas generadas**:  
- `outputs/data/`
  - `EulerBackward_dt[VALOR]_CFL[VALOR]_dx500_profile[gauss|rectg]_nr[VALOR]_numerical.nc` (resultados numéricos)  
  - `EulerBackward_dt[VALOR]_CFL[VALOR]_dx500_profile[gauss|rectg]_nr[VALOR]_analytical.nc` (solución analítica)  
- `outputs/figures/EulerBackward/`  
  - Imágenes `.png` para cada paso de tiempo (ej: `3D000_EulerBackward_dt40_...png`)  

### Paso 2 – Generar animación `.gif` con los resultados:  

```bash
python p02_gif_image.py --method [NOMBRE_MÉTODO] --dt [VALOR] --profile [gauss|rectg] [--nr VALOR] [--type numerical|analytical]
```

```bash
# Animación numérica con perfil gaussiano
python p02_gif_image.py --method "Euler Backward" --dt 40 --profile gauss --nr 5
# Animación analítica con perfil rectangular
python p02_gif_image.py --method "Euler Forward" --dt 60 --profile rectg --type analytical
```

### Parámetros configurables:
Los siguientes parámetros se pueden modificar dentro de `p01_run_simulation.py` y `p02_gif_image.py`:
```python
u = 10       # Velocidad de advección (m/s)  
Nx = 101     # Número de puntos espaciales  
dx = 500     # Espaciado del grid (m)  
dt = 40      # Paso de tiempo (s)  
nr = 10      # Control del ancho de la gaussiana inicial
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


