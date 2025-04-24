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
8. [Contribución](#-contribución)  
9. [Licencia](#-licencia)  

## 🎯 Descripción  
Este proyecto simula el transporte de un contaminante en un flujo unidimensional usando:  
- **Esquema Euler Backward** para la discretización temporal.  
- 
- **Condiciones periódicas** en los bordes del dominio.  
- Visualización interactiva con `matplotlib` y `xarray`.  

**Aplicaciones**: Modelado atmosférico, dispersión de contaminantes, dinámica de fluidos.  

## 📂 Estructura del Proyecto  
```plaintext
atMOdel/  
├── src/                   # Código fuente  
│   ├── physics.py         # Funciones matemáticas (gaussiana, Euler backward)  
│   ├── visualization.py   # Gráficos 2D/3D y estilos  
│   ├── data_handling.py   # Manejo de datasets (xarray)  
│   └── main.py            # Script principal  
├── outputs/               # Resultados  
│   ├── figures/           # Gráficos (PNG)  
│   └── logs/              # Registros (opcional)  
├── tests/                 # Pruebas unitarias  
├── docs/                  # Documentación adicional  
├── README.md              # Este archivo  
├── requirements.txt       # Dependencias  
└── .gitignore             # Archivos ignorados por Git  
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
### Ejecutar la simulación completa (test):  
```bash
python src/main.py
```  

### Parámetros configurables (en `src/main.py`):  
```python
u = 10       # Velocidad de advección (m/s)  
Nx = 101     # Puntos en la malla  
dx = 500     # Espaciado del grid (m)  
dt = ...      # Paso de tiempo (s)  
```  

### Generar gráficos personalizados:  
Modifica `visualization.py` para ajustar:  
- Colormaps (`custom_bwr`).  
- Vistas 3D (`ax.view_init`).  

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
- falta editar

## 🤝 Contribución  
1. DeepSeek

## ✉️ Contacto  
¿Preguntas? ¡Abre un *issue* o contacta a [@tu-usuario](https://github.com/tu-usuario).  

