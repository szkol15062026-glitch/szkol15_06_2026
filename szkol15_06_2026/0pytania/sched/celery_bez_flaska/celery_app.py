"""
Instancja Celery — CZYSTY PYTHON, bez Flaska, bez Dockera, bez Redisa.
Broker dziala NA PLIKACH (filesystem://) — kolejka to zwykle foldery.

Foldery broker/in, broker/out, broker/processed oraz results
tworzy automatycznie start.bat.
"""
from celery import Celery

app = Celery("przyklad")

# Kaz Celery zaladowac plik z zadaniami, zeby je zarejestrowal.
app.conf.imports = ("tasks",)

# --- Broker oparty o system plikow (bez zadnego serwera) ---
# WAZNE: data_folder_in i data_folder_out MUSZA wskazywac TEN SAM folder.
# Beat (producent) zapisuje wiadomosc do data_folder_out, a Worker (konsument)
# czyta z data_folder_in. Gdyby to byly rozne foldery, Worker nigdy nie
# zobaczylby zadan wyslanych przez Beat.
app.conf.broker_url = "filesystem://"
app.conf.broker_transport_options = {
    "data_folder_in": "./broker/queue",
    "data_folder_out": "./broker/queue",
    "processed_folder": "./broker/processed",
    "store_processed": True,
}

# Wyniki zadan tez trzymamy w plikach.
app.conf.result_backend = "file://./results"

# --- Harmonogram okresowy ---
app.conf.beat_schedule = {
    "zadanie-co-15-sekund": {
        "task": "tasks.zadanie",
        "schedule": 15.0,   # co 15 sekund
    },
}
