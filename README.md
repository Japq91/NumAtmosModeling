# atMOdel
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
8. [Contribución](#-contribución)  
9. [Documentación Técnica](#-documentación-técnica)  


## 🌟 Descripción  
Este proyecto simula el transporte de un contaminante en un flujo unidimensional usando:  
- **Esquema Euler Backward** para la discretización temporal.  
- **Condiciones periódicas** en los bordes del dominio.  
- Visualización interactiva con `matplotlib` y `xarray`.  

**Aplicaciones**: Modelado atmosférico, dispersión de contaminantes, dinámica de fluidos.  

## 📂 Estructura del Proyecto  
```plaintext
atMOdel/  
├── src/                   # Código fuente  
│   ├── physics.py         # Cálculos numéricos (Euler backward)  
│   ├── data_handling.py   # Manejo de datos NetCDF  
│   └── visualization.py   # Visualización 3D  
├── p01_run_simulation.py  # Script principal de simulación  
├── p02_generate_plots.py  # Generador de gráficos  
├── p03_make_animation.py  # Creador de animaciones  
├── outputs/               # Resultados  
│   ├── data/              # Archivos NetCDF (.nc)  
│   ├── figures/           # Imágenes estáticas  
│   └── animations/        # Animaciones GIF  
├── docs/                  # Documentación técnica  
│   ├── 01_Introduction.md  
│   ├── 02_Equation.md  
│   ├── ...  
└── requirements.txt       # Dependencias  
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
git clone https://github.com/Japq91/atMOdel.git
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

### Paso 1 – Ejecutar la simulación  
```bash
python p01_run_simulation.py --method [NOMBRE_MÉTODO] --dt [VALOR] --profile [gauss|rectg] --nr [VALOR]

```  
**Ejemplos**:  
```bash
python p01_run_simulation.py --method "Euler Backward" --dt 30 --profile gauss --nr 10
```  
### Paso 2 – Generar animación `.gif` con los resultados:  

```bash
python p02_gif_image.py --numerical [NOMBRE_MÉTODO] --dt [VALOR] --profile [gauss|rectg] [--nr VALOR]
```  
**Ejemplos**:  
```bash
python p02_generate_plots.py --numerical "Euler Backward" --dt 30 --profile gauss --nr 10
python p02_generate_plots.py --analytical "Euler Backward" --dt 30 --profile gauss --nr 10

```

### Paso 3 – Generar animación `.gif` con los resultados:  

```bash
python p03_make_animation.py --numerical [NOMBRE_MÉTODO] --dt [VALOR] --profile [gauss|rectg] [--nr VALOR]
```
**Ejemplos**:  
```bash
# Animación numérica con perfil gaussiano
python p03_make_animation.py --numerical "Euler Backward" --dt 30 --profile gauss --nr 10
# Animación analítica con perfil rectangular
python p03_make_animation.py --analytical "Euler Backward" --dt 30 --profile gauss --nr 10
```
### Parámetros configurables:  
| Parámetro | Descripción | Valores típicos |  
|-----------|-------------|-----------------|  
| `--dt`    | Paso temporal | 25-120 (segundos) |  
| `--profile` | Perfil inicial | `gauss` o `rectg` |  
| `--nr`    | Ancho gaussiano | 2-10 |  

## 📊 Ejemplos de Código  
### Simulación básica:  
```python
from physics import gauss, euler_backward_step  
Cn = [gauss(x, 0, nr=10, u=10, dx=500, Nx=101) for x in range(101)]  
Cnp1 = euler_backward_step(Cn, u=10, dt=60, dx=500, Nx=101)  
```  

### Visualización 3D:  
```python
from visualization import plot_3d_surface  
plot_3d_surface(dataset, metodo="Euler Backward", ti=115, dt=60, CFL=1.2)  
```  

## 📌 Resultados  
Ejemplos de salidas generadas:  
- **Datos numéricos**: `outputs/data/EulerBackward_dt30_CFL0.6_dx500_profilegauss_nr10_numerical.nc`  
- **Gráficos 3D**: `outputs/figures/EulerBackward/3D000_EulerBackward_*.png`  
- **Animaciones**: `outputs/animations/EulerBackward_dt30_profilegauss_nr10_numerical_cropped.gif`  

## 🧪 Pruebas (no mostrado)
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

- `01_Introduction.md`: Fundamentos del modelo de advección y su importancia en ciencias atmosféricas.  
- `02_Equation.md`: Descripción de la ecuación de advección 1D, condiciones iniciales y de frontera.  
- `03_Methods.md`: Métodos numéricos implementados: Euler Backward, Leapfrog, RK4, etc.  
- `04_Stability.md`: Criterios de estabilidad, número de CFL, y análisis de Von Neumann.  
- `05_Experiments.md`: Configuraciones de simulación, condiciones de prueba y criterios de evaluación.  
- `06_Referenc.md`: Bibliografía científica utilizada (formato APA7).

## 📜 Versiones
| Versión | Cambios Importantes                     | Fecha       |
|---------|----------------------------------------|-------------|
| v2.0.0  | Refactorización mayor del proyecto      | Jun 2024    |
| v1.0.0  | Versión inicial estable                | May 2024    |

## ✉️ Contacto  
¿Preguntas? ¡Abre un *issue* o contacta a [@Japq91](https://github.com/Japq91).


