import os
import sys

# Katalog nadrzedny (pakiety_error). Ten plik lezy 3 foldery glebiej:
# pakiety_error / dao / poddao / poddao.py  -> dlatego dirname() 3 razy.
KATALOG_NADRZEDNY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, KATALOG_NADRZEDNY)

# Struktura projektu, w ktorym teraz jestesmy:
#
# pakiety_error/                <-- KATALOG_NADRZEDNY (dodany do sys.path)
# |
# +-- dao/
# |   +-- __init__.py
# |   +-- dao.py                (dodaj, dziel, mnoz, odejmij)
# |   +-- poddao/
# |       +-- __init__.py       (robi z folderu poddao PAKIET)
# |       +-- poddao.py         <-- TEN PLIK (poddodaj, poddziel, podmnoz, pododejmij)
# |       +-- podpoddao/
# |           +-- __init__.py
# |           +-- podpoddao.py  (podpodraz, podpoddwa, podpodtrzy, podpodcztery)
# |
# +-- testy/
#     +-- __init__.py
#     +-- dao_test.py           (importuje funkcje z dao/, poddao/, podpoddao/)
#
# Plik __init__.py robi z folderu poddao/ PAKIET. Dzieki temu z innego pliku
# mozna napisac import:  from dao.poddao.poddao import poddodaj, ...
# Bez __init__.py taki import (przez kropki) rzucalby blad o braku pakietu.
#
# ----------------------------------------------------------------------------
# CWICZENIE - sprawdz sam, do czego sluzy __init__.py:
#   1. Wejdz do folderu testy/ w terminalu:
#        cd testy
#   2. Uruchom testy i zobacz, ze import z poddao DZIALA:
#        python dao_test.py
#   3. Usun (lub przenies) plik dao/poddao/__init__.py
#   4. Uruchom ponownie:
#        python dao_test.py
#      Spodziewany blad (import z poddao przestaje dzialac):
#        ModuleNotFoundError: No module named 'dao.poddao'
#   5. Przywroc plik __init__.py - blad znika, import znowu dziala.
#
# Wniosek: bez __init__.py folder poddao/ przestaje byc pakietem i nie da sie
# go zaimportowac przez kropki (dao.poddao.poddao).
# ----------------------------------------------------------------------------


def poddodaj(a,b):
    return a +b

def poddziel(a,b):
    return a / b

def podmnoz(a,b):
    return a * b

def pododejmij(a,b):
    return a - b


if __name__ == "__main__":
    # Pokaz importowania - dokladnie tak samo jak w dao.py:
    # importujemy funkcje Z INNEGO PAKIETU (dao/) i jej uzywamy.
    #
    # Import dziala, bo:
    #   - KATALOG_NADRZEDNY (pakiety_error) jest w sys.path,
    #   - foldery dao/ i poddao/ maja __init__.py (sa pakietami),
    # wiec Python potrafi przejsc sciezke przez kropki: dao.dao -> funkcja dodaj.
    from dao.dao import dodaj

    # Funkcje z TEGO pliku (poddao) wolamy bezposrednio:
    print("poddodaj(2, 3) =", poddodaj(2, 3))
    print("podmnoz(4, 3)  =", podmnoz(4, 3))

    # Funkcja zaimportowana z pakietu dao:
    print("dodaj(2, 3)    =", dodaj(2, 3), "(zaimportowane z dao.dao)")

    print("OK - import miedzy pakietami dziala.")