@echo off
REM ============================================================
REM  Odpala caly projekt (Opcja C - bez Dockera, bez Redisa).
REM  Sprawdza TYLKO, czy istnieje srodowisko wirtualne venv.
REM  Jest venv  -> odpala 3 procesy (Flask, Worker, Beat).
REM  Brak venv  -> pokazuje instrukcje i CZEKA (pause).
REM  Uruchom: kliknij dwukrotnie ten plik.
REM ============================================================

cd /d "%~dp0"

REM --- Jedyny warunek: czy jest venv? Jak nie ma -> skok do :novenv ---
if not exist "venv\Scripts\python.exe" goto novenv

REM Sciezka do Pythona z venv.
set "PY=venv\Scripts\python.exe"

REM Utworz foldery brokera (kolejka na plikach), jesli nie istnieja.
if not exist "broker\in"        mkdir "broker\in"
if not exist "broker\out"       mkdir "broker\out"
if not exist "broker\processed" mkdir "broker\processed"
if not exist "results"          mkdir "results"

REM 1. Flask - aplikacja zyjaca nieskonczenie.
start "Flask"  "%PY%" app.py

REM 2. Celery worker - na Windows KONIECZNE --pool=solo.
start "Worker" "%PY%" -m celery -A celery_app worker --loglevel=info --pool=solo

REM 3. Celery beat - "budzik" wysylajacy zadanie wg harmonogramu.
start "Beat"   "%PY%" -m celery -A celery_app beat --loglevel=info

echo.
echo Uruchomiono 3 okna (z venv): Flask, Worker, Beat.
echo Aby wystawic na swiat, w osobnym oknie odpal: ngrok http 5000
echo.
echo To okno mozesz zamknac - tamte 3 maja dzialac dalej.
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
