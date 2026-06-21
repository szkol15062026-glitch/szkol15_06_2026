"""
threading.Timer — czysty Python, BIBLIOTEKA STANDARDOWA (nic nie instalujesz).
Pokazowka: co 15 sekund wykonuje funkcje, ktora wypisuje napis.

HACZYK: threading.Timer odpala funkcje tylko RAZ, po zadanym czasie.
Zeby powstal cykl, na koncu kazdego wykonania PLANUJEMY kolejny Timer.
To tzw. "samo-planujacy sie" timer.
"""
import time
import threading

INTERWAL = 15   # sekundy


def zadanie():
    print("Zadanie wykonane (co 15 sekund).")


def cykl():
    """Wykonaj zadanie, a potem ZAPLANUJ kolejne wywolanie za INTERWAL sekund."""
    zadanie()

    # To jest sedno: tworzymy NOWY Timer na kolejny cykl.
    t = threading.Timer(INTERWAL, cykl)
    t.daemon = True   # watek-demon: zginie razem z programem (czysty Ctrl+C)
    t.start()


if __name__ == "__main__":
    print(f"Timer wystartowal. Co {INTERWAL} s wykonuje zadanie. Ctrl+C aby zakonczyc.")

    # Pierwszy timer — pierwszy cykl odpali sie za INTERWAL sekund.
    pierwszy = threading.Timer(INTERWAL, cykl)
    pierwszy.daemon = True
    pierwszy.start()

    # Glowny watek musi zyc, inaczej program zakonczylby sie od razu.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nZatrzymano.")
