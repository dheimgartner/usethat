import click

@click.command(help = "poetry demo.")
def run():
    print("hello cli")