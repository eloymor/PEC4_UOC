"""
Módulo con funciones auxiliares para fechas.
"""

import datetime

def to_year_fraction(date: datetime.datetime | datetime.date) -> float:
    """
    A partir de una fecha, devuelve el año decimal.

    :param date: datetime.datetime o datetime.date, fecha a convertir
    :return: float, fecha convertida a año decimal
    """

    # https://stackoverflow.com/questions/6451655/how-to-convert-python-datetime-dates-to-decimal-float-years
    start: int = datetime.date(date.year, 1, 1).toordinal()
    year_length: int = datetime.date(date.year + 1, 1, 1).toordinal() - start

    return date.year + float(date.toordinal() - start) / year_length
