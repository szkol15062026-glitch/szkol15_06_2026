### Obiektowość ###### Obiektowość ###### Obiektowość ###### Obiektowość ###### Obiektowość ###### Obiektowość ######
########################################################################################################################
# Klasy a instancje # Klasy a instancje # Klasy a instancje # Klasy a instancje # Klasy a instancje # Klasy a instancje
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################
# Klasa a instancja

#Klasa -->
class Pies:
    pass

class Wilk:
    pass

#Instancja -->
burek = Pies()
azorek = Pies()
wilkolak = Pies()
burek.imie = 'Burek'

print(burek.imie)
# print(azorek.imie)
print(f"Czy to ten sam pies:{'Tak' if burek is azorek else 'Nie'}")
print(f"Czy to jest ta sama klasa {'Tak' if type(burek) == type(azorek) else 'Nie'}")
print(f"Czy to jest ta sama klasa {'Tak' if type(burek) == type(wilkolak) else 'Nie'}")
print(f'Czy Burek należy do klasy Wilk {'Tak' if isinstance(burek, Wilk) else 'Nie'}')
print(f'Czy Burek należy do klasy Pies {'Tak' if isinstance(burek, Pies) else 'Nie'}')
print(type(burek))

# 1. Zdefiniuj pustą klasę Ksiazka,
# utwórz dwie instancje i sprawdź, 
# że to różne obiekty tej samej klasy.

# 1.
class Ksiazka:
    pass
powiesc = Ksiazka()
horror = Ksiazka()
print(f'Czy powiesc należy do klasy Ksiazka {'Tak' if isinstance(powiesc, Ksiazka) else 'Nie'}')
print(f'Czy horror należy do klasy Ksiazka {'Tak' if isinstance(horror, Ksiazka) else 'Nie'}')

########################################################################################################################
# Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty # Atrybuty
#-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##--
########################################################################################################################
# Klasa a instancja

# – Atrybuty Klasy --> atrybut domyślny, atrybut instancji, atrybut kompozycji
# atrybut instancji
class Drzewo:
    pass

sosna = Drzewo()
kasztan = Drzewo()
sosna.wiek = 70
print(sosna.wiek) #--> należy tylko do przypisanej instacji
# print(kasztan.wiek) --> atrybut instancji

# atrybut domyślny
class Narzedzia:
    ilosc = 4

pila = Narzedzia()
miarka = Narzedzia()
print(pila.ilosc,miarka.ilosc)
pila.ilosc = 6
print(pila.ilosc,miarka.ilosc)

# atrybut innej klasy --> kompozycja

class Silnik: 
    pass
class Auto: 
    pass

silnik = Silnik()
silnik.moc = 132

auto = Auto()
auto.silnik = silnik       # OBIEKT jako atrybut innego obiektu
print(auto.silnik.moc)     # 132   (dwie kropki: auto -> silnik -> moc)

# 2.1. Zadanie spróbuj wyświetlić sobie co pokaze każda instancja dla atrybutu produkty

# 2.1.
class Koszyk:
    produkty = []        # atrybut klasy

k1 = Koszyk()
k2 = Koszyk()
k1.produkty.append("chleb")
print(k1.produkty)
print(k2.produkty)

# 2.2 Klasa Pies z atrybutem klasy gatunek.
# Utwórz dwie instancje, potem przypisz gatunek 
# tylko jednej i pokaż, że druga się nie zmienia.

# 2.2
# przykład 1
"""
class Pies():
    gatunek = ""
terrier = Pies()
pudel = Pies()
terrier.gatunek = "maly"
print(terrier.gatunek)
print(pudel.gatunek)
"""

# przykład 2
"""
class Pies:
    gatunek = "wilkowaty"

burek = Pies()
azor = Pies()
burek.gatunek = "owczarek"
print(burek.gatunek)
print(azor.gatunek)
"""

# przykład 3
"""
class Pies:
    def __init__(self, gatunek):
        self.gatunek = gatunek

pikus = Pies("chihuahua")
atryb = Pies()
# print(atryb.gatunek) --> brak atrybutu domyślnego
print(pikus.gatunek)
"""

# 2.3 Utwórz obiekt Silnik, nadaj mu moc,
# a potem przypnij go jako atrybut obiektu 
# Samochod. Odczytaj moc z poziomu samochodu. 

# 2.3
class Silnik: 
    pass
class Samochod: 
    pass

silnik = Silnik()
silnik.moc = 132

auto = Samochod()
auto.silnik = silnik       # OBIEKT jako atrybut innego obiektu
print(auto.silnik.moc) 

