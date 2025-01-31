# Proyecto RPA File

Este proyecto está diseñado para monitorear una carpeta específica y procesar archivos nuevos automáticamente.

## Organización de Carpetas

La estructura de carpetas del proyecto es la siguiente:

```
rpa-file/
│
├── bot/
│   ├── __init__.py
│   ├── file_watcher.py
│   └── file_processor.py
│
├── .gitignore
└── README.md
```

- **bot/**: Contiene los scripts principales del proyecto.
  - **file_watcher.py**: Script que monitorea la carpeta especificada y detecta nuevos archivos.
  - **file_processor.py**: Script que procesa los archivos detectados.
  - **__init__.py**: Archivo para tratar el directorio como un paquete.

## Herramientas Utilizadas

- **Python**: Lenguaje de programación principal utilizado en el proyecto.
- **Watchdog**: Biblioteca de Python utilizada para monitorear el sistema de archivos y detectar cambios en tiempo real.
- **OS**: Módulo de Python utilizado para interactuar con el sistema operativo.
- **Time**: Módulo de Python utilizado para manejar operaciones relacionadas con el tiempo.

## Cómo Empezar

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando `pip install -r requirements.txt`.
3. Ejecuta el script `file_watcher.py` para comenzar a monitorear la carpeta especificada.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.
