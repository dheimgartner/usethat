import click
from . import scaffold as old

@click.group()
def cli():
    pass

@cli.command(help = "Scaffold a minimal python package")
def scaffold():
    old.scaffold()