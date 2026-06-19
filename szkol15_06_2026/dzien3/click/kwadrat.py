# Zamień zwykłą funkcję kwadrat, która wypisuje kwadrat liczby, w komendę click. 
# Liczba ma przychodzić jako opcja --liczba (typ int). --> 'type=int'
# Skorzystaj z @click.command(), @click.option(...) i click.echo.

import click
@click.command()
@click.option("--liczba", default=1, type=int, help="podaj liczbe")
def kwadracik(liczba):
    click.echo(f"Kwadratowa liczba {liczba} to {liczba**2}")
if __name__ == "__main__":
    kwadracik()