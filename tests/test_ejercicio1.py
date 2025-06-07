import os
import pytest
import pandas as pd
from funciones_pec4.ejercicio1 import ejercicio1


# Creamos un fixture para crear un archivo CSV en un directorio temporal
@pytest.fixture
def dummy_csv_file(tmpdir: os.path) -> str:
    """
    Creamos un fichero CSV dummy en un directorio temporal.
    :param tmpdir: os.path, directorio temporal.
    :return: str, ruta relativa del fichero csv.
    """

    file_path = tmpdir.join('test.csv')
    # Escribimos unas columnas y unas filas con valores dummy
    data = 'col1,col2,col3\n1,2,3\n4,5,6\n'
    with open(file_path, 'w') as f:
        f.write(data)
    return str(file_path)


def test_ejercicio1_carga_csv(dummy_csv_file: str) -> None:
    """
    Probamos lectura correcta del fichero csv
    :param dummy_csv_file: ruta del fichero csv.
    :return: None
    """

    # Obtenemos carpeta y nombre del fichero csv
    folder, filename = os.path.split(dummy_csv_file)

    # Ejecutamos el ejercicio1 con los argumentos dummy
    df = ejercicio1(filename=filename, folder=folder)

    # El objeto devuelto debe ser un DataFrame
    assert isinstance(df, pd.DataFrame), 'El resultado debe ser un DataFrame.'
    # Miramos el nombre de las columnas
    assert list(df.columns) == ['col1', 'col2', 'col3'], 'No coinciden las columnas del DataFrame.'
    # Comprobamos longitud del DataFrame
    assert len(df) == 2, 'Debería haber 2 filas en el DataFrame.'


def test_ejercicio1_ruta_no_encontrada(tmpdir: os.path)-> None:
    """
    Caso carpeta vacia (sin ningún csv)
    :param tmpdir: os.path, ruta del directorio temporal.
    :return: None
    """

    # Creamos directorio temporal falso
    folder: os.path = tmpdir.mkdir("data")

    # Se espera que ejercicio1() ejecute sys.exit()
    with pytest.raises(SystemExit):
        ejercicio1(folder=str(folder))


def test_ejercicio1_csv_no_encontrado() -> None:
    """
    Caso de fichero csv no encontrado.
    :return: None
    """
    # Establecemos ruta y fichero falsos
    folder: str = "non_existent_folder"
    filename: str = "missing.csv"

    # Debe ejecutar sys.exit()
    with pytest.raises(SystemExit):
        ejercicio1(filename=filename, folder=folder)


def test_ejercicio1_buscar_csv(dummy_csv_file: str, tmpdir) -> None:
    """
    Caso carpeta correcta y fichero csv sin especificar pero existente
    :param dummy_csv_file: str, nombre del fichero csv.
    :param tmpdir: str, ruta del directorio temporal.
    :return: None
    """
    folder: str = os.path.dirname(dummy_csv_file)

    # Ejecutamos ejercicio1 con carpeta temporal correcta
    df: pd.DataFrame = ejercicio1(folder=folder)

    assert isinstance(df, pd.DataFrame), 'Debe devolver un DataFrame.'
    assert len(df) == 2, 'La longitud del DataFrame debe ser 2.'
