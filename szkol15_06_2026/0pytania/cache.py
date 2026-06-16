#######################################################################################################################
#Kantor walut

from functools import lru_cache
import time

OPLATA = 0.1

def kurs_bez_cache(waluta):
  time.sleep(OPLATA)
  return {"EUR": 4.30, "USD": 3.95, "GBP": 5.10}[waluta]

@lru_cache(maxsize=None)
def kurs_z_cache(waluta):
  time.sleep(OPLATA)
  return {"EUR": 4.30, "USD": 3.95, "GBP": 5.10}[waluta]

waluty = ["EUR", "USD", "GBP"]

t = time.perf_counter()
for i in range(103): kurs_bez_cache(waluty[i % 3])
czas_bez = time.perf_counter() - t

t = time.perf_counter()
for i in range(103): kurs_z_cache(waluty[i % 3])
czas_z = time.perf_counter() - t

print(f"bez cache: {czas_bez:.2f}s  (bank pytany 103 razy)")
print(f"z cache:   {czas_z:.2f}s  (bank pytany tylko 3 razy)")
print(f"przyspieszenie: ~{czas_bez / czas_z:.0f}x")
print(kurs_z_cache.cache_info())

########################################################################################################################

"""
Przykłady z realnego życia
Tłumaczenie słów --> api tłumacza --> częste te same słowa w tekście
Pogoda dla miast --> api pogody --> odpytywanie ciągle tych samych miast
szukanie adresu --> api adresu --> powtarzające się adresy
czas dojazdu --> wyliczanie trasy --> te same pary miast
"""