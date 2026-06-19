# Iteratory Przykład jak to działa bardziej za plecami pętle?
"""
Protokół Iteratora to jest dokładne wyjaśnienie tego co się dzieje w trakcie korzystania w pythonie z pętli:
for i in lista:
    .....

for i in range(5): -->
    ......

Iterator działa tylko i wyłącznie na obiekty w pythonie, które są w stanie przechodzić krok po kroku.
Brać jeden element, następnie kolejny, kolejny, kolejny, aż skończy im się zapas. Co jest takim iterable?
Odpowiedź jest prosta:
--> string --> 'Python' --> można tu przechodzić po literach P-->y-->t-->h-->o-->n
--> range(5) --> też implementuje __iter__ i przechodzi po 0-->1-->2-->3-->4
--> tuple --> (2,5,6) --> można przechodzić po cyfrach 2-->5-->6
--> list --> [5,'str',7,6.5] --> można przechodzić po ele.(str,float,int) 5-->str-->7-->6.5
--> set -->  {2,5,7,2} --> można przechodzic po cyfra 2-->5-->7 #brak drugiej 2 to nie błąd set bierze tylko
unikalne wartosci a kazdy duplikat kasuje
--> dict --> {'imie':'Damian','age':24} VVVV
########################### można przechodzić po kluczach -->imie-->age #############################
########################### mozna po wartościach -->Damian-->24         #############################
########################### po klucz i warto imie:damian-->age:24       #############################


__iter__ tworzy/zwraca iterator i ustawia go przed pierwszym elementem (to wywołuje iter())
__next__ pamięta GDZIE JESTEŚ i podaje następny element, znając poprzednie położenie (to wywołuje
next())
StopIteration daje znać, że nie ma już kolejnego elementu, więc next() się nie wykona i pętla się
kończy

Analogia ze świata nr1: --> (Playlista)
Iterable -> Mozna przejść po kawałku(pętli) puszczasz jeden utwór po drugim.
Iterator -> Odtwarzacz(mp3) -> pamięta na jakim utworze zakończyliśmy słuchanie
Next -> przycisk next -> możesz przejść do kolejnego utworu
StopIteration -> playlista się kończy, muzyka przestaje grać(nie bierzmy pod uwage shufle, odtwarzania w nieskończoność)

Analogia ze świata nr2: --> (Książka)
Iterable -> Można przejść od strony do strony etc.
Iterator -> zakładka, dzięki której pamiętasz obiekt -> stronę
Next -> przesuwasz zakładkę dalej po przeczytaniu strony
StopIteration -> kończą się strony, nie ma co czytać dalej

Analogia ze świata nr3: --> (Matrioszka)
Iterable -> matrioszka sama w sobie, możesz otworzyć jedną po drugiej
Iterator -> po otworzeniu jednej/kilku pamięta stan, większe otworzone leżą z boku
Next -> otworzenie kolejnej matrioszki
StopIteration -> Ostatnia lalka matrioszki już się nie otwiera, koniec

W pythonie:
owoce = ["jabłko", "banan", "wiśnia"]   # --> ITERABLE

it = iter(owoce) -> iter() robi ITERATOR z ITERABLE --> umieszcza przed pierwszym elementem, dlatego pierwszy next() daje jabłko

print(next(it)) "jabłko" <-- next() daje kolejny
print(next(it)) "banan"
print(next(it)) "wiśnia"
print(next(it)) --> StopIteration --> koniec

Wygląda znajomo ---> generatory --> yield --> to co się dzieje za plecami for

Własnoręcznie iteratorów prawie się nie pisze. Ten temat to zaglądanie pod maskę — pokazuje, co Python robi za Twoimi
plecami przy każdym for. W pętlach for dodatkowo next() jest opakowany w try/except, który wyłapuje 'aha nie ma
kolejnego elementu koniec wywoływania next(), wykonuj dalej kod'

Dodatkowo linki z tematami iteratorów:
-https://www.geeksforgeeks.org/python/iterators-in-python/
-https://www.w3schools.com/python/python_iterators.asp
-https://realpython.com/python-iterators-iterables/#understanding-iteration-in-python -> możlwie będzie wymagało logowania
"""