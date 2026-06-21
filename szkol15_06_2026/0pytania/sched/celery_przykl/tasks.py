"""
Zadanie Celery: co 5 minut pyta aplikację "co robić" i to wykonuje.
"""
import requests
from celery_app import app


@app.task
def odpytaj_aplikacje():
    # Pytamy żyjącą aplikację Flask: "co mam robić?"
    try:
        odpowiedz = requests.get("http://localhost:5000/co-robic", timeout=5)
        polecenia = odpowiedz.json()
    except requests.RequestException as e:
        # Aplikacja nie odpowiada => łagodna degradacja, nie wywalamy workera.
        print(f"[Celery] Nie udało się odpytać aplikacji: {e}")
        return "blad_polaczenia"

    if not polecenia:
        print("[Celery] Nic do zrobienia.")
        return "brak zadań"

    for polecenie in polecenia:
        # tu realnie wykonujesz pracę: wyślij raport, przelicz, wyczyść...
        print(f"[Celery] Wykonuję polecenie: {polecenie}")

    return f"wykonano: {polecenia}"
