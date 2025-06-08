import pandas as pd
from funciones_pec4.formatos import print_separador


def calcular_periodos_sequia(df: pd.DataFrame, nivel: float = 60.0) -> list[list[float]]:
    """
    Calcula los periodos de sequía de la serie 'nivell_perc_smooth' del DataFrame.
    Cuando el % de volumen es menor o inferior al nivel indicado.
    :param df: pd.DataFrame completo con los datos.
    :param nivel: float con el nivel de sequía. Por defecto 60%.
    :return: lista de listas con los periodos de sequía (valores tipo float).
    """

    df = df.copy()
    # Creamos máscara booleana donde se cumpla la condición:
    masc_bool: pd.Series = df['nivell_perc_smooth'] <= nivel
    # Lista donde añadiremos las listas de periodos
    periods = []

    # Variable para almacenar el inicio de cada período, empezamos sin ningún valor
    inicio = None
    for idx, condicion in enumerate(masc_bool):
        # Si la condición se cumple (nivel <= 60)
        if condicion:
            # Si no hay inicio, lo añadimos y continúamos
            if inicio is None:
                # Establecemos el inicio con el valor de ese índice en la serie 'dia_decimal'.
                # El siguiente 'iloc' devuelve numpy.array, con 'item' obtenemos el valor.
                inicio = df.iloc[idx]['dia_decimal'].item()
        else:
            # Buscamos el final del periodo
            if inicio is not None:
                # Valor del índice anterior que ya no cumple con la condición.
                final = df.iloc[idx - 1]['dia_decimal'].item()
                # Añadimos el periodo a la lista de periodos, redondeamos a un decimal
                periods.append([round(inicio, 1), round(final, 1)])
                # Ya tenemos un período completo, eliminamos el inicio para buscar uno nuevo
                # en las siguientes iteraciones.
                inicio = None


    return periods


def ejercicio5(df: pd.DataFrame) -> list[list[float]]:
    """
    Muestra por pantalla los periodos de sequía de la serie 'nivell_perc_smooth' del DataFrame.
    :param df: pd.DataFrame completo con los datos.
    :return: Lista de listas con los periodos de sequía.
    """

    periodos: list[list[float]] = calcular_periodos_sequia(df)
    print_separador()
    print("Lista de periodos de sequía:")
    print(periodos)
    print_separador()

    return periodos
