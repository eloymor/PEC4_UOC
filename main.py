import argparse
import sys
import pandas as pd
from funciones_pec4.formatos import print_header
from funciones_pec4.ejercicio1 import ejercicio1
from funciones_pec4.ejercicio2 import ejercicio2
from funciones_pec4.ejercicio3 import ejercicio3
from funciones_pec4.ejercicio4 import ejercicio4
from funciones_pec4.ejercicio5 import ejercicio5


def main():
    """
    Función principal del programa.
    :return: None
    """
    # Creación del parser de argumentos
    parser = argparse.ArgumentParser(description="""Linea de comandos para ejecutar la PEC 4 de la
    asignatura Programación para la ciencia de datos de la UOC. Autor: Eloy Mor. (06/06/25)""")
    # añadimos los argumentos al parser
    parser.add_argument('-ex', type=str, default=None,
                        help="""Ejecuta el ejercicio indicado ('ex 1', 'ex 2', etc)
                             Si no se especifica ningún argumento, 
                             se ejecutan todos los ejercicios.""")
    parser.add_argument('-filename', type=str, default=None,
                        help="""Nombre del archivo con extension csv a cargar, si no se especifica 
                         ninguno se carga el primer archivo .csv en la carpeta indicada.""")
    parser.add_argument('-folder', type=str, default='./data',
                        help="Ruta de la carpeta donde buscar el archivo, por defecto '/data'.")

    # parseamos los argumentos del parser
    args = parser.parse_args()

    # Definimos las funciones que invocará el parser de argumentos,
    # Simplemente actuan de puente con las funciones de cada ejercicio,
    # además de garantizar la sequencia de ejecución de los ejercicios.
    def ex_1(filename=None, folder='./data'):
        """
        Ejecuta el ejercicio 1.
        :param filename: Ruta del archivo .csv a cargar.
        :param folder: Carpeta donde buscar el archivo. Por defecto './data'.
        :return: None. Esta función no retorna nada.
        """
        print_header("Ejercicio 1")
        ejercicio1(filename, folder)


    def ex_2(filename=None, folder='./data'):
        """
        Ejecuta el ejercicio 1 y 2.
        :param filename: Ruta del archivo .csv a cargar.
        :param folder: Carpeta donde buscar el archivo. Por defecto './data'.
        :return: None. Esta función no retorna nada.
        """
        print_header("Ejercicio 1")
        df: pd.DataFrame = ejercicio1(filename, folder)
        print_header("Ejercicio 2")
        ejercicio2(df)


    def ex_3(filename=None, folder='./data'):
        """
        Ejecuta el ejercicio 1, 2 y 3.
        :param filename: Ruta del archivo .csv a cargar.
        :param folder: Carpeta donde buscar el archivo. Por defecto './data'.
        :return: None. Esta función no retorna nada.
        """
        print_header("Ejercicio 1")
        df: pd.DataFrame = ejercicio1(filename, folder)
        print_header("Ejercicio 2")
        df_labaells: pd.DataFrame = ejercicio2(df)
        print_header("Ejercicio 3")
        ejercicio3(df_labaells)


    def ex_4(filename=None, folder='./data'):
        """
        Ejecuta el ejercicio 1, 2, 3 y 4.
        :param filename: Ruta del archivo .csv a cargar.
        :param folder: Carpeta donde buscar el archivo. Por defecto './data'.
        :return: None. Esta función no retorna nada.
        """
        print_header("Ejercicio 1")
        df: pd.DataFrame = ejercicio1(filename, folder)
        print_header("Ejercicio 2")
        df_labaells: pd.DataFrame = ejercicio2(df)
        print_header("Ejercicio 3")
        df_labaells = ejercicio3(df_labaells)
        print_header("Ejercicio 4")
        ejercicio4(df_labaells)


    def ex_5(filename=None, folder='./data'):
        """
        Ejecuta todos los ejercicios (1, 2, 3, 4 y 5).
        :param filename: Ruta del archivo .csv a cargar.
        :param folder: Carpeta donde buscar el archivo. Por defecto './data'.
        :return: None. Esta función no retorna nada.
        """
        print_header("Ejercicio 1")
        df: pd.DataFrame = ejercicio1(filename, folder)
        print_header("Ejercicio 2")
        df_labaells: pd.DataFrame = ejercicio2(df)
        print_header("Ejercicio 3")
        df_labaells = ejercicio3(df_labaells)
        print_header("Ejercicio 4")
        df_labaells_smoothen: pd.DataFrame = ejercicio4(df_labaells)
        print_header("Ejercicio 5")
        ejercicio5(df_labaells_smoothen)


    # Diccionario que relaciona el argumento 'ex' con la función correspondiente.
    # Utilizamos lambda para asociar la función a cada argumento.
    ejercicios: dict[str, callable] = {
        '1': lambda: ex_1(args.filename, args.folder),
        '2': lambda: ex_2(args.filename, args.folder),
        '3': lambda: ex_3(args.filename, args.folder),
        '4': lambda: ex_4(args.filename, args.folder),
        '5': lambda: ex_5(args.filename, args.folder),
        '0': lambda: ex_5(args.filename, args.folder)
    }

    # Si la ejecución contiene el argumento 'ex'
    if args.ex:
        # Obtenemos el número del ejercicio
        ejercicio = args.ex.split()[-1]
        # Si el número del ejercicio está dentro del diccionario de ejercicios
        if ejercicio in ejercicios:
            # Ejecutamos la función correspondiente al número del ejercicio
            ejercicios[ejercicio]()
        else:
            print("Error: Ejercicio no encontrado")
            sys.exit(1) # Detenemos ejecución (código 1 - error)

    # Si no se especifica el argumento 'ex'
    else:
        ex_5() # Ejecutamos el último ejercicio (por cascada ejecuta todos los demás)


if __name__ == '__main__':
    main() # Punto de entrada del programa
