# __init__.py pakietu  dao.poddao.podpoddao
# ============================================================================
# Wykonuje sie AUTOMATYCZNIE przy pierwszym imporcie pakietu
# dao.poddao.podpoddao (np. "from dao.poddao.podpoddao.podpoddao import podpodraz").
#
# JAK DZIALAJA IMPORTY DZIEKI TEMU PLIKOWI:
#
# 1) Obecnosc pliku robi z folderu podpoddao/ PAKIET - najglebszy w lancuchu.
#    Pelna sciezka importu dziala TYLKO gdy KAZDY folder po drodze ma __init__.py:
#        dao/__init__.py  +  poddao/__init__.py  +  podpoddao/__init__.py
#    Brak ktoregokolwiek = blad "No module named ..." na tym wlasnie poziomie.
#
# 2) Re-eksport ponizej skraca import - zamiast:
#        from dao.poddao.podpoddao.podpoddao import podpodraz  # przez modul
#    zadziala krocej:
#        from dao.poddao.podpoddao import podpodraz            # prosto z pakietu
#
# Import wzgledny - kropka = "ten pakiet (podpoddao)":
# from .podpoddao import podpodraz, podpoddwa, podpodtrzy, podpodcztery #<------ Dzięki temu oszczędzamy dłuższe importowanie pakietów
#
# NOTKA: powyzsza linia jest ZAKOMENTOWANA, wiec krotki import
#        "from dao.poddao.podpoddao import podpodraz" NA RAZIE NIE DZIALA (ImportError).
#        Zeby zaczal dzialac -> ODKOMENTUJ powyzsza linie (usun '# ' z poczatku).

# Co sie wydarzy przy "from dao.poddao.podpoddao import podpodraz":
#   krok 1: import pakietu dao                 -> dao/__init__.py
#   krok 2: import pakietu dao.poddao          -> poddao/__init__.py
#   krok 3: import pakietu dao.poddao.podpoddao-> TEN plik
#   krok 4: ten plik robi "from .podpoddao import ..." -> laduje podpoddao.py
#   krok 5: podpodraz dostepne jako dao.poddao.podpoddao.podpodraz.
