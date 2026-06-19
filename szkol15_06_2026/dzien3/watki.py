########################################################################################################################
# Wprowadzenie do asynchroniczności w Pythonie # Wprowadzenie do asynchroniczności w Pythonie # Wprowadzenie do asynchro
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################
# Wprowadzenie do asynchroniczności w Pythonie

# przykład wątków odpalonych w tym samym czasie 
"""
import threading

def praca(i):
    print(f"wątek {i} działa")

watki = [threading.Thread(target=praca, args=(i,)) for i in range(4)]

# threading.Thread(target=praca) # --> jest to wątek (1)

for w in watki:
    w.start()    # uruchom wszystkie (start NIE czeka)
for w in watki:
    w.join()      # dopiero teraz czekaj na każdy

# wątki się konczą (kończą swoją robotę) --> dopiero kod nad dole
print("wszystkie skończyły")
"""



import threading, time

def praca(i=1):
    time.sleep(1)                 # wątek "pracuje" 1 sekundę
    print(f"  wątek {i} skończył pracę")

watki = [threading.Thread(target=praca, args=(i,)) for i in range(4)] #->> 0, --> (0)
for w in watki:
    w.start()

for w in watki:
    w.join()

# threading.Thread(target=praca).start()
# threading.Thread(target=praca).start()

print("main: po join() -> teraz NA PEWNO wszystkie skończyły")
print("main: po join() -> teraz NA PEWNO wszystkie skończyły")
print("main: po join() -> teraz NA PEWNO wszystkie skończyły")


# Napisz funkcję podwajaj(nazwa), która startuje od n = 1 i kilka razy podwaja tę wartość (n = n * 2), 
# za każdym razem wypisując nazwę wątku i aktualny wynik. Uruchom ją na 3 wątkach i poczekaj 
# na wszystkie przez join().
"""
import threading
def podwajaj(n):
    n = 1
    for i in range(5):
        n = n*2
        print(f"wynik podwajania: {n}")

# --> jak nie podam n to n = 1

watki = [threading.Thread(target=podwajaj, args=(f'Wątek nr:{n}',)) for n in range(3)]

for w in watki:
    w.start()
    print(w)

for w in watki:
    w.join()

print(f"Kończymy działanie programu")
"""



import time
import threading

def tripple_double(i):
    x = 1
    time.sleep(1)
    while True:
        x *= 2
        # print(x)
        if x > 100:
            break
        return x

tds = [threading.Thread(target=tripple_double, args=(i,)) for i in range(3)]

# for td in tds:
#     td.start()
# print(td)

# for td in tds:
#     td.join()

# for _ in range(5): --> nie korzystanie z pętli 
#     pass

# <Thread(Thread-1 (tripple_double), started 124514056185536)>
# <Thread(Thread-2 (tripple_double), started 124514047792832)>
# <Thread(Thread-3 (tripple_double), started 124514039400128)>

# class Konto:
#     def __init__(self):
#         pass

# konto = Konto()
# print(konto)

########################################################################################################################
# Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # Daemon # D
#-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##--
########################################################################################################################
## Wątki jako demony?

"""
import time, threading

def odliczaj(ile):
    for x in range(ile):
        print(x)
        time.sleep(1)
        
f = threading.Thread(target=odliczaj, args=(10,), daemon=False)
f.start()

print('koniec')
print('koniec')
print('koniec')
print('koniec')
"""

# Program wypisze tylko 0 i od razu się kończy — demon zostaje zabity.

# daemon --> defaulta ustawiony na False --> działa jak bez argumentu i wykonuje kod
# daemon --> True --> czuwasz, czyli siedzi w kodzie, i trwa (monitoring, logowanie, heartbeat, odświeżanie cache w tle.)

"""
Napisz wątek-demon, który w nieskończonej pętli co sekundę wypisuje tik. 
W głównym programie „popracuj" przez 3 sekundy (time.sleep(3)), a potem wypisz koniec programu. 
Nie używaj join(). Zaobserwuj, że demon zatrzymuje się sam, gdy główny wątek się kończy.
"""

#Celery --> funkcje w środek i w tym momencie dodajesz czas  

import time
import threading

def ticker(i=1):
    while True:
        print("Tick")
        time.sleep(1)


# td = threading.Thread(target=ticker, args=(1,), daemon=False)
td = threading.Thread(target=ticker, args=(1,), daemon=True)

td.start()

(time.sleep(3))
print('Koniec')