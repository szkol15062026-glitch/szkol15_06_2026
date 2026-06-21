# __init__.py pakietu  testy
# ============================================================================
# JAK DZIALAJA IMPORTY DZIEKI TEMU PLIKOWI:
#
# 1) Obecnosc pliku robi z folderu testy/ PAKIET. Dzieki temu dziala import
#    przez kropki, ktorego uzywa dao/dao.py w swoim bloku __main__:
#        from testy.dao_test import wypowiedz
#    Bez tego pliku byloby "No module named 'testy'".
#
# 2) Tutaj CELOWO NIC NIE IMPORTUJEMY (plik zostaje pusty oprocz komentarza).
#    Powod: testy/dao_test.py sam importuje funkcje z pakietu dao. Gdybysmy
#    tutaj zrobili "from .dao_test import ...", to KAZDY import pakietu testy
#    natychmiast uruchamialby caly modul testowy (i jego importy z dao) - a
#    tego zwykle nie chcemy. Pakiety z testami trzyma sie zazwyczaj PUSTE.
#
# Wniosek: __init__.py nie MUSI nic importowac. Czasem jego jedynym zadaniem
# jest po prostu "oznaczyc folder jako pakiet", zeby dzialaly importy do srodka.
