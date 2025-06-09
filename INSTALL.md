# Instalación

Este documento contiene los detalles para instalar el proyecto PEC4, el cual contiene módulos específicos.

## Prerrequisitos

- **Version de Python:** Este proyecto solo es compatible con Python > 3.9. 
- Se recomienda instalar este programa dentro de un entorno virtual. Ejemplo con `pip`:
    ```bash
   pip install virtualenv
   virtualenv venv
   ```
    Activación del entorno en Windows:
    ```bash
   .\venv\Scripts\activate
   ```
   Activación en Linux/macOS:
    ```bash
   source venv/bin/activate
   ```
- Es necesario instalar `setuptools` en el entorno para ejecutar el script de instalación (`pip`):
    ```bash
  pip install setuptools
  ```
---
## Instalación del programa

- Situarse en el directorio **raíz** del proyecto:
    ```bash
  cd PEC4
  ```
- Ejecuta el script de instalación:
    ```bash
  python setup.py sdist
  pip install -e .
  ```
    Se recomienda la instalación arriba indicada (opción editable) para evitar errores de dependencias al ejecutar los 
tests.


**Nota: Este script de instalación también añadirá todas las librerías y paquetes necesarios para el funcionamiento de
este programa al entorno de trabajo activo.**


En caso de error, se pueden instalar de forma manual con `pip`:
```bash
    pip install -r requirements.txt
   ```
