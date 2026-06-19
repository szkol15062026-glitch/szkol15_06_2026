########################################################################################################################
# Iteratory # Iteratory # Iteratory # Iteratory # Iteratory # Iteratory # Iteratory # Iteratory # Iteratory # Iteratory
#-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--##-->1<--###-->1<--###-->1<--##
########################################################################################################################
#  Iteratory
# – __iter__
# – __next__

# Iterator = obiekt, po którym for przechodzi krok po kroku. Musi mieć dwie metody:

# __iter__(self) → zwraca sam iterator (zwykle return self),
# __next__(self) → zwraca KOLEJNĄ wartość, a gdy nie ma już nic — robi raise StopIteration.


# generatory -->
# for -->  nie wywala stopite--> kończy na nim 

# iterable --> obiekt, który ma możliwość iterowania --> listy, słowniki, krotki -->
"""
class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i
"""


lista = [5,7,3,4,5] #--> iterable  (5,6) etc

# print(next(lista)) # --> nie jest iteratorem

iterable_to_iter = iter(lista)

print(next(iterable_to_iter))
print(next(iterable_to_iter))
print(next(iterable_to_iter))
print(next(iterable_to_iter))
print(next(iterable_to_iter))
# print(next(iterable_to_iter)) # --> stopiterrations

# Iterator to wbudowana zaplecze do korzystania z pętli bez błędu stopiterrations

# Wykonać iteracje dla obiektów
string_example = 'Python'
tuple_example = (5,7)

# zmienia iterable na iterator
petla = [2,3,4]

for i in petla:
    print(i)