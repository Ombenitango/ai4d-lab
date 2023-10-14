import click


@click.group(short_help="ai4dlab CLI.")
def ai4dlab():
    """ai4dlab CLI.
    """
    pass


@ai4dlab.command()
@click.argument("name", default="ai4dlab")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [ai4dlab]
