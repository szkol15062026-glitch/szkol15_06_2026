
import click

@click.command()
@click.argument("imie")                          # pozycyjny, wymagany
@click.option("--krzycz", is_flag=True)          # flaga włącz/wyłącz
@click.option("--powtorz", default=1, type=int, show_default=False)
def witaj(imie, krzycz, powtorz):
    tekst = f"Cześć {imie}"
    if krzycz:
        tekst = tekst.upper() + "!"
    for _ in range(powtorz):
        click.echo(tekst)

if __name__ == "__main__":
    witaj()
# python plik.py Ala --krzycz --powtorz 2
# CZEŚĆ ALA!
# CZEŚĆ ALA!