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
# |   +-- __init__.py           (robi z folderu PAKIET)
# |   +-- dao.py                <-- TEN PLIK (dodaj, dziel, mnoz, odejmij)
# |   +-- poddao/
# |       +-- __init__.py
# |       +-- poddao.py         (poddodaj, poddziel, podmnoz, pododejmij)
# |       +-- podpoddao/
# |           +-- __init__.py
# |           +-- podpoddao.py  (podpodraz, podpoddwa, podpodtrzy, podpodcztery)
# |
# +-- testy/
#     +-- __init__.py
#     +-- dao_test.py           (importuje funkcje z dao/)
#
# Pliki __init__.py sa wazne: dzieki nim 'dao' to PAKIET (folder), a nie
# zwykly modul (plik dao.py). Bez nich, przy uruchomieniu 'python dao.py'
# z wnetrza folderu dao/, nazwa 'dao' wskazywalaby na PLIK dao.py i import
# 'from dao.dao import ...' rzucalby blad: "'dao' is not a package".
#
# ----------------------------------------------------------------------------
# CWICZENIE - sprawdz sam, do czego sluzy __init__.py:
#   1. Wejdz do folderu dao/ w terminalu:
#        cd dao
#   2. Uruchom plik bezposrednio i zobacz, ze DZIALA (foldery sa pakietami):
#        python dao.py
#   3. Usun (lub przenies) pliki __init__.py ze wszystkich folderow:
#        - dao/__init__.py
#        - dao/poddao/__init__.py
#        - dao/poddao/podpoddao/__init__.py
#        - testy/__init__.py
#   4. Uruchom ponownie:
#        python dao.py
#      Spodziewany blad:
#        ModuleNotFoundError: No module named 'dao.dao'; 'dao' is not a package
#   5. Przywroc pliki __init__.py - blad znika, import znowu dziala.
#
# Wniosek: bez __init__.py folder dao/ przestaje byc pakietem, a Python
# bierze plik dao.py jako modul 'dao' -> 'dao.dao' nie istnieje.
# ----------------------------------------------------------------------------

# UWAGA - import cykliczny (circular import):
# Ponizszy import NIE moze stac tutaj, na gorze pliku. Powod:
#   - dao.py importuje 'wypowiedz' z testy/dao_test.py,
#   - a testy/dao_test.py importuje funkcje z dao/dao.py.
# Pliki importuja sie NAWZAJEM -> Python nie zdazy zaladowac jednego,
# zanim zacznie potrzebowac drugiego -> ImportError (partially initialized module).
#
# Rozwiazanie: import przenosimy do bloku __main__ na dole pliku - wtedy
# wykona sie TYLKO gdy uruchamiamy dao.py bezposrednio, a nie gdy dao.py
# jest importowany przez dao_test.py. To przerywa petle.


def dodaj(a,b):
    return a +b

def dziel(a,b):
    return a / b

def mnoz(a,b):
    return a * b

def odejmij(a,b):
    return a - b



if __name__ == "__main__":

    # Import tutaj (a nie na gorze pliku) - patrz uwaga o imporcie cyklicznym.
    from testy.dao_test import wypowiedz

    print(dodaj(5,6))
    print(dziel(10,5))
    print(mnoz(3,8))
    print(odejmij(20,7))

    wypowiedz()