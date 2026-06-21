"""
Instancja Celery w OPCJI C — broker na plikach.
Zero Dockera, zero Redisa: kolejką są zwykłe foldery na dysku.

Foldery broker/in, broker/out, broker/processed oraz results
tworzy automatycznie skrypt start.bat (albo utwórz je ręcznie).
"""
from celery import Celery

app = Celery("projekt")

# Każ Celery załadować plik z zadaniami, żeby je zarejestrował.
app.conf.imports = ("tasks",)

# --- Broker oparty o system plików (bez żadnego serwera) ---
app.conf.broker_url = "filesystem://"
app.conf.broker_transport_options = {
    "data_folder_in": "./broker/in",
    "data_folder_out": "./broker/out",
    "data_folder_processed": "./broker/processed",
}

# Wyniki zadań też trzymamy w plikach.
app.conf.result_backend = "file://./results"

# --- Harmonogram okresowy: TU jest "wplecenie" pollingu co 5 minut ---
app.conf.beat_schedule = {
    "odpytaj-co-15-sekund": {
        "task": "tasks.odpytaj_aplikacje",
        "schedule": 15.0,   # TEST: co 15 sekund (docelowo 300.0 = 5 minut)
    },
}
