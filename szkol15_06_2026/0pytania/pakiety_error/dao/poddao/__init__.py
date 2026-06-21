# __init__.py pakietu  dao.poddao
# ============================================================================
# Wykonuje sie AUTOMATYCZNIE przy pierwszym imporcie pakietu dao.poddao
# (np. "from dao.poddao.poddao import poddodaj").
#
# JAK DZIALAJA IMPORTY DZIEKI TEMU PLIKOWI:
#
# 1) Obecnosc pliku robi z folderu poddao/ PAKIET zagniezdzony w dao/.
#    Dzieki temu dziala pelna sciezka przez kropki:
#        from dao.poddao.poddao import poddodaj
#    UWAGA: zeby ta sciezka dzialala, KAZDY folder po drodze (dao, poddao)
#    musi miec swoj __init__.py.
#
# 2) Re-eksport ponizej skraca import - zamiast:
#        from dao.poddao.poddao import poddodaj   # przez modul poddao.py
#    zadziala krocej:
#        from dao.poddao import poddodaj          # prosto z pakietu poddao
#
# Import wzgledny - kropka = "ten pakiet (poddao)":
# from .poddao import poddodaj, poddziel, podmnoz, pododejmij #<------ Dzięki temu oszczędzamy dłuższe importowanie pakietów
#
# NOTKA: powyzsza linia jest ZAKOMENTOWANA, wiec krotki import
#        "from dao.poddao import poddodaj" NA RAZIE NIE DZIALA (rzuci ImportError).
#        Zeby zaczal dzialac -> ODKOMENTUJ powyzsza linie (usun '# ' z poczatku).

# Co sie wydarzy przy "from dao.poddao import poddodaj":
#   krok 1: Python importuje pakiet dao        -> uruchamia dao/__init__.py
#   krok 2: Python importuje pakiet dao.poddao -> uruchamia TEN plik
#   krok 3: ten plik robi "from .poddao import ..." -> laduje poddao.py
#   krok 4: poddodaj jest dostepne jako dao.poddao.poddodaj i stamtad sie bierze.
