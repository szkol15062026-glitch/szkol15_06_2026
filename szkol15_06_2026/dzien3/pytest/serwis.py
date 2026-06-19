import requests
def pobierz_kurs(waluta):
    return requests.get(f"https://api.example/{waluta}").json()["kurs"]
def cena_pln(kwota, waluta):
    return round(kwota * pobierz_kurs(waluta), 2)