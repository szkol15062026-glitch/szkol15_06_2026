# Przykłady realnego zastosowania dla rozpakowania.
# Czemu mamy z tego korzystać, a nie skorzystać z indexowania obiekt[0]

"""
Czytelność kodu
Powiedzmy, że mamy krotkę, która do nas trafia do jakiejś funkcji i wracamy do tej
funkcji po jakimś dopiero czasie
"""

p = (54,23) # --> nieznany przez nas punkt przekazywany do funkcji jako jeden argument
pol = p[0] * p[1] # --> return p[0] * p[1] Nie wiemy czym jest p[1], p[0] na pierwszy rzut oka

bok_a, bok_b = p
pol = bok_a * bok_b # --> bardziej czytelne w porównaniu do indexowania

# Pułapka --> złe działanie kodu
p = (54,23,30)
pol = p[0] * p[1]
"""
Zwraca nam dalej kod i wykonuje działanie, nie wiemy o tym, że dane są źle przekazywane
przez nie wiemy też o błędzie.
"""
# a, b = p
"""
Rozpakowanie pokaże nam, że coś jest nie tak
-------------------------------------------------
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 7, in <module>
ValueError: too many values to unpack (expected 2)
-------------------------------------------------
"""

"""
Krótszy zapis jeśli chcemy wziąć przykładowo pierwszy, środek i ostatni element
Znowu trafia do nas lista, gdzie nie mamy pojęcia ile jest w niej elementów.
Może to być lista_a, albo lista_b na dole
"""
lista_a = [2,4,0]
lista_b = [6,2,7,4,2,4,7,3,4]

pierwszy, *srodek, ostatni = lista_a
print(pierwszy, srodek, ostatni)
pierwszy, *srodek, ostatni = lista_b
print(pierwszy, srodek, ostatni)

"""
W przypadku indexowania jest to dużo wolniejszy proces oraz dużo łatwiej popełnić błąd 
"""

"""
Rozpakowania, więc najlepiej korzystamy, kiedy wyciągami kilka wartości w jednym momencie. Dzięki temu
nazywamy je i pilnujemy, czy jest ich odpowiednia ilość. Przy wyciąganiu jednego elementu lepiej sobie
poradzi index[0]
"""

dane = ("Anna", (1990, 5, 12)) # --> w przypadku zagnieżdzenia w danych, -->lista,krotka,słownik
imie, (rok, miesiac, dzien) = dane
print(imie, rok)

"""
Przy użyciu indexowania może się mieszać, szczególnie jak jest duzo elementów
dane[1][0], dane[1][2] .......
"""