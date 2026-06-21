Celery bez Flaska — czysty Python + Celery

Pokazowka: beat co 15 sekund uruchamia zadanie, ktore wypisuje napis.
Broker dziala na plikach — bez Dockera, bez Redisa.

## Pliki

`celery_app.py` | Instancja Celery + broker na plikach + harmonogram

`tasks.py` | Zadanie, ktore co 15 s wypisuje napis

`start.bat` | Odpala Worker + Beat (2 okna)

`requirements.txt` | `celery` + `pywin32` (Windows)

## 1. Instalacja (raz)

```powershell
python -m venv venv
venv\Scripts\python.exe -m 
pip install -r requirements.txt
```

## 2. Uruchomienie

Kliknij dwukrotnie **`start.bat`** — otworzy 2 okna: Worker i Beat.
Co 15 sekund w oknie **Worker** zobaczysz `[Celery] Zadanie wykonane (co 15 sekund).`
