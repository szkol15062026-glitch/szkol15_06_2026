# Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki ## Słowniki #
########################################################################################################################
# Tworzenie słowników # Tworzenie słowników # Tworzenie słowników # Tworzenie słowników # Tworzenie słowników # Tworzeni
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################

slownik = {} #--> slownik pusty
# slownik #--> zawiera klucz-wartość
# klucz charakteryzuje się tym, że jest unikalny

slownik = {'imie':'Przemek','wiek':45}
print(slownik)
slownik = {'imie':'Przemek','wiek':45,'imie':'Jacek'} #--> drugi taki sam klucz nadpisuje wartość
print(slownik)

# stwórz słownik za pomocą dict
slownik_dict1 = dict() #--> pusty słownik
slownik_dict2 = dict(imie='Przemek',wiek=45)
print(slownik_dict1)
print(slownik_dict2)

# Tworzenie za pomoca zip()
imie = ['Anna','Damian','Agata']
wiek = [25,62,34]
slownik_lista = dict(zip(imie,wiek)) #-->zip()
print(slownik_lista)

# Tworzenie słownika za pomocą compre
lista_di = [a for a in range(5)]
# comprehension --> [a for a in petla]
slownik_compr = {x:x**2 for x in lista_di}
print(slownik_compr)

# metoda fromkeys
dni = dict.fromkeys(['pon','wt','śr'], "wolne")
print(dni)

# 1.1 Stwórz osoba z imie="Ala", wiek=30.
# 1.2 Z list ["a","b","c"] i [1,2,3] zbuduj słownik.
# 1.3 Zrób dict comprehension {n: n**2} dla 1-5 (klucze mają być int!).
# 1.4 Z ["Adam","Andrzej","Dominik"] zrób słownik z wartością 18 jako cyfra dla każdego klucza (bez pętli).
# 1.1
osoba = dict(imie = 'Ala', wiek = 30)
print(osoba)
# 1.2
litery = ['a', 'b', 'c']
liczby = [1, 2, 3]
zip_dict = dict(zip(litery, liczby))
print(zip_dict)
# 1.3
dict_comprehension = {x: x**2 for x in range(1,6)}
print(dict_comprehension)
# 1.4
lista_c = ['Adam', 'Andrzej', 'Dominik']
dict_bez_petli = dict.fromkeys(lista_c, 18)
print(dict_bez_petli)

########################################################################################################################
# Pobieranie wartości ze słowników # Pobieranie wartości ze słowników # Pobieranie wartości ze słowników # Pobieranie wa
#-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##-->2<--##--
########################################################################################################################

osoba = {'imie':'Renata','wiek':45,'zawod':'Bankier'}
# pobieranie zawartosci ze slownika ->
print(osoba['imie']) #--> jest klucz w slowniku
# print(osoba['telefon']) #--> nie ma klucza --> błąd
print(osoba.get('telefon')) #--> nie zwróciło nam błędu, ale jest None
print(osoba.get('telefon','Brak')) 

# jak wydobywac przez iteracje.
lista_slownik = list(osoba)  # lista_slownik = list(osoba.keys()) zwraca to samo 
print(lista_slownik)
# .keys() .values() .items()
# .keys() --> zwraca klucze
# .values() --> wartości
# .items() --> oba, czyli klucz i wartosc
lista_slownik_wart = list(osoba.values())
print(lista_slownik_wart)

for key,value in osoba.items():
    print(f"Klucz:{key} --> Wartość:{value}")

for key in osoba.keys():
    print(f"Klucz:{key} --> Wartość:?")
    
for value in osoba.values():
    print(f"Klucz:? --> Wartość:{value}")

# 2.Mając
osobal={"imie":"Ala","wiek":30,"miasto":"Kraków"}
# 2.1 pobierz imie,
# 2.2 bezpiecznie pobierz telefon z domyślną "brak"
# 2.1
print(osobal['imie'])
# 2.2
print(osobal.get('telefon','brak'))

########################################################################################################################
# Modyfikacja zawartości słowników # Modyfikacja zawartości słowników # Modyfikacja zawartości słowników # Modyfikacja z
#-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##--
########################################################################################################################

osobak={"imie":"Ala","wiek":30,"miasto":"Kraków"}
print(osobak)
osobak['imie'] = 'ola'
print(osobak)
osobak['telefon'] = '756453634'
print(osobak)
osobak.update(zawod='bankier',kraj='PL',imie='Andrzej')
print(osobak)

osobai={"imie":"Damian","wiek":30}

# del[] pop() usuwanie zawartości 

imie = osobai.pop('imie')
# telefon = osobai.pop('telefon') # --> error jak nie ma
telefon = osobai.pop('telefon','Brak') 
print(imie)
print(telefon)
print(osobai)

del osobai['wiek']
print(osobai)