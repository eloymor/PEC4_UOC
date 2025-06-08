"""
Módulo con las funciones del ejercicio 2.
"""

import pandas as pd
from modules.formatos import print_separador


def ejercicio2(df: pd.DataFrame, filtro: str = 'La Baells') -> pd.DataFrame:
    """
    Modifica las columnas del DataFrame por unas más normalizadas,
    imprime en pantalla los pantanos únicos del DataFrame,
    limpia el campo 'estacio' del DataFrame, eliminando la palabra "Embassament de"
    y los parentesis y filtra el DataFrame por el campo 'estacio' según el parámetro filtro.
    (por defecto filtra por 'La Baells'.)

    :param df: pd.DataFrame del ejercicio 1
    :param filtro: palabra o texto con el que filtrar el pantano
    :return: pd.DataFrame con las columnas renombradas y filtrado
    """
    # Los pd.DataFrame son de tipo mutable, por lo que crearemos una copia para
    # no modificar el original (se está pasando la referencia al original a través
    # del argumento df de la función)
    df = df.copy()

    # Obtenemos las columnas originales y las renombramos con las proporcionadas
    columnas_iniciales: list[str] = list(df.columns)
    columnas_final: list[str] = ['dia', 'estacio', 'nivell_msnm', 'nivell_perc', 'volum']
    # Creamos un diccionario con las claves como las columnas originales
    # y los valores como las nuevas
    columnas_dict: dict[str, str] = dict(zip(columnas_iniciales, columnas_final))
    df.rename(columns=columnas_dict, inplace=True)

    # La variable pantanos_unicos realmente es de tipo numpy.array, pero para no cargar
    # modulos que no utilizaremos en este ejercicio, le añado la hint de tipo list
    # (a efectos prácticos será lo mismo)
    pantanos_unicos: list[str] = df['estacio'].unique()
    print_separador()
    print("Los pantanos únicos del DataFrame son:\n")
    for i, pantano in enumerate(pantanos_unicos):
        print(f"{i} - {pantano}\n")
    print_separador()

    # Utilizaremos la función str.replace de pandas con la cual podemos
    # utilizar expresiones regulares. Encadenaremos dos, una para eliminar
    # la palabra "Embassament de" y otra para eliminar los parentesis.
    # https://stackoverflow.com/questions/22588316/pandas-applying-regex-to-replace-values
    df['estacio'] = df['estacio'].str.replace(r'^Embassament de\s*', '', regex=True) \
        .str.replace(r'\s*\(.*?\)', '', regex=True)

    # Filtramos por el nombre del pantano, guardamos en un nuevo DataFrame,
    # convertimos todo a minúsculas para evitar errores de coincidencia
    df_filtrado: pd.DataFrame = df.loc[df['estacio'].str.lower() == filtro.lower()]

    # Devolvemos el DataFrame filtrado
    return df_filtrado
