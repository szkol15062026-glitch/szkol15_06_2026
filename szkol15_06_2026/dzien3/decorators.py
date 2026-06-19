########################################################################################################################
# Dekarotory # Dekarotory # Dekarotory # Dekarotory # Dekarotory # Dekarotory # Dekarotory # Dekarotory # Dekarotory # D
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################

#przekazywanie funkcji do środka innej funkcji
#zwracanie funkcji

def loguj(funkcja):
    def wrapper():
        print(f"Witaj, opdalasz funkcję {funkcja.__name__}")
        wynik = funkcja()
        print(f"Witaj, Kończysz działanie funkcji {funkcja.__name__}")
        return wynik
    return wrapper

@loguj
def witaj():
    return 'abra'

witaj()

# Napisz dekorator, który wyprintuje naszą funkcję witaj()

def printer(funkcja):
    def output():
        print(funkcja())
        return funkcja()
    return output

@printer
def witaj():
    return 'abracadabra'

witaj()

print(witaj.__name__)

# @functools.wraps(funkcja) 

import functools # --> import biblioteki

def printer2(funkcja):
    @functools.wraps(funkcja)  # --> wbudowany dekorator pozwalający na zwrot oryginalnych wartości funkcji po opkaowaniu dekoratorem
    def output():
        print(funkcja())
        return funkcja()
    return output

@printer2
def witaj2():
    return 'abracadabra'

witaj2()

print(witaj2.__name__)


def printer3(funkcja):
    @functools.wraps(funkcja)  
    def output(*args,**kwargs):
        print(funkcja(*args,**kwargs))
        wynik = funkcja(*args,**kwargs)
        return wynik
    return output

@printer3
def dodaj(a,b):
    return a +b

dodaj(2,5)

# Napisali dekorator, który dla funkcji odpowiedzialnej za mnożenie dwóch cyfr zwróci nam jego dwukrotność
# Upewnijcie się, że oryginalna funkcja nie będzie nadpisana przez funkcję dekoratora


# przykład 1 
"""
def dekor(funkcja):
    @functools.wraps(funkcja)
    def output(*args,**kwargs):
        solution = funkcja(*args,**kwargs)
        print(funkcja(*args,**kwargs)*2)
        return solution * 2
    return output

@dekor
def mnoz(a,b):
    return a*b
print(mnoz(2,3))
print(mnoz.__name__)
"""

# przykład 2
"""
import functools

def double(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
          return funkcja(*args, **kwargs) * 2
    return wrapper

@double
def multi(a,b):
    return a * b

print(multi(3,4))
"""


def otul(funkcja):
    print(f'Pierwsze wywołanie {funkcja.__name__}')
    def wrapper(*args,**kwargs):
        wynik = funkcja(*args,**kwargs)
        return wynik
    return wrapper


@otul
def hello():
    print('Hello,Hello')

hello()
hello()
hello()


# Napisać dekorator, który będzie korzystał z printowania zewnętrznego i za pomocą jego wyświetli nam Przywitanie
# Dekorator użyli nie tylko na jednej funkcji, ale na kilku
# Nastepnie wywołajcie funkcje kilka razy

def dekorator(funkcja):
    print("##Witaj w załodze##"*5)
    ## Dodać w tym segmencie logi -> Jakie funkcje są opakowane jakim dekoratorem?
    def wrapper(*args,**kwargs):
        wynik = funkcja(*args,**kwargs)
        return wynik
    return wrapper

@dekorator
def przywitanie():
    print('hejka')
@dekorator
def testing():
    print('test')
    
przywitanie()
przywitanie()
testing()
testing()

# Trzykrotne opakowanie funkcji # opakowywanie przez więcej funkcji dekoratory

import functools

def powtorz(ile):                         # 1) argument dekoratora
    def dekorator(funkcja):               # 2) funkcja
        @functools.wraps(funkcja)
        def wrapper(*a, **k):             # 3) opakowanie
            return [funkcja(*a, **k) for _ in range(ile)]
        return wrapper
    return dekorator

@powtorz(2)
def przywitaj(imie):
    return f"Cześć {imie}"


print(przywitaj("Ala")) 



# ***
# Napisz dekorator licz_wywolania, który zlicza, ile razy wywołano dekorowaną funkcję. 
# Licznik ma być dostępny z zewnątrz jako atrybut funkcji — funkcja.licznik. --> wrapper.atrybut <--
# Sprawdź: po trzech wywołaniach funkcja.licznik powinno wynosić 3.

import functools

def licz_wywolania(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        wrapper.atrybut += 1
        print(f"Funkcja {funkcja.__name__} została wywołana {wrapper.atrybut} razy")
        return funkcja(*args, **kwargs)
    wrapper.atrybut = 0
    return wrapper

@licz_wywolania
def hello():
    print("Hello World!")

hello()
hello()
hello()

print(hello.atrybut)


# Mieliśmy coś takiego cache

"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2) 
"""

# @property
# def hello():
#     print("Hello World!")

# hello()

# Django --> @login_required, @group_required --> adminem
# Flask --> @app_route --> generuje ścieżke na którą można się dostać 

# funkcja --> która odpowiedzialna jest za coś 
# dekorator --> wymagane jest, mile widziane, nie ingerencja w logikę funkcji 