"""
Zadanie Celery — CZYSTY PYTHON, bez Flaska.
Pokazowka: beat co 15 sekund uruchamia to zadanie, ktore wypisuje napis.
"""
from celery_app import app


@app.task
def zadanie():
    print("[Celery] Zadanie wykonane (co 15 sekund).")
    return "ok"
