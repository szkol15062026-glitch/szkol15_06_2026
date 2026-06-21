"""
Test pokazujacy POPRAWNY import funkcji z pakietu dao.

Problem: dao/ i testy/ to dwa osobne foldery (rodzenstwo). Gdy uruchamiasz
ten plik bezposrednio (python testy/dao_test.py), Python widzi tylko folder
testy/ - nie znajdzie pakietu dao. Dlatego musimy zrobić sztuczkę

Jak to wyglada w prawdziwych projektach:
W realnych projektach zwykle NIE robi sie recznie tej sztuczki z sys.path.
Zamiast tego buduje sie jeden wspolny pakiet/projekt z folderem nadrzednym,
ktory spina wszystkie podfoldery (dao/, testy/ itd.) w jedna calosc. To
"polaczenie" tworzy sie raz na poziomie projektu, np.:

  - dodajac plik __init__.py w folderach, zeby staly sie pakietami,
  - instalujac projekt jako pakiet (pip install -e . z plikiem
    pyproject.toml / setup.py),
  - albo uruchamiajac testy narzedziem typu pytest z katalogu glownego.

Dzieki temu Python od poczatku zna sciezki miedzy modulami i import
"from dao.dao import ..." dziala bez bledow o nieznalezionym module/relacji
miedzy folderami - bez wpisywania sys.path.insert w kazdym pliku osobno.

Ponizszy fragment z sys.path to wersja "na piechote" - pokazuje recznie to,
co w projekcie zalatwia wlasnie ten wspolny folder nadrzedny i konfiguracja
pakietu.
"""
import os
import sys

# Katalog nadrzedny (pakiety_error) - tam, gdzie leza foldery dao/ i testy/.
KATALOG_NADRZEDNY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KATALOG_NADRZEDNY)

# Struktura projektu, w ktorym teraz jestesmy:
#
# pakiety_error/                <-- KATALOG_NADRZEDNY (dodany do sys.path)
# |
# +-- dao/
# |   +-- __init__.py
# |   +-- dao.py                (dodaj, dziel, mnoz, odejmij)
# |   +-- poddao/
# |       +-- __init__.py
# |       +-- poddao.py         (poddodaj, poddziel, podmnoz, pododejmij)
# |       +-- podpoddao/
# |           +-- __init__.py
# |           +-- podpoddao.py  (podpodraz, podpoddwa, podpodtrzy, podpodcztery)
# |
# +-- testy/
#     +-- __init__.py
#     +-- dao_test.py           <-- TEN PLIK (tutaj jestesmy)

# Teraz import dziala niezaleznie od tego, skad uruchomisz plik.
from dao.dao import dodaj, dziel, mnoz, odejmij
# import dao.dao # W celu użycia funkcji np dodaj trzeba --> dao.dao.dodaj(2, 3)
# import dao.dao as ddao # w celu użycia funkcji np. dodaj trzeba --> ddao.dodaj(2,3)
# from dao.dao import dodaj # import tylko jednej funkcji, która nas interesuje

from dao.poddao.poddao import poddodaj, poddziel, podmnoz, pododejmij

from dao.poddao.podpoddao.podpoddao import podpodraz, podpoddwa, podpodtrzy, podpodcztery

def wypowiedz():
    print('Tutaj jest sprawdzenie, czy wywoła')

def sprawdz_dao():
    # Przypadek importu 'from dao.dao import dodaj, dziel, mnoz, odejmij'
    print("dodaj(2, 3)   =", dodaj(2, 3))
    print("odejmij(5, 2) =", odejmij(5, 2))
    print("mnoz(4, 3)    =", mnoz(4, 3))
    print("dziel(10, 2)  =", dziel(10, 2))

    # Przypadek importu 'import dao.dao'
    # print("dodaj(2, 3)   =", dao.dao.dodaj(2, 3))
    # print("dodaj(2, 3)   =", dao.dao.odejmij(2, 3))
    # print("dodaj(2, 3)   =", dao.dao.mnoz(2, 3))
    # print("dziel(10, 2)  =", dao.dao.dziel(10, 2))

    # Przypadek importu 'import dao.dao as ddao'
    # print("dodaj(2, 3)   =", ddao.dodaj(2, 3))
    # print("odejmij(5, 2) =", ddao.odejmij(5, 2))
    # print("mnoz(4, 3)    =", ddao.mnoz(4, 3))
    # print("dziel(10, 2)  =", ddao.dziel(10, 2))

    # Przypadek importu 'from dao.dao import dodaj'
    # print("dziel(10, 2)  =", dodaj(10, 2))


    print("OK - import z pakietu dao dziala, wartosci pobrane.")

def sprawdz_poddao():
    print("poddodaj(2, 3)   =", poddodaj(2, 3))
    print("pododejmij(5, 2) =", pododejmij(5, 2))
    print("podmnoz(4, 3)    =", podmnoz(4, 3))
    print("poddziel(10, 2)  =", poddziel(10, 2))

    print("OK - import z pakietu poddao dziala, wartosci pobrane.")

def sprawdz_podpoddao():
    print("podpodraz(2, 3)    =", podpodraz(2, 3))
    print("podpoddwa(5, 2)    =", podpoddwa(5, 2))
    print("podpodtrzy(4, 3)   =", podpodtrzy(4, 3))
    print("podpodcztery(10, 2)=", podpodcztery(10, 2))

    print("OK - import z pakietu podpoddao dziala, wartosci pobrane.")



if __name__ == "__main__":
    # Pobieramy wartosci z funkcji pakietu dao.
    sprawdz_dao()
    sprawdz_poddao()
    sprawdz_podpoddao()