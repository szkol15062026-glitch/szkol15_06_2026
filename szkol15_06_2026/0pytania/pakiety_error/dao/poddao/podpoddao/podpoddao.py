import os
import sys

# Katalog nadrzedny (pakiety_error). Ten plik lezy 4 foldery glebiej:
# pakiety_error / dao / poddao / podpoddao / podpoddao.py  -> dirname() 4 razy.
KATALOG_NADRZEDNY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
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
# |           +-- __init__.py       (robi z folderu podpoddao PAKIET)
# |           +-- podpoddao.py  <-- TEN PLIK (podpodraz, podpoddwa, podpodtrzy, podpodcztery)
# |
# +-- testy/
#     +-- __init__.py
#     +-- dao_test.py           (importuje funkcje z dao/, poddao/, podpoddao/)
#
# Plik __init__.py robi z folderu podpoddao/ PAKIET. Dzieki temu z innego pliku
# mozna napisac import:  from dao.poddao.podpoddao.podpoddao import podpodraz, ...
# Kazdy folder w tej sciezce (dao, poddao, podpoddao) musi miec __init__.py,
# zeby cala droga przez kropki dzialala.
#
# ----------------------------------------------------------------------------
# CWICZENIE - sprawdz sam, do czego sluzy __init__.py:
#   1. Wejdz do folderu testy/ w terminalu:
#        cd testy
#   2. Uruchom testy i zobacz, ze import z podpoddao DZIALA:
#        python dao_test.py
#   3. Usun (lub przenies) plik dao/poddao/podpoddao/__init__.py
#   4. Uruchom ponownie:
#        python dao_test.py
#      Spodziewany blad (import z podpoddao przestaje dzialac):
#        ModuleNotFoundError: No module named 'dao.poddao.podpoddao'
#   5. Przywroc plik __init__.py - blad znika, import znowu dziala.
#
# Wniosek: bez __init__.py folder podpoddao/ przestaje byc pakietem i nie da sie
# go zaimportowac przez kropki (dao.poddao.podpoddao.podpoddao).
# ----------------------------------------------------------------------------


def podpodraz(a,b):
    return a +b

def podpoddwa(a,b):
    return a / b

def podpodtrzy(a,b):
    return a * b

def podpodcztery(a,b):
    return a - b


if __name__ == "__main__":
    # Pokaz importowania - dokladnie tak samo jak w dao.py:
    # importujemy funkcje Z INNYCH PAKIETOW (dao/ oraz poddao/) i ich uzywamy.
    #
    # Import dziala, bo:
    #   - KATALOG_NADRZEDNY (pakiety_error) jest w sys.path,
    #   - WSZYSTKIE foldery na sciezce (dao/, poddao/) maja __init__.py,
    # wiec Python potrafi przejsc cala droge przez kropki az do funkcji.
    from dao.dao import dodaj
    from dao.poddao.poddao import poddodaj

    # Funkcje z TEGO pliku (podpoddao) wolamy bezposrednio:
    print("podpodraz(2, 3) =", podpodraz(2, 3))
    print("podpodtrzy(4, 3)=", podpodtrzy(4, 3))

    # Funkcje zaimportowane z pakietow nadrzednych:
    print("dodaj(2, 3)     =", dodaj(2, 3), "(z dao.dao)")
    print("poddodaj(2, 3)  =", poddodaj(2, 3), "(z dao.poddao.poddao)")

    print("OK - import miedzy pakietami dziala.")