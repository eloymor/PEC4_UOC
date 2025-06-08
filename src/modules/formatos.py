"""
Módulo con funciones auxiliares para formatos.
"""

def print_separador(n: int = 150) -> None:
    """
    Imprime un separador de líneas.
    :param n: longitud del separador, por defecto 150.
    :return: None
    """

    print('-' * n)



def print_header(s: str) -> None:
    """
    Imprime un encabezado.
    :param s: texto del encabezado.
    :return: None
    """

    l: int = len(s)
    print_separador(l)
    print(f"\n{s.upper()}\n")
    print_separador(l)