# Przykład z metodą __init__
"""
class Silnik:
    def __init__(self, moc):
        self.moc = moc

rolce_royce = Silnik(1000)
print(rolce_royce.moc)
"""

########################################################################################################################
# Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # Metody # M
#-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##--
########################################################################################################################
# Metody --> .count() 

class Konto:
    saldo = 1000
    def wyplac(self, kwota): # pytanie --> czym jest nasz self
        if kwota > self.saldo:
            print("Brak środków!"); return
        self.saldo -= kwota
        print(f"Z konta upłynęło {kwota}")

insta1 = Konto()
insta1.wyplac(200)
insta1.wyplac(400)
insta1.wyplac(900)

insta2 = Konto()
insta2.wyplac(200)
insta2.wyplac(400)


# 3. Klasa Prostokat z metodami pole() i obwod(). Atrybuty a, b ustaw na obiekcie ręcznie
"""
class Prostokąt:
        class Prostokąt:
        a = 10
        b = 20
        def pole(self):
            return self.a * self.b
        def obwod(self):
         return 2 * (self.a + self.b)
        
prostokat = Prostokąt()
prostokat.a =30
prostokat.b=60

print(prostokat.pole())
"""

"""
class Prostokat():
    a=1
    b=1
    
    def pole(self, a, b):
        wynik = a*b
        return wynik
    
    def obwod(self,a, b):
        wynik= 2*a+2*b 
        return wynik
    
obiekt = Prostokat()
print(obiekt.pole(a=4,b=5))
"""

# Pułapka atrybuty domyślne musimy bez self. jako przekazywane argumenty 

########################################################################################################################
# Konstruktor __init__ # Konstruktor __init__ # Konstruktor __init__ # Konstruktor __init__ # Konstruktor __init__ # Kon
#-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##-->4<--##--
########################################################################################################################
#  Konstruktor __init__

class Ksiazka:
    def __init__(self,strony,typ, rok_wydania):
        self.strony = strony
        self.typ = typ
        self.rok_wydania = rok_wydania
    def __str__(self):
        return f'Książka ma stron: {self.strony}, typ: {self.typ}, rok_wydania: {self.rok_wydania}'

horror = Ksiazka(200,'ciezka oprawa',1854)
print(horror) #--> <__main__.Ksiazka object at 0x0000023676EF8C20>

# 4.1 Stwórz klasę Zwierze() w której będzie gatunek, imie, wiek, za pomocą metody __init__ oraz dodać metodę __str__

# 4.1
class Zwierze():
    def __init__(self, gatunek, imie, wiek):
        self.gatunek = gatunek
        self.imie = imie
        self.wiek = wiek
    def __str__(self):
        return f"{self.imie} jest {self.wiek} lat i jest to: {self.gatunek}"
    
zebra = Zwierze('koniowata','Marysia',7)
print(zebra)

class Tygrys():
    def __init__(self, imie, wiek, cena, umaszczenie='Brak',zoo='Brak'):
        self.imie = imie
        self.wiek = wiek
        if cena < 0:
            raise ValueError("cena nie może być ujemne!")   # WALIDACJA
        self.cena = cena
        self.umaszczenie = umaszczenie
        self.zoo = zoo
    
# tyg= Tygrys('Maniek',20,-300)
# print(tyg.umaszczenie,tyg.zoo)

# 4.2 Klasa Ksiazka(tytul, autor). Utwórz DWIE różne książki z tej samej klasy i wypisz ich dane
# 4.3 Klasa uzytkownik Utwórz użytkownika BEZ podania roli (ma wyjść user) oraz administratora z rolą admin --> atrybut domyślny
# 4.4 Klasa Student(imie, wiek): konstruktor ma odrzucać wiek ujemny, a pole oceny
# ma startować jako pusta lista (nie pochodzi z argumentu).

# 4.2
class Ksiazka():
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    def __str__(self):
        return f"{self.tytul} by {self.autor}"  

duna = Ksiazka("Duna", "Frank Herbert")
print(duna)
sapiens = Ksiazka("Sapiens", "Yuval Noah Harari")
print(sapiens)

# 4.3
class User():
    def __init__(self, rola='user'):
        self.rola = rola

uzytkownik = User()
print(uzytkownik.rola)
admin = User('admin')
print(admin.rola)

# 4.4
class Student():
    a = 20
    def __init__(self, wiek):
        if wiek < 0:
            raise ValueError("Wiek nie może być ujemny")
        self.wiek = wiek
        self.oceny = []

