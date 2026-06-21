"""
Aplikacja Flask — żyje nieskończenie (jak Django).
Trzyma prostą "kolejkę poleceń". Celery co 5 minut odpyta endpoint /co-robic.

host="0.0.0.0" => aplikacja słucha na wszystkich interfejsach,
dzięki czemu da się ją wystawić na świat (np. przez ngrok).
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Kolejka poleceń trzymana w pamięci. W realnym projekcie => baza danych.
polecenia_do_zrobienia = []


@app.route("/")
def index():
    return (
        "<h2>Aplikacja działa.</h2>"
        "Dodaj polecenie: <code>/dodaj?co=wyslij_raport</code><br>"
        f"Aktualnie w kolejce: {polecenia_do_zrobienia}"
    )


@app.route("/dodaj")
def dodaj():
    # np. http://localhost:5000/dodaj?co=wyslij_raport
    co = request.args.get("co", "nic")
    polecenia_do_zrobienia.append(co)
    return f"Dodano: {co}. W kolejce: {polecenia_do_zrobienia}"


@app.route("/co-robic")
def co_robic():
    # Celery odpyta ten endpoint co 5 minut.
    # Zwracamy polecenia i czyścimy kolejkę (zostały "pobrane").
    global polecenia_do_zrobienia
    do_wykonania = polecenia_do_zrobienia
    polecenia_do_zrobienia = []
    return jsonify(do_wykonania)


if __name__ == "__main__":
    # debug=False => to nie jest tryb deweloperski wystawiany na świat z debuggerem.
    app.run(host="0.0.0.0", port=5000, debug=False)
