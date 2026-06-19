# 1. Funkcja w środku modułu -> nazwana tak samo jak pakiet
# 2. 100 % calable.... błąd nie importujemy dwóch jednocześnie wzajemnie modułów
# 3. import datetime <-- import własny moduł z funkcją o tej samej nazwie 
# *** !!!! unikamy nazwewnictwa podobnego do funkcji wbudowanych
# len(), filter(), sorted(), datetime, list(), dict(), tuple()
# 4. Jest import datetime --> zrobimy nowy import tej samej biblioteki 

# import datetime as dt
# as dat
# dt.now()