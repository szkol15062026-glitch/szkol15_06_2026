### Listy ###### Listy ###### Listy ###### Listy ###### Listy ###### Listy ###### Listy ###### Listy ###### Listy ######

########################################################################################################################
# Tworzenie list # Tworzenie list # Tworzenie list # Tworzenie list # Tworzenie list # Tworzenie list # Tworzenie list #
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################
lista_example = []

# str -> teksty 'abrakadrabra' int --> cyfry 2 float -> 3.5 bool -> True, False list, słowniki ....
lista_mieszana = [2,5.6,'str',True, 4]
lista_list = list() # -> []

print(lista_example)
print(lista_list)
print(lista_mieszana)

# comprehension
lista_wypelniona = [a for a in range(5)] # -> range(6) -> 0, 1,2,3,4,5   pętle zapisuje for a in range(5): print(a) 
print(lista_wypelniona)

# for a in range(5):
#     print(a)

lista_mnozenie = [0]*5
print(lista_mnozenie)

# 1.zadanie 
#  1.1 Stwórz listę liczb 1-10  --> użyj range(start,stop) 
#  1.2 comprehension - listę ich kwadratów. -> a**2
#  1.3 Z napisu "Python" zrób listę liter. -> użyj list()
#  1.4 Stwórz listę pięciu zer bez ręcznego wpisywania.

# 1.1
lista_10 = list(range(1,11))
print(lista_10)
# 1.2
lista_compr = [a**2 for a in lista_10]
print(lista_compr)
# 1.3
lista_pyh = list('Python')
print(lista_pyh)
# 1.4
lista_5_zer =[0]* 5
print(lista_5_zer)

#Pułapki mnożenia
lista_5_zer = [[0]] * 5 #--> 99 append()
print(lista_5_zer)

slownik = {1:'jeden',2:'dwa'} #--> da nam tylko wartości do listy z kluczami
lista_slownik = list(slownik)
print(lista_slownik)

lista_pulapka = ['karwasze',3,6.7,'jagoda']
lista_nowa = lista_pulapka

lista_nowa.append('kura')
print(lista_pulapka)
print(lista_nowa)

#copy()
lista_nowa_nowa = lista_pulapka.copy()

########################################################################################################################
# Pobieranie wartości z list ## Pobieranie wartości z list ## Pobieranie wartości z list ## Pobieranie wartości z list #
#-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--##-->1.2<--
########################################################################################################################

owoce = ['jagoda','banan','truskawka','granat','jablko']
#owoceindex --> [0,1,2,3,4]

pierwszy_element = owoce[0]
print(f"Nasz pierwszy element to -> {pierwszy_element}")
ostatni_element = owoce[-1]
print(f"Nasz ostatni element to -> {ostatni_element}")

# slicing = listy   lista[start,end,step]
# start - jest początek listy, czyli z którego miejsca startujemy
# end - jest koncem gdzie kończymy na jakimś punkcie nie biorąc go pod uwagę
# step - o ile kroków
print(f"Slicing --> {owoce[2:]}") # od drugiego elementu do końca
print(f"Slicing --> {owoce[-2:]}") # ostatnie dwa elementy
print(f"Slicing --> {owoce[1:4:2]}") # od 1 do 3*(zawsze - 1) co drugi element
print(f"Reverse list --> {owoce[::-1]}") # odwrócona lista

# 2. Mając 
dni = ["pon","wt","śr","czw","pt","sob","nd"] 
# 2.1 wyłuskaj: pierwszy i ostatni dzień, dni robocze (wycinkiem),
# 2.2 weekend (indeksami ujemnymi), 
# 2.3 co drugi dzień, 
# 2.4 listę odwróconą (nową, bez psucia dni).

# 2.1
dni[0]
dni[-1]
lista_ostatni_pierwszy = [dni[0],dni[-1]]
print(lista_ostatni_pierwszy)
print(dni[0::6])
# 2.2 
print(dni[-2:])
# 2.3
print(dni[::2])
# 2.4
nowa_dni = dni[::-1] # slicing tworzy nam nową listę
print(dni[::-1])

lista_pulapka_slicing = [2,5,3] # 0 1 2

print(lista_pulapka_slicing[:100]) # idzie dalej bez problemu

########################################################################################################################
# Iterowanie po listach # Iterowanie po listach # Iterowanie po listach # Iterowanie po listach # Iterowanie po listach
#-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--##-->1.3<--
########################################################################################################################
# 0 1 2 3 4 

for owoc in owoce:
    print(f"Owoc: {owoc}")

for index,owoc in enumerate(owoce,start=1): #-> start odkad ma zaczynac liczyc
    print(f"Nr:{index} --> {owoc}")

