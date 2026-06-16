
### Generator ###### Generator ###### Generator ###### Generator ###### Generator ###### Generator ###### Generator ####
########################################################################################################################
# yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## yield ## y
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################
# Generatory Czym są generatory?

def startuj(): # --> yield == generator
    print('Startuje program')
    yield 1
    print('Wywołuje pierwsze zawołanie')
    yield 2 

gen = startuj()
print(next(gen))
print(next(gen))
# print(next(gen)) # --> StopIteration nie ma kolejnego elementu do zwrócenia

gen2 = startuj()
print(next(gen2))
print(next(gen2))

gen3 = startuj()
print(list(gen3))
print(list(gen3))

# 1. Napisz generator parzyste(n), który leniwie zwraca kolejne liczby parzyste od 0 do n włącznie.
# 2. Generator licznik_slow(zdania) dostaje listę zdań (stringów) i dla każdego zwraca liczbę słów

# 1.
def generator_liczb(n): 
    for i in range(0,n+1,2):
        yield i

gen = generator_liczb(10)
print(list(generator_liczb(10)))
print(next(gen),next(gen),next(gen))

print("*"*100)
def parzyste(n):
    for n in range(n+1):
        if n % 2 == 0:
            print(n)
            yield n
        # print(n)
        # yield n
        # print(n+2)
        # yield n+2

parz = parzyste(8)
print(list(parz))
# print(next(parz))
# print(next(parz))
# print(next(parz))

# 2.
def word_gen(phrase):
    for word in phrase.split():
        yield len(word)

gen = word_gen('Ala ma kota')

print(list(gen))

dane = ["Ala ma kota", "Python jest super", "koniec"]

def word_gen(phrase):
    for word in phrase:
        yield len(word.split())

gen = word_gen(dane)

print(list(gen))

########################################################################################################################
# Generatory skończone # Generatory skończone # Generatory skończone # Generatory skończone # Generatory skończone # Gen
#-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--###-->2<--##
########################################################################################################################

#generator który zwraca parzyste
def zwraca_parzyste(n):
    for i in range(0,n+1,2): # --> (start,stop,step)
        yield i

def zwraca_parzyste_ifem(n):
    for i in range(0,n+1):
        if i % 2 ==0: #-->modulo sprawdza czy zwraca resztę
            yield i

gen_parz = zwraca_parzyste(4)
print(next(gen_parz))

# 3. Napisać dwa generatory Jeden, żeby zwracał nam liczby do n, a drugi, żeby
# 4. zwracał nam sześcian z każdej liczby/elementu danej listy

# 3.
print("*"* 100)
def liczby(n):
    for i in range(n+1):
        yield i

run = liczby(12)
print(list(run))

# 4.
lista_danych = [2,4,6,7]
def szescian(lista):
    for i in lista:
        i = i**3
        yield i
szes = szescian(lista_danych)
print(list(szes))


def liczby_do_n(n):
    for i in range(1,n+1):
        yield i

# for liczba in liczby_do_n(10):
#     print(liczba)

def sześciany(lista):
    for liczba in lista:
        yield liczba**3

lista = [2,4,6,7]

# 5. Zwrócić listę szczescianów z generatora liczb i od razu wrzucic do szescianow

# 5.
# Rozwiązanie nr1
def liczby(n):
    for i in range(n+1):
        yield i
run = liczby(12)

wynik = list(run)

def szescian(lista):
    for i in lista:
        i = i**3
        yield i

szes = szescian(wynik)
print(list(szes))

# Rozwiązanie nr2
def liczby_do_n(n):
    for i in range(1,n+1):
        yield i

lista = [x for x in liczby_do_n(10)]
print(lista)

#lista = [2,3,4,5,6,7]

def sześciany(lista):
    for liczba in lista:
        yield liczba**3

for liczba in sześciany(lista):
    print(liczba)

# 6. Pomiędzy generatorami umieścić jeszcze jeden generator odpowiedzialny za przesiewanie listy,
# z naszej listy tylko parzyste elementy

print("%"*150)
# Rozwiązanie nr1.

# 6.
def liczby_do_n(n):
    for i in range(1,n+1):
        yield i

lista = [x for x in liczby_do_n(10)]
print(lista)

def sieve(lista):
    for i in lista:
        if i % 2 == 0:
            yield i
parzyste = [x for x in sieve(lista)]
print(parzyste)

def sześciany(lista):
    for liczba in lista:
        yield liczba**3

lista_sześcianów = [x for x in sześciany(parzyste)]
print(lista_sześcianów)

print("%"*150)
print("#"*150)

# Rozwiązanie nr2.
def liczby(n):
    for i in range(n+1):
        yield i
run = liczby(12)
wynik = list(run)
def parzyste(input):
    for i in input:
        if i % 2 ==0:
            yield i
parz = list(parzyste(wynik))
def szescian(lista):
    for i in lista:
        i = i**3
        yield i
szes = szescian(parz)
print(list(szes))

print("#"*150)

########################################################################################################################
# Generatory nieskończone # Generatory nieskończone # Generatory nieskończone # Generatory nieskończone # Generatory nie
#-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##-->3<--##--
########################################################################################################################

def zwracaj_kolejne_cyfry():
    n = 0
    while True:
        yield n
        n += 1

gener = zwracaj_kolejne_cyfry()
print(next(gener))
print(next(gener))
print(next(gener))
print(next(gener))

# !!! Nie wolno korzystać z metody list() !!!

# # 7. Napisać generator zwracający mnozenie liczby o 2 w nieskończoność
# 1 ** 2 --> 2 ** 2

#Rozwiązanie1
def return_numbers():
    x = 1
    while True:
        yield x ** 2
        x += 1

return_numbers_inst = return_numbers()
print(next(return_numbers_inst))
print(next(return_numbers_inst))
print(next(return_numbers_inst))

print('*'*20)
for i in return_numbers():
    print(i)
    if i > 0:
        break

def mnozenie(): # do sprawdzenia
    n = 1
    while True:
        yield n*2
        n = n + 1
    
mnoz = mnozenie()
print(next(mnoz))
print(next(mnoz))
print(next(mnoz))
print(next(mnoz))
print(next(mnoz))

from itertools import islice

def potegi_dwojki():
    n = 1
    while True:
        yield n
        n *= 2

print(list(islice(potegi_dwojki(), 10)))   # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# 8. Napisać generator, który będzie generował numer biletu z prefixem 'Bilet' dodając na samym końcu
# z każdym wywołaniem nową cyfre czyli np. 'Bilet-001,Bilet-002. 
# def generator(prefix): .... **Generator nieskończony**
# Następnie wymień w liście pierwsze 10 biletów ***n:04d* 

# 8.
# Rozwiązanie nr1
def generator(prefix):
    n = 1
    while True:
        yield f'{prefix}{n:02d}'
        # yield str(prefix) + str(n)
        n += 1

print(list(islice(generator("Bilet-"),10)))

# Rozwiązanie nr2
def generator(prefix):
    n = 1
    while True:
        yield prefix + str(n)
        n += 1

gen = generator("Bilet-")

from itertools import islice
print(list(islice(gen, 10)))