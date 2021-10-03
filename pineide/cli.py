import click
from .ide import PineIDE


@click.command()
def cli():
    """Run the IDE"""
    PineIDE.run(title="PineIDE")
