"""
APScheduler — czysty Python, JEDEN PROCES, bez brokera, bez Dockera.
Pokazowka: co 15 sekund wykonuje funkcje, ktora wypisuje napis.
Petle ma wbudowana sam scheduler (scheduler.start()).
"""
from apscheduler.schedulers.blocking import BlockingScheduler


def zadanie():
    print("Zadanie wykonane (co 15 sekund).")


scheduler = BlockingScheduler()

# Co 15 sekund.
scheduler.add_job(zadanie, "interval", seconds=15)
# Przyklad alternatywy: codziennie o 8:00 ->
# scheduler.add_job(zadanie, "cron", hour=8, minute=0)


if __name__ == "__main__":
    print("Scheduler wystartowal. Co 15 s wykonuje zadanie. Ctrl+C aby zakonczyc.")
    try:
        scheduler.start()   # blokuje i odpala zadania wg harmonogramu
    except (KeyboardInterrupt, SystemExit):
        print("\nZatrzymano.")
