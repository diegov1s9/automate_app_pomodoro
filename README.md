# App Pomodoro - Proyecto de Pruebas Automatizadas

Este repositorio contiene un conjunto de pruebas automatizadas diseñadas para garantizar la funcionalidad y estabilidad de la aplicación web basada en la técnica de Pomodoro. Las pruebas están desarrolladas en **Python** utilizando **Selenium** y **Pytest**, siguiendo las mejores prácticas de automatización de pruebas.

---

## 🎯 **Propósito del Proyecto**

El propósito principal de este proyecto es proporcionar un entorno robusto para validar la aplicación web, asegurando que los componentes clave funcionen correctamente y mejorando la calidad del software.

---

## 🚀 **Requisitos del Entorno**

Para ejecutar las pruebas automatizadas, asegúrate de contar con lo siguiente:

- **Python** 3.8 o superior
- **Selenium**
- **Pytest**
- **pytest-html** para la generación de reportes

---

## 🛠 **Instalación**

### Clonar el Repositorio

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

### Configurar un Entorno Virtual

Si prefieres configurar tu entorno localmente

1. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instala las dependencias:

```bash
# En Linux/Mac:
pip install -r requirements.txt
# En Windows (si tienes problemas con pip):
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 🐳 Configuración con Docker

Si prefieres usar Docker para un entorno pre configurado:

1. Construye la imagen:

```bash
docker build -t nombre-de-tu-imagen .
```

2. Ejecuta el contenedor:

```bash
docker run  --rm nombre-de-tu-imagen
```

### 🔧 Configuración

Antes de ejecutar las pruebas:

1. Configura el archivo data.py con las URLs y credenciales necesarias.

### 🧪 Ejecución de Pruebas

#### Ejecutar Todas las Pruebas

Para ejecutar todas las pruebas disponibles:

```bash
pytest
```

#### Generar Reportes

Para generar un reporte HTML detallado:

```bash
python -m pytest -s -v -p no:logging --html=reports/report.html test_app_pomodoro.py::TestAppPomodoro

```

#### Ejecutar un Test específico

Si deseas ejecutar una prueba individual:

```bash
python -m pytest -s -v -p no:logging --html=reports/report.html test_app_pomodoro.py::TestAppPomodoro::test_edit_task
```

### 📁 Estructura del Proyecto

```bash
app_pomodoro/
├── logs/                 # Archivos de registro
│   └── homepage.log
├── pages/                # Clases de página (Page Objects)
│   └── home_page.py
├── reports/              # Reportes HTML
│   ├── assets/
│   │   └── style.css
│   └── report.html
├── utils/                # Funciones utilitarias y configuraciones
│   ├── logger.py
│   └── utils.py
├── .gitignore            # Archivos ignorados por Git
├── data.py               # Configuración y constantes
├── README.md             # Documentación del proyecto
├── requirements.txt      # Dependencias del proyecto
├── selector.py           # Selectores de elementos
├── test_app_pomodoro.py  # Archivo principal de pruebas
└── Dockerfile.py         # Instrucciones para crear una image de Docker
```

### ✅ Mejores Prácticas en el Proyecto

#### Manejo de Errores

- Se utiliza logging para registrar errores de manera estructurada en lugar de imprimir directamente en la consola.
  Los mensajes de error son claros y concisos para facilitar la depuración.

#### Uso de Lazy Formatting

- Para evitar problemas con el formato de cadenas, se sigue la recomendación de Pylint: usar % en lugar de f-strings en los mensajes de log.

### 📊 Generación de Reportes

Los reportes generados en formato HTML están disponibles en la carpeta reports/ para facilitar la revisión de resultados.
