"""
Test ejercicio4.py.
"""

import os
from pathlib import Path
import pandas as pd
import pytest
from modules.ejercicio1 import ejercicio1
from modules.ejercicio2 import ejercicio2
from modules.ejercicio3 import ejercicio3
from modules.ejercicio4 import ejercicio4

@pytest.fixture
def obtener_df() -> pd.DataFrame:
    """
    Función para obtener el DataFrame del ejercicio4.
    :return: pd.DataFrame cargado por el ejercicio3.
    """
    base_dir: Path = Path(__file__).resolve().parent.parent
    path_csv: Path = base_dir / "data"
    df: pd.DataFrame = ejercicio1(folder=str(path_csv))
    df_labaells: pd.DataFrame = ejercicio2(df)
    df_labaells= ejercicio3(df_labaells)

    return df_labaells


@pytest.fixture
def obtener_ruta_img() -> str:
    """
    Función para obtener la ruta de la imagen del ejercicio4.
    :return: str, ruta relativa de la imagen.
    """

    base_dir: Path = Path(__file__).resolve().parent.parent
    path_img: Path = base_dir / 'img'

    return str(path_img)

def test_ejercicio4_completo(obtener_df: pd.DataFrame) -> None:
    """
    Comprueba la funcionalidad del ejercicio4.
    :param obtener_df: pd.DataFrame cargado por el ejercicio3.
    """

    df_labaells: pd.DataFrame = ejercicio4(obtener_df)

    # Comprobamos que tenemos un DataFrame
    assert isinstance(df_labaells, pd.DataFrame), 'Debe devolver un DataFrame.'
    # Comprobamos columna 'nivell_perc_smooth' (con filtro savgol)
    assert 'nivell_perc_smooth' in df_labaells.columns, \
        'La columna "nivell_perc_smooth" no existe.'
    # Comprobamos el dtype de la columna 'nivell_perc_smooth'
    assert df_labaells['nivell_perc_smooth'].dtype in ['float64', 'float32', 'float'], \
        'La columna "nivell_perc_smooth" debe ser de tipo float.'


def test_ejercicio4_img(obtener_ruta_img: str) -> None:
    """
    Comprueba la creación del gráfico y la carpeta img.
    :param obtener_ruta_img: str, ruta relativa de la imagen.
    :return: None
    """
    # Listamos ficheros en la carpeta img
    sorted_img_list: list = [] # inicializamos variable (vacía)
    try:
        img_list = os.listdir(obtener_ruta_img)
        # Ordenamos la lista de ficheros por longitud, orden ascendente
        sorted_img_list = sorted(img_list, key=len)

    except FileNotFoundError:
        pass

    assert os.path.exists(obtener_ruta_img), 'La carpeta img no existe.'
    assert len(sorted_img_list) > 0 , 'Debe haber almenos una imagen en la carpeta img.'
    assert sorted_img_list[-1].endswith('.png'), 'La imagen debe tener extensión .png.'
    assert 'Smoothed_Eloy_Mor'.lower() in sorted_img_list[-1].lower() , \
        'la imagen debe contener el nombre del alumno.'
