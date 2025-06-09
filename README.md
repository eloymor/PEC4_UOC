# PEC 4 - Programación para la ciencia de datos  (UOC)

Proyecto escrito en Python para la práctica cuatro (**PEC4**) de la asignatura **Programación para la ciencia de datos**, 
UOC. Este programa ejecuta una serie de ejercicios de forma secuencial o individual con funciones de procesamiento y analisis
de datos. Se ha diseñado para funcionar a través de la terminal de comandos.


Autor: **Eloy Mor**  
Fecha: **06/06/2025**

---

## Características 

- **Command-line Interface (CLI):** Especifica el número de ejercicio con un simple comando de la terminal.
- **Multiples ejercicios:** Los ejercicios se evaluan de forma secuencial, siempre se ejecutarán los ejercicios anteriores al especificado.
- **Control de ficheros CSV:** Carga y procesa automáticamente ficheros `.csv` ubicados en la carpeta especificada.
- **Opciones de personalización:** Se puede especificar el nombre concreto del fichero y la carpeta donde buscar.
- **Código modular y reutilizable:** Cada ejercicio tiene una función / módulo dedicado.

---

## Instalación del módulo `PEC4`

Por favor, consultar el archivo `INSTALL.md`.

---

## Utilización del programa `PEC4`

Ejecuta el programa con la línea de comandas (terminal). Las siguientes opciones están disponibles:


### Comandos:
- `-ex`: Indica el ejercicio a ejecutar (ej: `-ex 1` para ejercicio 1, `-ex 2` para ejercicio 1 y 2, etc.). 
0 para ejecutarlos todos.
- `-filename`: Indica el nombre del fichero `.csv` a analizar. Si se omite, el primer fichero `.csv` por orden 
alfabético en la carpeta especificada, será el que se utilizará.
- `-folder`: Define la ruta a la carpeta dónde se encuentre el fichero `.csv`. Por defecto: `./data`.
- `-h` o `--help`: Muestra la ayuda.

### Ejemplos de utlización:

- Ejecuta todos los ejercicios con la configuración por defecto:
  ```bash
  python main.py
  ```
- Ejecuta un ejercicio en concreto (por ejemplo el ejercicio 1):
  ```bash
  python main.py -ex 1
  ```
- Ejecuta un ejercicio con un archivo y carpeta especificada:
  ```bash
  python main.py -ex 2 -filename data.csv -folder ./data_files
  ```
  
**IMPORTANTE:** Todas las rutas indicadas deben ser **relativas** al directorio **raíz** del proyecto.

---