student1 = Student(18)
print(student1.wiek)
student1.oceny.append(6)
print(student1.oceny)

student2 = Student(20)
print(student2.oceny)

########################################################################################################################
# Dziedziczenie # Dziedziczenie # Dziedziczenie # Dziedziczenie # Dziedziczenie # Dziedziczenie # Dziedziczenie # Dziedz
#-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##-->5<--##--
########################################################################################################################
# Dziedziczenia klas 

class Zwierze:      # klasa BAZOWA (rodzic)
    def __init__(self, imie):
        self.imie = imie
    def dzwiek(self):
        return '...'
    def opis(self):
        return self.imie
    
class Pies(Zwierze):
    def __init__(self, imie, umaszczenie):
        super().__init__(imie)
        self.umaszczenie = umaszczenie
    def dzwiek(self):
        return 'Hau'
    def opis(self):
        return super().opis() + f'->pies o umaszczeniu {self.umaszczenie}'
    
class Kot(Zwierze):
    def __init__(self,imie,umaszczenie):
        super().__init__(imie)
        self.umaszczenie = umaszczenie
    def dzwiek(self):
        return 'Miau'
    def opis(self):
        return super().opis() + f'->kot o umaszczeniu {self.umaszczenie}'

burek = Pies('Burek','czarne')
zwierz = Zwierze('rafal')
kot = Kot('Eris','biale')

print(zwierz.opis())
# print(burek.imie,burek.umaszczenie)
print(burek.opis())
print(kot.opis())

for i in [Zwierze('zwierze'),Kot('kot','zielone'),Pies('pies','szare')]: # Polimorfizm
    print(i.dzwiek())
    
### super().__init__

# 5.1 Napisz klasę bazową Pojazd z polem marka i metodą opis() (np.
#  zwraca „Pojazd marki Toyota"). Potem utwórz klasę potomną 
# Samochod,która dziedziczy po Pojazd, 
# dodaje własne pole liczba_drzwi i rozszerza 
# (nie zastępuje!) metodę opis() o liczbę drzwi — korzystając z 
# super(). 
# Na koniec stwórz Samochod("Toyota", 5) i wypisz jego opis.

# 5.2 Klasa bazowa Pracownik(imie, pensja) z metodami przedstaw() i
# wyplata(). Klasa Menedzer dziedziczy po Pracownik, 
# nie zmienia przedstaw() ani konstruktora, ale całkowicie 
# nadpisuje wyplata() tak, by doliczała premię 1000

# 5.1
"""
class Pojazd:
    def __init__(self, marka):
        self.marka = marka
    def opis(self):
        return f"Pojazd marki {self.marka}"
    
class Samochod(Pojazd):
    def __init__(self,marka, liczba_drzwi):
        super().__init__(marka) ## --> zabrakło
        self.liczba_drzwi = liczba_drzwi
    def opis(self):
        return super().opis() + f'liczba drzwi {self.liczba_drzwi}'
toyota= Samochod('Toyota',5)
print(toyota.opis())
print(toyota.liczba_drzwi)
"""

# 5.2
"""
class Pracownik:
    def __init__(self, imie, pensja):
        self.imie= imie
        self.pensja= pensja
    def przedstaw(self):
        return self.imie
    def wyplata(self):
        return self.pensja
    
class Menager(Pracownik):
    def __init__(self, imie, pensja):
        super().__init__(imie, pensja)
    def przedstaw(self):
        return super().przedstaw()
    def wyplata(self):
        return self.pensja+1000
    
menager = Menager('Damian',10000)

print(menager.wyplata())
print(menager.przedstaw())
"""

#  Dziedziczenie po wielu klasach

class Plywak:
    def ruch(self): return "płynę"
    def plyn(self): return "umiem pływać"

class Lotnik:
    def ruch(self): return "lecę"
    def lec(self): return "umiem latać"

class Kaczka(Plywak,Lotnik):
    # def ruch(self): return 'lece i pływam'
    pass

kaczka = Kaczka() #--> MRO (Method Resolution Order)

print(kaczka.lec())
print(kaczka.plyn())
print(kaczka.ruch())

print([c.__name__ for c in Kaczka.__mro__])  # --> pokazuje kolejność dziedziczenia MRO


# 5.3 Zrób dwie klasy A i B, każda z metodą kto() zwracającą odpowiednio "A" i "B". Następnie utwórz C, która dziedziczy po obu (class C(A, B)).
# Zgadnij, zanim odpalisz: czy C().kto() zwróci "A", czy "B"? Sprawdź wynik i wypisz C.__mro__, żeby zobaczyć, dlaczego tak

