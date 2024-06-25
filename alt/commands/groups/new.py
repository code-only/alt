import click

@click.group()
def new():
    """Commands related to new project."""
    pass

if __name__ == "__main__":
    new()