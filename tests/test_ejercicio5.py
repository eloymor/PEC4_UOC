import os
import pandas as pd
import pytest
from pathlib import Path
from funciones_pec4.ejercicio1 import ejercicio1
from funciones_pec4.ejercicio2 import ejercicio2
from funciones_pec4.ejercicio3 import ejercicio3
from funciones_pec4.ejercicio4 import ejercicio4
from funciones_pec4.ejercicio5 import ejercicio5

@pytest.fixture
def obtener_df() -> pd.DataFrame:
    """
    Función para obtener el DataFrame del ejercicio5.
    :return: pd.DataFrame cargado por el ejercicio4.
    """
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    path_csv: Path = BASE_DIR / "data"
    df: pd.DataFrame = ejercicio1(folder=str(path_csv))
    df_labaells: pd.DataFrame = ejercicio2(df)
    df_labaells= ejercicio3(df_labaells)
    df_labaells= ejercicio4(df_labaells)

    return df_labaells


def test_ejercicio5_completo(obtener_df: pd.DataFrame) -> None:
    """
    Comprueba la funcionalidad del ejercicio5.
    :param obtener_df: pd.DataFrame cargado por el ejercicio4.
    """

    periodos: list[list[float]] = ejercicio5(obtener_df)

    # Miramos tipo de retorno
    assert isinstance(periodos, list), 'Debe devolver una lista.'
    # Sabemos que la lista no puede estar vacía
    assert len(periodos) > 0, 'La lista no puede estar vacía.'
    # Comprobamos que sea una lista de listas
    assert all(isinstance(periodo, list) for periodo in periodos), \
        'Cada elemento de la lista debe ser una lista.'
    # Los valores de los periodos deben ser de tipo float
    assert all(isinstance(nivel, float) for periodo in periodos for nivel in periodo), \
        'Cada valor del periodo debe ser de tipo float.'
    # Sabemos que no hay periodos abiertos, todos tienen incio y final
    # (a fecha de creación de este ejercicio)
    assert all(len(periodo) == 2 for periodo in periodos), \
        'Cada elemento de la lista de periodos debe tener dos elementos (inicio, final).'
