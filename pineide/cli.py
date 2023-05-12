import click

from pineide.pine import Pine


@click.command()
@click.argument("path", default="./", type=click.Path(exists=True))
def main(path: str):
    """Run the IDE"""
    Pine(path).run()
