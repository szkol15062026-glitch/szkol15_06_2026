# __init__.py pakietu  dao
# ============================================================================
# Ten plik wykonuje sie AUTOMATYCZNIE przy PIERWSZYM imporcie pakietu dao
# (np. gdy ktos napisze "from dao.dao import dodaj" albo "import dao").
#
# JAK DZIALAJA IMPORTY DZIEKI TEMU PLIKOWI - dwa osobne efekty:
#
# 1) SAMA OBECNOSC pliku __init__.py robi z folderu dao/ PAKIET.
#    To wystarczy, zeby dzialaly importy "przez kropki" z zewnatrz:
#        from dao.dao import dodaj          # siegamy do modulu dao/dao.py
#        import dao.poddao.poddao
#    Gdyby tego pliku nie bylo - powyzsze rzucaloby blad "No module named 'dao'".
#
# 2) Jesli COS TUTAJ ZAIMPORTUJEMY, to "podnosimy" nazwy na poziom pakietu
#    (re-eksport). Dzieki ponizszej linii zadziala KROTSZY import:
#        from dao import dodaj              # prosto z pakietu, bez ".dao"
#    a nie tylko dluzszy:
#        from dao.dao import dodaj          # przez modul dao.py
#
# Uzywamy importu WZGLEDNEGO - kropka oznacza "ten pakiet (dao)":
#   from .dao  -> czytaj jako "z modulu dao.py lezacego w tym pakiecie"
# from .dao import dodaj, dziel, mnoz, odejmij  #<------ Dzięki temu oszczędzamy dłuższe importowanie pakietów
#
# NOTKA: powyzsza linia jest ZAKOMENTOWANA, wiec krotki import
#        "from dao import dodaj" NA RAZIE NIE DZIALA (rzuci ImportError).
#        Zeby zaczal dzialac -> ODKOMENTUJ powyzsza linie (usun '# ' z poczatku).

# Co dokladnie sie wydarzy przy "from dao import dodaj":
#   krok 1: Python importuje pakiet dao -> uruchamia TEN plik (__init__.py)
#   krok 2: ten plik robi "from .dao import ..." -> laduje modul dao/dao.py
#   krok 3: nazwa dodaj jest teraz dostepna jako  dao.dodaj
#   krok 4: "from dao import dodaj" po prostu ja stamtad bierze.
