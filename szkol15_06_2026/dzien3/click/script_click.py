# python -m venv venv
# .\venv\Scripts\Activate
# pip list 
# pip install click 

import click

@click.command() 
@click.option("--imie", default="świecie", help="kogo przywitać")
def witaj(imie):
    click.echo(f"Witaj {imie}!") # print()

if __name__ == "__main__":
    witaj()

"""
# python script_click.py --imie Ala   ->  Witaj Ala!
# python script_click.py              ->  Witaj świecie!
# python script_click.py --help       ->  click SAM generuje pomoc z help=
"""