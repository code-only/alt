import subprocess

import click
from rich.console import Console

console = Console()


@click.group()
def react():
    """Commands related to React."""
    pass


@react.command()
@click.option('--folder', default='react-app', help='Folder name for the new React project. Default is "react-app".')
def new(folder):
    """Create new React App."""
    create_new_react_app(folder)


def create_new_react_app(folder):
    console.print(f"[bold blue]Creating a new React app in folder {folder}...[/bold blue]")
    try:
        subprocess.run(['npx', 'create-react-app', folder], check=True)
        click.echo(f"Successfully created React app in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred setting up React app: {e}", err=True)


if __name__ == '__main__':
    react()
