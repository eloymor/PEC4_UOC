"""
Módulo con las funciones del ejercicio 4.
"""

import pandas as pd
from scipy.signal import savgol_filter
import numpy as np
from modules.plotting import line_plot


def filtro_savgol(df: pd.DataFrame,
                  atr: str = 'nivell_perc',
                  window: int = 1500,
                  order: int = 3) -> (
        pd.DataFrame):
    """
    Aplica el filtro Savitzky-Golay a la serie indicada.

    :param df: pd.DataFrame con los datos.
    :param atr: str con el nombre de la serie a suavizar.
    :param window: int con el tamaño del filtro.
    :param order: int con el orden del filtro.
    :return: pd.DataFrame con la serie suavizada en una nueva columna.
    """
    df = df.copy()
    # Convertimos la serie a un numpy array
    x = np.array(df[atr])
    # Aplicamos el filtro
    filtro: np.array = savgol_filter(x, window, order)
    # Creamos la nueva columna con el resultado del filtro
    df[f"{atr}_smooth"]: pd.Series = filtro

    return df


def ejercicio4(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica el filtro Savitzky-Golay (savgol) a la serie 'nivell_perc' del DataFrame y guarda
    un gráfico de líneas con el volumen (con y sin filtro) vs. tiempo.
    :param df: pd.DataFrame con los datos del ejercicio anterior.
    :return: pd.DataFrame con la serie suavizada en una nueva columna.
    """

    df = df.copy()
    # Aplicamos el filtro
    df = filtro_savgol(df)
    # Creamos y guardamos gráfico
    line_plot(df, smoothen=True)

    return df