class A:
    def kto(self):
        return "A"
    
class B:
    def kto(self):
        return "B"
    
class C(B,A):
    pass

c = C()
print(c.kto())
print([c.__name__ for c in C.__mro__])

# Ciekawy przypadek
class A:
    def robie(self): print("A")

class B(A):
    def robie(self): print("B"); super().robie()

class C(A):
    def robie(self): print("C"); super().robie()

class D(B, C):
    def robie(self): print("D"); super().robie()

# Klasa A to rodzic
# Klasa B dziedziczy po A
# Klasa C dziedziczy po A
# Klasa D dziedziczy po B i C 

print('*'*30)
d_klase = D()
print(d_klase.robie())

# Metody i klasy abstrakcyjne

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod #-> dekorator
    def pole(self):                   # metoda ABSTRAKCYJNA — sama deklaracja, bez ciała
        ...
    def przedstaw(self):              # klasa abstrakcyjna MOŻE mieć też zwykłe metody
        return f"Pole = {self.pole()}"

# Figura()  ->  TypeError: Can't instantiate abstract class Figura with abstract method pole
class Prostokat(Figura):              # klasa konkretna — implementuje kontrakt
    def __init__(self, a, b):
        self.a, self.b = a, b
    def pole(self):                   # MUSI zaimplementować pole(), inaczej sama jest abstrakcyjna
        return self.a * self.b
    
class Kolo(Figura):
    def __init__(self, r):
        self.r=r
    def pole(self):
        return 3.14*int(self.r)**2
    
class Kwadrat(Figura):
    def __init__(self, a):
        self.a= a
    def pole(self):                   
        return self.a * self.a
    
# p = Prostokat(3, 4)
# print(p.pole())  
# print(p.przedstaw()) 

# for i in [Zwierze('zwierze'),Kot('kot','zielone'),Pies('pies','szare')]: # Polimorfizm
#     print(i.dzwiek())


# 5.4 Korzystając z klasy abstrakcyjnej Figura (tej z teorii powyżej), dopisz dwie własne figury: Kolo i Kwadrat, każda z własnym pole().
# Wrzuć kilka figur do jednej listy i policz sumę ich pól jedną pętlą (polimorfizm).


# print("*"*50)
# for i in [Kolo('4'),Kwadrat(6)]:
#     print(i.pole())

# 5.4
"""
print("*"*50)
for i in [Kolo('4'),Kwadrat(6)]:
    print(i.pole())

p = Prostokat(3, 4)
print(p.pole()) 
print(p.przedstaw()) 

kw = Kwadrat(5)
print(kw.pole())
print(kw.przedstaw())

k = Kolo(2)
print(k.pole())
print(k.przedstaw())

lista = [p, kw, k]
suma_pol = 0
for figura in lista:
    suma_pol += figura.pole()
print(suma_pol)

"""

########################################################################################################################
# Metody magiczne # Metody magiczne # Metody magiczne # Metody magiczne # Metody magiczne # Metody magiczne # Metody mag
#-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##-->6<--##--
########################################################################################################################

# Metody magiczne
# - __init__ --> szablonem
# – __str__  --> string zwraca bardziej ludzki opis zamiast niezrozumialego dla nas <clas-->
# – __getitem__ --> pozwala na pobieraniu obiektu za pomocą indexowania
# – __setitem__ --> 

class Figura:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'Bok jeden to: {self.a}, bok drugi to {self.b}'

class Playlista:
      def __init__(self):
          self.utwory = ["Bohemian Rhapsody", "Imagine", "Hey Jude", "Yesterday"]
      def __getitem__(self, i): # --> __getitem__ p[0]
          # uruchamia się, gdy ktoś napisze playlista[i]
          return self.utwory[i]
      def __setitem__(self,i,wartosc):
          return self.utwory[i] == wartosc
          
p = Playlista()
print(p[1])

#   6.1 Napisz klasę Alfabet:
#   * W __init__ zrób atrybut self.litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".
#   * Dodaj __getitem__, które dla alfabet[i] zwróci literę o numerze i.

#   6.2 Napisz klasę Sklep:
#   * W __init__: self.produkty = ["chleb", "mleko", "masło", "ser"].
#   * Dodaj __getitem__, żeby sklep[i] zwracało i-ty produkt.


#   6.1
class Alfabet:
    def __init__(self):
        self.litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __getitem__(self, i):
        return self.litery[i]

