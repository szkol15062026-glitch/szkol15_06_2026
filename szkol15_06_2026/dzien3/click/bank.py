# Napisz komendę konto, która przyjmuje opcję --operacja ograniczoną do wplata/wyplata (użyj click.Choice)
# oraz opcję --kwota (typ int). Komenda ma wypisać np. wplata: 100. Dodaj do funkcji docstring, żeby pojawił 
# się w --help, i sprawdź, że click sam wygeneruje pomoc.


import click

@click.command()
@click.option("--operacja", type=click.Choice(["wplata", "wyplata"]))
@click.option("--kwota", type=int)
def konto(operacja, kwota):
    """Wpłacam lub wypłacam podana kwote"""
    click.echo(f"Operacja {operacja} na kwote {kwota}")
    
if __name__ == "__main__":
    konto()