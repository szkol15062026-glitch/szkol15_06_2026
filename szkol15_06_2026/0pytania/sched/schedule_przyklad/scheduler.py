"""
schedule — czysty Python, JEDEN proces, bez brokera, bez Dockera.
Pokazowka: co 15 sekund wykonuje funkcje, ktora wypisuje napis.

Roznica wzgledem APScheduler: tutaj SAMI piszemy petle (while True),
ktora co sekunde pyta 'schedule', czy cos juz dojrzalo do wykonania.
"""
import time
import schedule


def zadanie():
    print("Zadanie wykonane (co 15 sekund).")


# Rejestracja harmonogramu. Co 15 sekund.
schedule.every(15).seconds.do(zadanie)
# Przyklad alternatywy: codziennie o 8:00 ->
# schedule.every().day.at("08:00").do(zadanie)


if __name__ == "__main__":
    print("Scheduler wystartowal. Co 15 s wykonuje zadanie. Ctrl+C aby zakonczyc.")
    try:
        # WLASNA petla: co sekunde pytamy schedule, czy cos dojrzalo.
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nZatrzymano.")
