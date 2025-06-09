"""
Módulo auxiliar con funciones para graficar.
"""

import os
from pathlib import Path
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from modules.formatos import print_separador

# Desactivamos la salida de gráficos en la terminal,
# evitamos posibles errores al ejecutar los tests con pytest.
matplotlib.use('Agg')


sns.set_style("whitegrid") # Estilo general de seaborn
plt.style.use('seaborn-v0_8-whitegrid') # Estilo general de matplotlib

# Controlamos que la salida de las imágenes sea en el directorio raíz del proyecto
abs_path: Path = Path(__file__).resolve().parent.parent.parent

def line_plot(df: pd.DataFrame, smoothen: bool = False) -> None:
    """
    Guarda una imagen con el gráfico de líneas de la serie volum vs tiempo.

    :param df: pd.DataFrame con los datos a graficar.
    :param smoothen: booleano que indica si se debe graficar la serie suavizada.
    :return: None: no retorna nada.
    """

    # Creamos carpeta 'img' si no existe, para evitar posible error de ejecución
    if not os.path.exists(os.path.join(abs_path, 'img')):
        os.makedirs(os.path.join(abs_path, 'img'))

    # Creamos la única figura de este gráfico, definimos tamaño
    fig: plt.Figure = plt.figure(figsize=(10, 6))

    # Opción con savgol_filter
    if smoothen:
        # Gráfico original, sin suavizar
        ax = sns.lineplot(x='dia_decimal', y='nivell_perc', data=df, label='Original')
        # Gráfico suavizado, con línea de ancho 3, unimos al axe del original
        sns.lineplot(x='dia_decimal',
                     y='nivell_perc_smooth',
                     data=df,
                     ax=ax,
                     linewidth=3,
                     label='Suavizado')
        # Mostramos la leyenda, posición inferior centro
        ax.legend(loc='lower center')
        # Para posterior guardado de la imagen
        nombre: str = 'smoothed_eloy_mor'

    # Opción sin savgol_filter
    else:
        ax = sns.lineplot(x='dia_decimal', y='nivell_perc', data=df)
        nombre: str = 'eloy_mor'


    # Añadimos título y etiquetas de ejes
    ax.set_title('Volumen de la baells')
    ax.set_xlabel('Año')
    ax.set_ylabel('% Volumen')
    # Añadimos subtítulo con el nombre
    fig.suptitle('Eloy Mor')
    # Guardamos imagen
    ruta_img: str = os.path.join(abs_path, 'img', nombre + '.png')
    plt.savefig(ruta_img)
    # Cerramos figura
    plt.close(fig)
    print_separador()
    print(f"Imágen guardada correctamente en '{ruta_img}'")
    print_separador()
