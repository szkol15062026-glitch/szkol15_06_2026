# 3. Ćwiczenia (lambda x: operacja(x), lista) dla większego zrozumienia o co chodzi z lambdą.

"""
lambda --> sposób na napisanie małej funkcji w jednej linni bez koniecznosci nadawania nazwy
--> skrócony def
"""

def dodaj(a,b):
    return a+b

# Zapis takiej funkcji za pomocą lambda będzie w jednej linijce

dodaj = lambda a,b: a+b

"""
zwrócenie za pomocą printa zwróci nam, że to jest funkcja --> <function <lambda> at....
lambde zawsze zapisujemy w jednej linijce. Zapisz poniższy wywali nam błąd:


f = lambda a,b:
    return a+b
    
##### lambda argumenty : działanie #####
Najczęstszy przypadek używania lambdy --> sortowanie
"""

osoby = [("Anna", 30), ("Piotr", 25), ("Ewa", 40)]
posortowane = sorted(osoby, key=lambda o: o[1])
#--> bierze element jako argument i robi sortowanie po drugim elemencie krotki
print(posortowane)

"""
lambda jest wykorzystywana przy funkjach takich jak filter, map, max, sorted,min
"""

slowa = ["kot", "parasol", "dom"]

print(max(slowa, key=lambda s: len(s))) # --> najdłuższe słowo

liczby = [1,2,3,4,5,6]

print(list(filter(lambda x: x % 2 == 0, liczby))) # --> tylko parzyste przy pomocy modulo
"""
modulo to jest zwrot z dzielenia. Jak to działa?
Dzieli liczbę przez dwa i sprawdza, czy wartość reszty równa się 0
Pojawia się zero to parzysta, nie to nieparzysta  
Różne typy modulo
x % 2 == 0 --> parzyste
x % 2 != 0 --> nieparzyste
x % 3 == 0 --> podzielne przez 3 --> x % 5 == 0 --> podzielne przez 5
x % 10 == 5 --> kończy się na 5
"""

print(list(map(lambda x: x ** 2, liczby))) # --> nowa lista z kwadratami z oryginału

"""
!!!!  Pułapka lambdy

  funkcje = []
  for i in range(3):
      funkcje.append(lambda: i)

  # spodziewamy się: 0, 1, 2
  print(funkcje[0]())   # --> 2  !!!
  print(funkcje[1]())   # --> 2  !!!
  print(funkcje[2]())   # --> 2  !!!
  
  lambda czyta wartość dopiero w chwili wywołania
"""


################################################################
"""
Przykłady uzycia lambdy przy pomocy funkcji filter()
"""

slowa = ["Kot", "pies", "", "Słoń", "ul", "Anna", "ekran", "Ada"]

print(list(filter(lambda s: s != "", slowa))) #--> str nie jest pusty
print(list(filter(lambda s: len(s) > 3, slowa))) #--> dłuższy niż 3 znaki
print(list(filter(lambda s: s[:1].isupper(), slowa))) #--> zaczyna się z dużej litery
print(list(filter(lambda s: "a" in s.lower(), slowa))) # --> zawiera literę 'a' dużą jak i małą w słowie
print(list(filter(lambda s: s.lower() == s.lower()[::-1] and s, slowa))) # --> palindromy kajak od tyłu to kajak


osoby = [
      {"imie": "Anna", "wiek": 30, "miasto": "Kraków"},
      {"imie": "Piotr", "wiek": 17, "miasto": "Gdańsk"},
      {"imie": "Ewa", "wiek": 45, "miasto": "Kraków"},
  ]

print(list(filter(lambda o: o["wiek"] >= 18, osoby))) #--> pełnoletni tylko
print(list(filter(lambda o: o["miasto"] == "Kraków", osoby))) #-->tylko krakowianie
# dwa warunki w jednym
print(list(filter(lambda o: o["wiek"] >= 18 and o["miasto"] == "Kraków", osoby)))

"""
Przykłady uzycia lambdy przy pomocy funkcji map()
filter decyduje, czy zostawić element z listy, map decyduje, czy zmienic 
"""

slowa = ["robocop", "Pies", "  ul  ", "Anna",'Geralt']

print(list(map(lambda s: s.upper(), slowa))) #--> daj mi wszystko z wielkimi literami
print(list(map(lambda s: s.strip(), slowa))) #--> usuwanie białych znaków(spacji)
# lstrip() z lewej strony tylko rstrip tylko z prawej. strip z obu
print(list(map(lambda s: len(s), slowa))) #--> zwróć mi długość każdego słowa
print(list(map(lambda s: s[0], slowa))) #--> pierwsza litera słowa

teksty = ["10", "25", "3", "99"]
# napisy --> liczby
print(list(map(lambda s: int(s), teksty))


"""
Przykłady z użycia lambdy przy pomocy sorted
"""

slowa = ["banan", "Ala", "kiwi", "ab", "Cytryna"]

print(sorted(slowa, key=lambda s: s.lower())) #--> alfabetycznie nie patrzac na wielkosc liter
print(sorted(slowa, key=lambda s: len(s))) #--> według dlugości słowa

osoby = [("Anna", 30), ("Piotr", 25), ("Ewa", 40), ("Adam", 25)]

print(sorted(osoby, key=lambda o: o[1])) #--> według drugiego elementu krotki
print(sorted(osoby, key=lambda o: o[0])) #--> według pierwszego elementu krotki
print(sorted(osoby, key=lambda o: o[1], reverse=True))#--> według drugiego elementu krotki w drugą stronę


produkty = [
      {"nazwa": "laptop", "cena": 3500, "ilosc": 2},
      {"nazwa": "myszka", "cena": 80,   "ilosc": 10},
      {"nazwa": "monitor","cena": 900,  "ilosc": 2},
  ]

print(sorted(produkty, key=lambda p: p["cena"]))
#--> według ceny reverse=True po przecinku za p["cena"] jak chcemy odwrotną kolejność
print(sorted(produkty, key=lambda p: p["cena"] * p["ilosc"]))
#--> według wartości poszczególnego produktu na stanie(hurtem)
print(sorted(produkty, key=lambda p: (p["ilosc"], p["cena"])))
#--> według ilosci, ale jak taka sama to wtedy wedlug ceny

"""
Można też według min max 
"""
print(max(produkty, key=lambda p: p["cena"])) #--> też wedlug ceny
print(min(slowa, key=lambda s: len(s))) #--> najkrótsze słowo

"""
lambda jest najszybszym sposobem jeśli chcemy coś posortować, więc króluje przy sortowaniu
"""