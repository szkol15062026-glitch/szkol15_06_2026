import kalkulator
import pytest
import narzedia as n
# from pakiety import modul

def test_dodaj():
    assert kalkulator.dodaj(6,4) == 10

# wywołanie --> testów --> pytest

# Dodaniu do kalkulatora kilku obliczeń, def z 1 argumentem zwracającym
# sześcian //////// def z 2 argumentami z wynikiem mnożenia 

def test_dodaj():
    assert kalkulator.dodaj(6,4) == 10
    assert kalkulator.mnozenie(2,2) == 4
    assert kalkulator.szescian(2) == 8

# pytest                          # auto-wykrywanie plików test_*.py
# pytest -v                       # szczegółowo (nazwy testów + wynik)
# pytest test_kalkulator.py::test_dodaj   # jeden konkretny test
# pytest -k "dodaj"               # wszystkie z "dodaj" w nazwie ( -k "not podziel" )
# pytest -x                       # zatrzymaj po pierwszym błędzie
# pytest -s                       # pokaż print() (domyślnie schowane)
# pytest --lf                     # tylko ostatnio padłe (last failed)

# --> @pytest.mark.parametrize

@pytest.mark.parametrize("n,oczekiwany", [(2, 8), (3, 27), (0, 0), (-2, -8)])
def test_szescian(n, oczekiwany):
    assert kalkulator.szescian(n) == oczekiwany

# dla mnożenia, dzielenia .....

## Mockowanie 

from unittest.mock import patch
import serwis

@patch("serwis.pobierz_kurs")              # patchuj TAM, gdzie UŻYWANE!
def test_cena_pln(mock_kurs):
    mock_kurs.return_value = 4.0
    assert serwis.cena_pln(100, "EUR") == 400.0
    mock_kurs.assert_called_once_with("EUR")

@pytest.mark.podstawowe
def test_sumuj():
    assert n.sumuj(5, 3) == 8

@pytest.mark.szczegolowe
def test_dajCyfryMin():
    tab = n.dajCyfry()
    assert min(tab) == 1

@pytest.mark.szczegolowe
def test_dajCyfryMax():
    tab = n.dajCyfry()
    assert max(tab) == 10

@pytest.mark.podstawowe
def test_dajCyfryLen():
    tab = n.dajCyfry()
    assert len(tab) == 10


## pytest -m podstawowe