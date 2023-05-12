import click
from pineide.ide import PineIDE


@click.command()
def main():
    """Run the IDE"""
    PineIDE.run(title="PineIDE")
