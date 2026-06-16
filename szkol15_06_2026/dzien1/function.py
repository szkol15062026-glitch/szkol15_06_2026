## Funkcje #### Funkcje #### Funkcje #### Funkcje #### Funkcje #### Funkcje #### Funkcje #### Funkcje #### Funkcje ####

########################################################################################################################
# *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *args ## *
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##--
########################################################################################################################

def sumuj_dane(a,b):
    return a + b 

print(sumuj_dane(4,8))

# print(sumuj_dane(3,8,5,4))

def sum_dane(*args):
    return sum(args)

# *args  jest to opakowanie czyli 3,8,5,4 -> (3,8,5,4) --> tuple
# args jest to już (3,8,5,4) 

print(sum_dane(3,8,5,4))
# args, ze podaje się je jako wartości same -> str,bool,int

print(sum_dane(3,8,5,4,8,4,6,3,2))
print(sum_dane(*[3,8,5,4])) #--> listy nie wolno bez rozpakowanie 

# Ważna kolejność w funkcji najpierw, które wpisujemy, potem *args, potem **kwargs def sum(a,b,c,*args,**kwargs)

# 1. Napisz iloczyn(*args) (iloczyn podanych liczb)
# oraz srednia(*oceny), która dla braku argumentów zwraca 0 
# (nie dzieli przez zero). Wywołaj srednia na liście [10,20,30] przez rozpakowanie.

# 1.
def iloczyn(*args): # --> (2,6,5)
    wynik = 1
    for i in args:
        wynik = wynik * i
    return f'Zwracamy iloczyn wszystkich liczb {wynik}'

# --> ... *= ...
def srednia(*oceny):
    if oceny:
        return int(sum(oceny) / len(oceny))
    else:
        return 0

print(iloczyn(2,6,3,6,4,3,6,2,7))
print(srednia(*[10,20,30]))

########################################################################################################################
# **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs ## **kwargs #
#-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##--
########################################################################################################################

def slownik(**kwargs):
    print(kwargs)
    # return -> zwraca coś nie ma --> None

slownik(imie='Przemek',wiek=26,telefon='765957456')

def slownik(**kwargs):
    for key,value in kwargs.items():
        print(f"Klucz:{key} --> wartość:{value}")

slownik(imie='Przemek',wiek=26,telefon='765957456')

# args wrzcuanych argumentów od razu a kwargs do danych klucz-wartość

# a,b,f, *args, **kwargs  
# *args, **kwargs
# a,b,f, **kwargs

# 2. Napisz opisz(**kwargs) wypisującą każdą parę jako klucz: wartość.
# Mając def przedstaw(imie, wiek, miasto) i słownik dane, wywołaj przedstaw, 
# rozpakowując słownik podwójną gwiazdką.

# 2.
dictionary = {'imie':'Tytus', 'wiek':12, 'miasto':'Warszawa'}

def słownik(**kwargs):
    for k,v in kwargs.items():
        print(f"Klucz: {k}, wartość: {v}")

słownik(**dictionary)

slownik_dane=dict(imie='Ola', wiek=66, miasto='Waszawa')
def przedstaw(**kwargs):
    for key,vaule in kwargs.items():
        print(f"{key}: {vaule}")

przedstaw(**(slownik_dane))

########################################################################################################################
# Funkcja wewnątrz funkcji ## Funkcja wewnątrz funkcji ## Funkcja wewnątrz funkcji ## Funkcja wewnątrz funkcji ## Funkcj
#-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##--
########################################################################################################################

def przedstaw():
    def wypisz():
        print('Witaj jestem')
    return wypisz

przedstawiam = przedstaw() # --> to plecak, closure

# przedstawiam()
# przedstawiam()
przedstawiam()

def mnoz(x):
    def przez(n):
        return x * n
    return przez

razy3 = mnoz(3) 
razy5 = mnoz(5)

print(razy3(10)) #-- print(mnoz(3)(10))

razy3 = mnoz(3)

# zapis funkcji z nawiasami przez()
# zapis funkcji bez nawiasów przez 

# 3. opakujcie funkcje w funkcji która będzie odpowiedzialna za sumowanie dwóch elementów
# opakujcie w closure(plecak) -> pierwszą wartość

# 3.
def sumowanie(x):
    def dodac(n):
        return x+n
    return dodac

print(sumowanie(5)(10))
piatka= sumowanie(5)
print(piatka(10))

def licznik():
    wynik = 0
    def licz():
        nonlocal wynik
        wynik += 1
        return wynik  
    return licz

liczaj = licznik()
liczaj2 = licznik()

print(liczaj())
print(liczaj())
print(liczaj())
print(liczaj2())

# 4. Napisz funkcje w funkcji która przyjmie kilka argumentów *args i zrobi z nich sumę

