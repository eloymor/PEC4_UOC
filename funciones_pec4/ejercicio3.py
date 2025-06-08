"""
Módulo con las funciones del ejercicio 3.
"""

import pandas as pd
from funciones_pec4.formatos import print_separador
from funciones_pec4.fechas import to_year_fraction
from funciones_pec4.plotting import line_plot


def ejercicio3(df: pd.DataFrame) -> pd.DataFrame:
    """
    Modifica la serie 'dia' de tipo str a tipo datetime.
    Ordena el DataFrame por la serie 'dia' en orden ascendente.
    Imprime la fecha minima y maxima de la serie 'dia' del DataFrame.
    Añade una nueva columna 'dia_decimal' al DataFrame.
    Guarda un gráfico con el volumen vs. tiempo.

    :param df: pd.DataFrame del ejercicio anterior
    :return: pd.DataFrame ordenado por fecha (dia) y con la nueva columna 'dia_decimal'
    """

    df = df.copy()

    # Convertimos la serie 'dia' a datetime directamente con la función pd.to_datetime.
    # Sobreescribimos la misma serie
    df['dia']: pd.Series = pd.to_datetime(df['dia'], format='%d/%m/%Y')

    print_separador()
    # Mostramos el total de registros (longitud del DataFrame)
    print(f"Total de registros: {len(df)}")

    # Ordenamos el DataFrame por la serie 'dia' en orden ascendente
    df: pd.DataFrame = df.sort_values(by='dia', ascending=True)

    # Reiniciamos el índice del DataFrame
    df = df.reset_index(drop=True)

    # En vez de escoger el 1er y último registro, obtenemos la fecha minima
    # y maxima de la serie 'dia' con el método .min() y .max(). Cambiamos
    # el formato de la fecha a mostrar a dd/mm/aaaa.
    fecha_min = df['dia'].min().strftime('%d/%m/%Y')
    fecha_max = df['dia'].max().strftime('%d/%m/%Y')

    # Mostramos la fecha minima y maxima
    print(f"Fecha minima: {fecha_min} (dd/mm/aaaa)")
    print(f"Fecha maxima: {fecha_max} (dd/mm/aaaa)")
    print_separador()

    # Función toYearFraction cargada del módulo pec4.fechas.
    # Creamos la nueva columna, recorremos la serie 'dia' con apply y la combinación
    # de la función lambda + toYearFraction.
    df['dia_decimal'] = df['dia'].apply(lambda x: to_year_fraction(x))

    # Función line_plot cargada del módulo pec4.plotting.
    # Guardamos un gráfico con la serie 'dia_decimal' vs. 'nivell_perc'
    line_plot(df)

    return df
