import pandas as pd
import pytest
import os
from pathlib import Path
import datetime
from funciones_pec4.ejercicio1 import ejercicio1
from funciones_pec4.ejercicio2 import ejercicio2
from funciones_pec4.ejercicio3 import ejercicio3


@pytest.fixture
def obtener_df() -> pd.DataFrame:
    """
    Función para obtener el DataFrame del ejercicio3.
    :return: pd.DataFrame cargado por el ejercicio2.
    """

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    path_csv: Path = BASE_DIR / "data"
    df: pd.DataFrame = ejercicio1(folder=str(path_csv))
    df_labaells: pd.DataFrame = ejercicio2(df)

    return df_labaells


@pytest.fixture
def obtener_ruta_img() -> str:
    """
    Función para obtener la ruta de la imagen del ejercicio3.
    :return: str, ruta relativa de la imagen.
    """

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    path_img: Path = BASE_DIR / 'img'

    return str(path_img)


def test_ejercicio3_completo(obtener_df: pd.DataFrame) -> None:
    """
    Comprueba la funcionalidad del ejercicio3.

    :param obtener_df: pd.DataFrame cargado por el ejercicio2.
    :return: None
    """

    df = obtener_df
    df_labaells: pd.DataFrame = ejercicio3(df)

    # Comprobamos que tenemos un DataFrame
    assert isinstance(df_labaells, pd.DataFrame), 'Debe devolver un DataFrame.'
    # Comprobamos el cambio de formato de la columna 'dia'
    assert df_labaells['dia'].dtype == 'datetime64[ns]', \
        'La columna "dia" debe ser de tipo datetime64[ns].'
    # Comprobamos que la columna 'dia_decimal' tiene el formato correcto
    assert df_labaells['dia_decimal'].dtype in ['float64', 'float32', 'float'], \
        'la columna "dia_decimal" debe ser de tipo float.'



def test_ejercicio3_img(obtener_ruta_img: str) -> None:
    """
    Comprueba la creación del gráfico y la carpeta img.
    :param obtener_ruta_img: str, ruta relativa de la imagen.
    :return: None
    """
    # Listamos ficheros en la carpeta img
    try:
        img_list = os.listdir(obtener_ruta_img)
    except FileNotFoundError:
        pass

    assert os.path.exists(obtener_ruta_img), 'La carpeta img no existe.'
    assert len(img_list) > 0 , 'Debe haber almenos una imagen en la carpeta img.'
    assert img_list[0].endswith('.png'), 'La imagen debe tener extensión .png.'
    assert 'Eloy_Mor'.lower() in img_list[0].lower() , \
        'la imagen debe contener el nombre del alumno.'
