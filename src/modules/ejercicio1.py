"""
Módulo con las funciones del ejercicio 1.
"""

import os
from pathlib import Path
import sys
import pandas as pd
from modules.formatos import print_separador


def ejercicio1(filename: str | None = None, folder: str = 'data') -> pd.DataFrame | None:
    """
    Carga un fichero .csv en un DataFrame y muestra información del DataFrame.

    :param filename: Nombre con extensión del fichero a cargar.
    Si no se especifica, se carga el primer fichero de tipo .csv en la carpeta indicada.
    :param folder: Carpeta donde buscar el fichero. Por defecto 'data'.
    :return: pd.DataFrame con el fichero cargado, en caso de error retorna None.
    """
    # El script main.py se encuentra en la carpeta src, por lo que la ruta relativa a la raíz
    # del proyecto no va a funcionar. Convertimos, de forma transparente para el usuario,
    # a ruta absoluta.
    abs_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')

    # Si la ruta del fichero no se especifica, se carga el primer fichero de tipo .csv
    # en la carpeta indicada, por defecto 'data'.
    if filename is None:
        # listamos todos los archivos de la carpeta data
        try:
            file_list: list[str] = os.listdir(os.path.join(abs_path, folder))
        except FileNotFoundError:
            print(f"Error: La carpeta '{folder}' no se encuentra.")
            sys.exit(1) # Detenemos ejecución (código 1 - error)
        # guardamos en una lista solo los que son de tipo .csv, ordenados alfabéticamente
        csv_files: list[str] = sorted([file for file in file_list if file.endswith('.csv')])
        # Nos quedamos con el primer fichero de la lista. Aunque solo debería haber uno,
        # tenemos que forzar la función escoger un solo fichero.
        try:
            filename = csv_files[0]
        except IndexError:
            print(f"Error: La carpeta '{folder}' no contiene ningún fichero .csv.")
            sys.exit(1)

    # Añadimos bloque try-except para controlar errores de carga
    try:
        # Cargamos el fichero en un DataFrame
        df = pd.read_csv(os.path.join(abs_path, folder, filename))
    # Excepción para error de ruta
    except FileNotFoundError:
        print(f"Error: El fichero '{filename}' no se encuentra en la carpeta '{folder}'.")
        sys.exit(1)
    # Excepción genérica
    except Exception as e:
        print(f"Error:Ocurrió un error al cargar el fichero '{filename}': {e}")
        sys.exit(1)

    print(f"\nMostrando las 5 primeras filas del fichero '{filename}':")
    print_separador()
    print(df.head())
    print_separador()

    print("\n\nMostrando las columnas originales del DataFrame:")
    print_separador()
    print(list(df.columns))
    print_separador()

    print("\n\nMostrando información del DataFrame:")
    print_separador()
    print(df.info())
    print_separador()

    # Devolvemos el DataFrame cargado
    return df
