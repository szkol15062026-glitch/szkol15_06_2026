# Napisz komendę oblicz, która przyjmuje dwa pozycyjne argumenty liczbowe a i b (typ int) oraz flagę --mnoz. 
# Domyślnie komenda ma wypisać sumę a + b, a przy włączonej fladze — iloczyn a * b.

import click

@click.command()
@click.argument("a", type=int)                          # pozycyjny, wymagany
@click.argument("b", type=int)
@click.option("--mnoz", is_flag=False) 
def oblicz(a, b, mnoz):
    if mnoz:
        wynik = a + b
        click.echo(wynik)
    else: 
        wynik = a * b      
        click.echo(wynik)

if __name__ == "__main__":
    oblicz()

# python plik.py 2 6 --mnoz
