def dodaj(a,b):
    return a+b

def odejmij(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def szescian(a):
    return a**3

def dziel(a,b):
    if a or b == 0:
        raise ValueError("nie dzielimy przez zero")
    return a / b