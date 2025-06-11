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

- Sitúate en el directorio donde se encuentra el fichero main.py (`./src/`):
    ```bash
  cd src
    ```
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

### Fichero `.csv`:


Dentro del archivo comprimido (`.zip`), junto con el resto del proyecto, ya se incluye la carpeta `\data` con el
corresopndiente dataset a utilizar.

El fichero `.csv` se puede obtener del siguiente enlace:
- [Enlace al dataset](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr/about_data)

---

## Tests

Los tests se ejecutan mediante la librería `pytest`. Adicionalmente, para el cálculo de cobertura del código principal
mediante tests, se utiliza la librería `pytest-cov`. Si se ha ejecutado el scrip de instalación mediante `setuptools`, 
estas ya estarán instaladas en el entorno de trabajo.
En caso contrario instalar desde el fichero `requirements.txt` o manualmente con `pip`:
```bash
    pip install -r requirements.txt
```
o bien
```bash
    pip install pytest
    pip install pytest-cov
```
Para ejecutar los tests, ejecutamos el siguiente comando en el directorio **raíz** del proyecto:
```bash
    pytest .
```

Para ejecutar los test y además mostrar su cobertura, debemos ejecutar el siguiente comando en el directorio **raíz** del
proyecto:
```bash
    pytest --cov=modules --cov-report=term-missing tests/
```

---

## Linter

He utilizado la librería `pylint`.

**NOTA:** Este paquete no se contempla en el fichero `requirements.txt`, ya que realmente no es necesario para la
ejecución de este proyecto, además que se podría utilizar cualquier otro linter.

Se puede instalar con `pip`:
```bash
    pip install pylint
```
Para ejecutar pylint, nos situamos dentro la carpeta `src/`:
```bash
    cd src
```
Ejecutamos pylint en la carpeta src para analizar los ficheros de la carpeta modules y main.py:
```bash
    pylint .
```
Si se quiere analizar los test, nos debemos colocar otra vez en la carpeta **raíz** del proyecto y ejecutar:
```bash
    pylint .\tests\
```

---

## Documentación

Se encuentra disponible en la carpeta `doc/`, en el directorio principal. Abrir el fichero `index.html` en un navegador.

---