imiona = ['Adam','Jacek','Natalia']
wiek = [56, 25, 97]

for imie,lat in zip(imiona,wiek): # kolejnosc przekazywania ma znaczenie
    print(f"Imię:{imie} oraz wiek: {lat}")

# [[0]]*5
lista_zagnie = [["jacek",25],['Adam',25],['natalia', 97]]

# Pętle zagnieżdzone
for lista_osob in lista_zagnie: 
    for dane in lista_osob:
        print(dane)

# 3.1 Mając oceny = [3,5,2,4,5] wypisz je w formacie 1. ocena: 3 (numeracja od 1),
# * a potem podwój każdą ocenę w miejscu (oceny ma faktycznie się zmienić, nie powstać nowa lista

#3.1
oceny = [3,5,2,4,5]

for i, o in enumerate(oceny, start=1):
    print(f"{i}. ocena: {o*2}")

for i in range(len(oceny)):
    oceny[i] *=  2    # --> *= --> +=
print(oceny)

for lista_osob in lista_zagnie: 
    print(lista_osob[0])

lista_zagn = [['JAcek',25]] #--> pandas, numpy 

print(lista_zagn[0][0])

########################################################################################################################
# Sprawdzanie czy element znajduje się na liście # Sprawdzanie czy element znajduje się na liście # Sprawdzanie czy elem
#-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--##-->1.4<--
########################################################################################################################

# 0 1 2 3
owoce = ['jagoda','banan','truskawka','granat','jablko']

# '' in lista

print('jaGoda'.lower() in owoce) # metoda pomniejszania liter sprawdzanie czy str jest w liście
# Zadanie SPrawdcie czy granat znajduje sie na liscie
print(owoce.index('banan'))

# print(owoce.index('adamantum'))
# Zadanie SPrawdcie działanie index
# ominięcie błędu index()
if 'banan' in owoce:
    print(f"Index banana to {owoce.index('banan')}")
else:
    print('Nie ma takiego owoca na liście')

print(owoce.count('bananaa'))

# 4.1Mając
koszyk = ["mleko","chleb","masło","mlekooo"]
# sprawdź czy jest "masło", policz "mleko", 
# bezpiecznie podaj indeks "jajka" (bez błędu), 
# sprawdź czy którekolwiek słowo ma więcej niż 5 liter. --> len()

# 4.1
if 'masło' in koszyk:
    print(True)

print('masło' in koszyk)

print(koszyk.count('mleko'))

if 'jajko' in koszyk:
    print(f"Index jajka: {koszyk.index('jajko')}")
else:
    print("Brak jajka w koszyku")

print('*'*20)
for element in koszyk:
    if len(element) > 5:
        print(f"Element: {element} is longer than 5 characters")
    else:
        print(f"Element: {element} is shorter than 5 characters")

########################################################################################################################
# Modyfikowanie zawartości listy # Modyfikowanie zawartości listy # Modyfikowanie zawartości listy # Modyfikowanie zawar
#-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--##-->1.5<--
########################################################################################################################

# metody append insert extend ...

lista_ind = [25,65,86]

print(lista_ind)
lista_ind[-1] = 65
print(lista_ind)

lista_ind[1:] = [0,0,0]
print(lista_ind)

lista_ind.append(6)
print(lista_ind)

lista_ind.append([5,7,4])
print(lista_ind)

lista_ind.extend([5,7,4])
print(lista_ind)

lista_ind.insert(0,0)
print(lista_ind)

# 5 zadanie
owoce = ['banan','jablko']
# 5.1 na sam koniec 'ananas'
# 5.2 na sam początek 'morele'
# 5.3 na sam koniec zagniezdzeną listę oraz metodą extend kilka elementów za jednym razem

owoce = ['banan', 'jabłko']

owoce.append('ananas')
print(owoce)

owoce.insert(0,'morele')
print(owoce)

owoce.append(['gruszka','śliwka','brzoskwinia'])
print(owoce)

owoce.extend(['gruszka','śliwka','brzoskwinia'])
print(owoce)

# Usuwania elementów z listy --> metody remove() pop()  del

ostatni = owoce.pop()
print(owoce)
print(ostatni)
pierwszy = owoce.pop(0)
print(pierwszy)
print(owoce)

del owoce[3]
print(owoce)

# del owoce[20] --> index ma znaczenie

del owoce[3:]
print(owoce)

owoce.remove('banan')
print(owoce)

if 'banan' in owoce:
    owoce.remove('banan')
else:
    print(f"Owoca nie ma")

