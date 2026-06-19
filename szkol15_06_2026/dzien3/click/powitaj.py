# Napisz komendę click o nazwie powitaj, która przyjmuje: pozycyjny argument imie, flagę --glosno 
# oraz opcję --powtorz (liczba całkowita, domyślnie 1). Komenda ma wypisać Cześć <imie> tyle razy, ile wynosi --powtorz,
# a przy włączonej fladze zamienić tekst na wielkie litery.

import click

@click.command()
@click.argument("imie")  
@click.option("--glosno", is_flag=True) 
@click.option("--powtorz", type=int, default=1) 
def powitaj(imie , glosno,powtorz):
    if glosno:
        wynik = f'Cześć {imie.upper()}'
        click.echo(wynik)
    else: 
        wynik = f'Cześć {imie}'
        for _ in range(powtorz):
             click.echo(wynik)
if __name__ == "__main__":
    powitaj()


# python plik.py 2 6 --mnoz
# @click.argument("liczby", nargs=-1) --> -1 to dla nas *args --> krotka
# @click.argument("liczby", nargs=2)
# x, y = liczby