alf = Alfabet()
print(alf[17])

#   6.2
class Sklep:
    def __init__(self):
        self.produkty= ["chleb", "mleko", "masło", "ser"]
    def __getitem__(self, i):
        return self.produkty[i]
    
prod = Sklep()
print(prod[2])

class Playlista:
      def __init__(self):
          self.utwory = ["Bohemian Rhapsody", "Imagine", "Hey Jude", "Yesterday"]

      def __getitem__(self, i): # --> __getitem__ p[0]
          # uruchamia się, gdy ktoś napisze playlista[i]
          return self.utwory[i]
      def __setitem__(self,i,wartosc):
          self.utwory[i] = wartosc
          
p = Playlista()

p[1] = 'abrakdar'

print(p.utwory)

#   6.3 Napisz klasę Magazyn:
#   * W __init__: self.stany = {"jabłka": 10, "gruszki": 5} (słownik produkt → ilość).
#   * __getitem__, żeby m["jabłka"] zwracało ilość.
#   * __setitem__, żeby m["jabłka"] = 20 ustawiało nową ilość (a m["banany"] = 7 dodawało nowy
#   produkt).

# slownik['klucz'] = wartosc

print("*"*30)

class Magazyn():
    def __init__(self):
        self.stany = {"Jabłka": 10, "Gruszki": 20, "Banany": 30}

    def __getitem__(self, key): #--> zwraca na, (2,5) --> 0 , 1
        return self.stany[key]

    def __setitem__(self, key, value): 
        self.stany[key] = value

mag = Magazyn()
print(mag["Jabłka"])
mag["Jabłka"] = 5
print(mag["Jabłka"])

########################################################################################################################
# Hermetyzacja # Hermetyzacja # Hermetyzacja # Hermetyzacja # Hermetyzacja # Hermetyzacja # Hermetyzacja # Hermetyzacja
#-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##-->7<--##--
########################################################################################################################
# Hermetyzacja

class Przyklad:
    def __init__(self):
        self.publiczna = 'publiczna'
        self._chroniona = 'chroniona'
        self.__prywatna = 'prywatna'

prywat = Przyklad()

print(prywat.publiczna)
print(prywat._chroniona)
print(prywat._Przyklad__prywatna)

# @property i setter
class Konto:
    def __init__(self):
        self.__saldo = 1000          # ukryte (name mangling)
    @property # --> @ -> dekoratory
    def saldo(self):                 # GETTER — czyta się BEZ nawiasów: konto.saldo
        return self.__saldo
    @saldo.setter
    def saldo(self, w):              # SETTER — pisze się BEZ nawiasów: konto.saldo = ...
        if w < 0:
            raise ValueError("Saldo nie może być ujemne!")
        self.__saldo = w

konto = Konto()
print(konto.saldo)
konto.saldo = 500 
print(konto.saldo)
# konto.saldo = -500 
print(konto.saldo)

# 7.1 Napisz klasę Temperatura, która trzyma temperaturę w ukrytym polu __celsjusz.
# Wystaw je na zewnątrz jako celsjusz przez @property: getter zwraca wartość, 
# a setter odrzuca temperatury poniżej −273,15°C (zero bezwzględne). 
# Dodatkowo zrób property fahrenheit tylko do odczytu (bez settera), 
# które wylicza stopnie Fahrenheita z aktualnego __celsjusz. --> F = C * 9/5 + 32

class Temperatura:
    def __init__(self,c=0):
        self.__celsjusz = c
    @property
    def celsjusz(self):
        return self.__celsjusz
    @celsjusz.setter
    def celsjusz(self,w):
        if w < -273.15:
            raise ValueError("Temperatura nie moze być niższa niż -273.15 c!")
        self.__celsjusz = w
    @property
    def fahnren(self):
        return self.__celsjusz * 9/5 + 32
    
temp = Temperatura()

print(temp.celsjusz)
temp.celsjusz = 50
print(temp.celsjusz)
print(temp.fahnren)

########################################################################################################################
# Dokumentowanie klas # Dokumentowanie klas # Dokumentowanie klas # Dokumentowanie klas # Dokumentowanie klas # Dokument
#-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##-->8<--##--
########################################################################################################################

class Konto:
    """Konto zawierające saldo zabezpieczone hermentyzacją ... ble ble ble """

    def wplac(self):
        """ Metoda klasy Konto odpowiedzialna za wplacanie pieniedzy i zmianę salda użytkownika"""
        pass

kon = Konto()
print(Konto.__doc__)  
print(Konto.wplac.__doc__)  