# 6.
koszyk = ["mleko","chleb","masło","mleko",'kura',['jajka','keczup'],'jajka']
# 6.1 usuń za pomocą pop() chleb i zachowaj w zmiennej
# 6.2 usuń za pomocc remove element 'maszynka do golenia' z listy
# 6.3 usuń za pomoca del liste zagniezdoną

koszyk = ['mleko', 'chleb', 'masło', 'mleko', 'kura', ['jajka', 'ketchup'], 'jajka']

# 6.1
v_chleb = koszyk.pop(koszyk.index('chleb'))

print(v_chleb)
print(koszyk)

# 6.2
if 'maszynka do golenia' in koszyk:
    koszyk.remove('maszynka do golenia')

print(koszyk)

# del koszyk[5] --> prostszy

# 6.3
for e in koszyk:
    if type(e) == list:
        del[koszyk[koszyk.index(e)]]

print(koszyk)

########################################################################################################################
# Funkcje wbudowane w listy # Funkcje wbudowane w listy # Funkcje wbudowane w listy # Funkcje wbudowane w listy # Funkcj
#-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--##-->1.6<--
########################################################################################################################

# funkcje len(), sum(), max(), min()
wiek = [15,64,23,74,23,75,27]

print(len(wiek)) #--> szukanie ile elementów w liscie 
print(sum(wiek)) #--> Sumuje
print(max(wiek)) #--> max daj największą cyfre
print(min(wiek)) #--> min daj najmniejszą

slowa = ['adam','edam','szyszynek','rower','szkola']

print(len(slowa)) #--> szukanie ile elementów w liscie 
# print(sum(slowa)) #--> Nie działa sumowanie na liscie str
print(max(slowa)) #--> max daje nam ostatni alf
print(min(slowa)) #--> min daje nam pierwszy
print(max(slowa,key=len)) #-> najdłuższe słowo
print(min(slowa,key=len)) # -> najkrótsze słowo

# Mając 
oceny=[3,5,2,4,5] 
slowa=["kot","parasol","dom","komputer"]
# policz średnią ocen, podaj max i min, znajdź najdłuższe słowo 

# ->  suma wszystkich elementów / liczba elementów --> sum() / len())

print("Średnia ocen:", sum(oceny) / len(oceny))
print("Najlepsza ocena: ", max(oceny))
print("Najgorsza ocena: ", min(oceny))
print("Najdłuższe słowo:", max(slowa, key=len))


# metody zip filter() dodatkowo
listaa = ['wiek','numer','assa']
listab = [2,6,3,6]
cyfry = [1,42,-53,98,67,34]

nowa_lista = list(zip(listaa,listab))
print(nowa_lista)
filtrowana = list(filter(lambda x: x > 0,cyfry))
print(filtrowana)

# --> () kolekcja -> tuple --> krotka = (1,0)

# lambda x: x >= 0, cyfry 

# petla = []
# for p in petla:
#     if p >= 0:
#         print(p)

########################################################################################################################
# Sortowanie i odwracanie list # Sortowanie i odwracanie list # Sortowanie i odwracanie list # Sortowanie i odwracanie l
#-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--##-->1.7<--
########################################################################################################################

# metody .sort() sorted()

lista_sort = [0,0,45,2,3]
# print(lista_sort)
# nowa_lista_sort = lista_sort.sort() #--> None # pułapka 
# lista_sort.sort()

print(lista_sort)

nowa_lista_sorted= sorted(lista_sort)
print(nowa_lista_sorted)

nowa_lista_sorted= sorted(lista_sort,reverse=True)
print(nowa_lista_sorted)

# sorted(mieszane, key=str.lower) --> str--> lower(), upper(), capitalize()   # ignoruj wielkość liter
# sorted(slowa, key=lambda x: (len(x), x.lower()))  # dwa kryteria

# sorted(slowa,key=lambda)

# lambda x: (len(x), x.lower())
########################################################################################################################
# Inne ciekawe funkcje i możliwości # Inne ciekawe funkcje i możliwości # Inne ciekawe funkcje i możliwości # Inne cieka
#-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--##-->1.8<--
########################################################################################################################

# rozpakowaywanie
unpacking_lista = [10,20,30]

a ,b, c = unpacking_lista
print(a,b,c)

unpacking_lista_large = [10,20,30,40,50,60]
z, *reszta = unpacking_lista_large

print(z, reszta)

# .join()

slowa_slowa = ['Ala', 'ma', 'kota']
# slowa_slowa = [3,65,23,52] -> operacje na str

print(" ".join(slowa_slowa))

# .split()

string_example ='Ala ma kota'
print(string_example.split(" "))