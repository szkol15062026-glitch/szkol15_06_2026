"""
Przykłady dla closure (funkcje)
Normalnie po zakończeniu działania funkcji jej zmiennie znikają. Closure to wyjątek - funkcja zabiera je ze sobą
i pamięta na później


def zewnetrzna(x):
    def wewnetrzna():
        print(x)
    return wewnetrzna

f = zewnetrzna(10)
f()

***Zmienna przypisana do f zostaje zapamiętana
"""

"""
Zad1 
Napisz funkcję (closure) potega(n), która zwraca pot liczby n 
"""
# ....

"""
Zad2 
Napisz funkcję (closure)) rabat(procent), która zwraca funkcje liczącą cene 
po rabacie
"""
# ...

"""
Zad3
Napisz funkcję (closure) srednia_biezaca() zwracającą średnią ze wszystkich dotąd podanych.
(closure) --> trzyma DWIE zmienne: suma i licznik -> nonlocal
"""
# ...

"""
Zad4
Napisz funkcje (closure) zbieracz(), która dodaje element do ukrytej listy i zwraca jej aktualny
stan. Sprawdź bez korzystania z nonlocal.
"""
# ...

"""
Zad5
Napisz funkcję (closure) najwiekszy() zapamiętująca największą dotąd podaną liczbe i ją zwraca
Przykładowo wpisujemy 5 i jako, ze nie daliśmy wcześniej żadnej wartości najwyższą zwróci jako 5
Następnie po wpisaniu kolejnej np. 3 nadal zwróci 5, bo nie jest większa, ale jak damy 7 to naszą 
5 zamieni na 7
"""

"""
Zad6
Napisz funkcję (closure) liczb_z_pamięcia(), która liczy kwadrat liczby, ale pamięta wyniki w słowniku
dzięki czemu nie liczy drugi raz wyniku dla tej samej wprowadzonej wartości (ręcznie zrobiony prosty cache)
"""

"""
Zad7
Napisz funkcję (closure) licznik_prob(limi), która symuluje próby logowania. Każde wywołanie zużywa jedną próbę
Po przekroczeniu określonego limitu zwraca komunikat o przekroczeniu limitu zamiast liczyć dalej.
"""


"""
Zad8
Napisz funkcję (closure) konto(saldo), która zwróci dwie funkcje wspoldzielace ten sam stan (saldo),
czyli funkcję wyplac(kwota) oraz wyplac(kwota). Wypłata większa niż saldo ma zwrócić komunikat o braku środków
i nie zmianiać salda. 
Warunki:
!! jeden closure -> dwie funkcje na tej samej zmiennej --> nonlocal. Spróbuj wypłacić większą kwotę niż ma saldo oraz dodać
"""