# 4.
def suma_argumentow(*args):
    wynik = 0
    def policz():
        nonlocal wynik
        for a in args:
            wynik += a
        return wynik
    return policz

opakowanie = suma_argumentow(2,6,4,8,4)
# print(opakowanie) #--> <function suma_argumentow.<locals>.policz at 0x000001B6E6F801A0>
print(opakowanie())

########################################################################################################################
# Funkcja jako argument funkcji # Funkcja jako argument funkcji # Funkcja jako argument funkcji # Funkcja jako argument
#-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##--
########################################################################################################################

# def .... policz() --> wywołaniem
# def .... policz --> to jest jako argument

def dodaj(a,b):
    return a + b

def mnoz(a,b):
    return a * b

def zastosuj(funkcja,a,b):
    return funkcja(a,b)

print(f"Zastosowanie dla dodaj: {zastosuj(dodaj,5,9)}")
print(f"Zastosowanie dla mnoz: {zastosuj(mnoz,5,9)}")

def sprawdz_dlugosc(funkcja, wartosc):
    return funkcja(wartosc)

print(f"długość to:  {sprawdz_dlugosc(len,'python')}")

# max min len count
# 5. napisali funkcje która sotsuje powyższe metody na jakaś listę

# 5.
list_example = [20,10,4,5]
def statistic(func, obj):
    return func(obj)
print(f"Lenght of list is: {statistic(len, list_example)}")
print(f"The largest number is: {statistic(max, list_example)}")
print(f"Minimal value is: {statistic(min, list_example)}")

########################################################################################################################
# Funkcja zwracająca funkcje ## Funkcja zwracająca funkcje ## Funkcja zwracająca funkcje ## Funkcja zwracająca funkcje #
#-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##--
########################################################################################################################
def potega(n):
    def wewn(x):
        return x ** n
    return wewn

kwadrat = potega(2); potega(4)(2)

def wiekszy_niz(prog):
    def sprawdz(x): return x > prog
    return sprawdz
list(filter(wiekszy_niz(17), wieki))


def z_logiem(funkcja):
    def opakowana(*args, **kwargs):
        print(f"-> {funkcja.__name__}")
        wynik = funkcja(*args, **kwargs)
        print(f"<- {wynik}")
        return wynik
    return opakowana

########################################################################################################################
# Rekurencja # Rekurencja # Rekurencja # Rekurencja # Rekurencja # Rekurencja # Rekurencja # Rekurencja # Rekurencja # R
#-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##--
########################################################################################################################

def odliczanie(n):
    if n == 0:                 # warunek bazowy -> koniec
        print("start!")
        return
    print(n)                   # 3, 2, 1...
    odliczanie(n - 1)          # krok: coraz mniejsze n, az dojdzie do 0
# odliczanie(8)

def silnia(n):
    if n <= 1:                 # warunek bazowy
        return 1
    return n * silnia(n - 1)   # krok: n razy silnia mniejszej liczby

print(silnia(5))

def dodawanie(n):
    if n == 100:
        print('start!')
        return
    print(n)
    dodawanie(n+1)

dodawanie(10)

# Funkcja odwołuje się do samej siebie *pierwszy warunek rekurencji
# Funkcja jest blokada --> warunek blokujący ciągłą pracę

# 6. Napisać taką funkcję --> rekurencję która będzie odnosić sie do samej siebie

# 6.
def suma_liczb(n):
    if n == 1:
        return 1
    return n + suma_liczb(n - 1)

print(suma_liczb(4))

########################################################################################################################
# Optymalizacja funkcji przez cache # Optymalizacja funkcji przez cache # Optymalizacja funkcji przez cache # Optymaliza
#-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##--
########################################################################################################################

from functools import lru_cache
import time

# DOWÓD szybkości: naiwnie vs @lru_cache (ta sama pamięć, automatyczna)
def fib_naiwny(n):
    return n if n < 2 else fib_naiwny(n-1) + fib_naiwny(n-2)

@lru_cache(maxsize=None)
def fib_cache(n):
    return n if n < 2 else fib_cache(n-1) + fib_cache(n-2)

t = time.perf_counter(); w1 = fib_naiwny(35); czas_n = time.perf_counter() - t
t = time.perf_counter(); w2 = fib_cache(35);  czas_c = time.perf_counter() - t

print(f"1) naiwny:  fib(35) = {w1}  w {czas_n:.4f}s")
print(f"   z cache: fib(35) = {w2}  w {czas_c:.6f}s")
print(f"   przyspieszenie: ~{czas_n / czas_c:.0f}x szybciej")

# DOWÓD, że każda wartość policzona jest RAZ
print("2)", fib_cache.cache_info())   # CacheInfo(hits=34, misses=36, ...) — 36 = n od 0 do 35

#hits jest dużo większe niż misses oznacza, że cache
# misses jest dużo więcej niż hits oznacza, że cache się w tym nie opłaca 

# [[],[]]