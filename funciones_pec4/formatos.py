def print_separador(n: int = 150):
    print('-' * n)
    pass


def print_header(s: str):
    l: int = len(s)
    print_separador(l)
    print(f"\n{s.upper()}\n")
    print_separador(l)
    pass
