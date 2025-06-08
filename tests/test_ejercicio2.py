from pathlib import Path
import pytest
import pandas as pd
from modules.ejercicio1 import ejercicio1
from modules.ejercicio2 import ejercicio2


# Creamos fixture con el DataFrame original, necesario para este test.
@pytest.fixture
def obtener_df() -> pd.DataFrame:
    """
    Función para obtener el DataFrame de prueba.
    :return: pd.DataFrame cargado por el ejercicio1.
    """

    # Buscamos la rura principal del proyecto
    # https://stackoverflow.com/questions/30218802/get-parent-of-current-directory-from-python-script
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    # Para este test necesitamos el fichero csv auténtico, la función ejercicio1() buscara
    # el archivo csv en la carpeta data/
    path_csv: Path = BASE_DIR / "data"
    df: pd.DataFrame = ejercicio1(folder=str(path_csv))

    return df


def test_ejercicio2_completo(obtener_df: pd.DataFrame) -> None:
    """
    :param obtener_df: pd.DataFrame cargado por el ejercicio1.
    :return: None
    """

    # Obtenemos el DataFrame modificado por ejercicio2
    df_labaells: pd.DataFrame = ejercicio2(obtener_df)

    # Comprobamos que tenemos un DataFrame
    assert isinstance(df_labaells, pd.DataFrame), 'Debe devolver un DataFrame.'
    # Comprobamos el nombre de las columnas
    assert list(df_labaells.columns) == ['dia', 'estacio', 'nivell_msnm', 'nivell_perc', 'volum'], \
        'No coinciden las columnas del DataFrame.'
    # Comprobamos que no hay ningún 'Embassament de' en la columna estacio
    assert not df_labaells['estacio'].isin(['Embassament de']).any(), \
        'Los nombres de los pantanos no se han limpiado'
    # Solo debe haber un pantano (La Baells)
    assert df_labaells['estacio'].nunique() == 1, 'No se han filtrado los pantanos.'
    # Si se cumple la assertion anterior, el pantano único debe ser 'La Baells'
    assert df_labaells['estacio'].value_counts().index[0].lower() == 'La Baells'.lower(), \
        'No se han filtrado los pantanos.'
