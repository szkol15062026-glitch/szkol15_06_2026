@echo off
REM ============================================================
REM  Celery BEZ Flaska - czysty Python + Celery (Opcja C).
REM  Bez Dockera, bez Redisa: broker na plikach.
REM  Sprawdza TYLKO, czy istnieje srodowisko wirtualne venv.
REM  Jest venv  -> odpala 2 procesy (Worker, Beat).
REM  Brak venv  -> pokazuje instrukcje i CZEKA (pause).
REM  Uruchom: kliknij dwukrotnie ten plik.
REM ============================================================

cd /d "%~dp0"

REM --- Jedyny warunek: czy jest venv? Jak nie ma -> skok do :novenv ---
if not exist "venv\Scripts\python.exe" goto novenv

REM Sciezka do Pythona z venv.
set "PY=venv\Scripts\python.exe"

REM Utworz foldery brokera (kolejka na plikach), jesli nie istnieja.
REM Kolejka to JEDEN folder (in i out wskazuja to samo miejsce).
if not exist "broker\queue"     mkdir "broker\queue"
if not exist "broker\processed" mkdir "broker\processed"
if not exist "results"          mkdir "results"

REM 1. Celery worker - na Windows KONIECZNE --pool=solo.
start "Worker" "%PY%" -m celery -A celery_app worker --loglevel=info --pool=solo

REM 2. Celery beat - "budzik" wysylajacy zadanie wg harmonogramu.
start "Beat"   "%PY%" -m celery -A celery_app beat --loglevel=info

echo.
echo Uruchomiono 2 okna (z venv): Worker, Beat.
echo Co 15 s w oknie Worker zobaczysz: [Celery] Zadanie wykonane.
echo.
echo To okno mozesz zamknac - tamte 2 maja dzialac dalej.
pause
exit /b 0

:novenv
echo ============================================================
echo  Brak srodowiska wirtualnego "venv".
echo.
echo  Zrob to raz:
echo    1. Zainstaluj Pythona: https://www.python.org/downloads/
echo       (zaznacz "Add python.exe to PATH").
echo    2. W folderze projektu utworz venv i zainstaluj pakiety:
echo         python -m venv venv
echo         venv\Scripts\python.exe -m pip install -r requirements.txt
echo    3. Uruchom start.bat ponownie.
echo ============================================================
echo.
pause
exit /b 1
