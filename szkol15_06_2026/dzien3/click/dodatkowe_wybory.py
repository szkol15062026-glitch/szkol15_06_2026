import click

@click.command()
@click.option("--kolor", type=click.Choice(["czerwony", "zielony", "niebieski"]))
def maluj(kolor):
    """Maluje w wybranym kolorze."""     # docstring = opis w --help
    click.echo(f"maluję na {kolor}")

if __name__ == "__main__":
    maluj()