# 1. rozróżnienie między funkcja a methodą .sort() sorted().

# Najprościej

# --> Metoda jest najprościej funkcja, która należy do obiektu i wywołuje się ją przez kropkę obiekt.nazwa()
# Przykładowo operacje na stringach str -->
#  "tekst".upper() -> tylko duże litery
#  "tekst".lower() -> tylko małe litery
#  "tekst".capitalize() -> Pierwsza litera z dużej

# --> Funkcja jest samodzielna - wywołuje się po samej nazwie więc: --> nazwa()
# Przykładowe funkcje wbudowane w pythona
# len([2,4,5]) --> długość listy --> len('tekst') --> długość stringa
# max([2,4,5]) --> największa cyfra --> max('pamiętliwy') --> alfabetycznie ostatni znak
# min([2,4,5]) --> najmniejsza cyfra --> max('asertywny') --> alfabetycznie pierwszy znak

#2. Czy range() jest generatorem? -->

# range sam w sobie nie jest generatorem. Co prawda oszczędza pamięć, ale można iterować przez niego wiele raz,
# czego nie można powiedzieć o generatorze. Można też po nim indexować. Generator też się zużywa po przejściu.

# Generator
gen = (x for x in range(5))
print(f'Pierwsze wywołanie generatora: {list(gen)}') # --> [0, 1, 2, 3, 4]
print(f'Drugie wywołanie generatora:   {list(gen)}')    # --> []

# Range
ran = range(5)
print(f'Pierwsze wywołanie range: {list(ran)}')     # --> [0, 1, 2, 3, 4]
print(f'Drugie wywołanie range:   {list(ran)}')     # --> [0, 1, 2, 3, 4]

# 3. Czy @property używane w klasach można wykorzystywać na zewnętrznych funkcjach

# @property to tak zwany deskryptor - działa tylko wyłącznie, gdy jest atrybutem klasy oraz jak się siega do niego przez obiekt.x
# przykład napisanego własnego @property
class moje_property:
    def __init__(self, getter, setter=None):
        self.getter = getter
        self.setter_fn = setter

    def __get__(self, instancja, klasa=None):
        if instancja is None:
            return self
        return self.getter(instancja)

    def __set__(self, instancja, wartosc):
        if self.setter_fn is None:
            raise AttributeError("brak settera — pole tylko do odczytu")
        self.setter_fn(instancja, wartosc)

    def setter(self, fn):
        # zwraca NOWY deskryptor z tym samym getterem + nowym setterem
        return moje_property(self.getter, fn)


class Kolo:
    def __init__(self, r):
        self._r = r

    @moje_property
    def promien(self):
        return self._r

    @promien.setter
    def promien(self, wartosc):
        if wartosc <= 0:
            raise ValueError("promień musi być dodatni")
        self._r = wartosc