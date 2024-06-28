import subprocess

import click
from rich.console import Console

console = Console()


@click.group()
def magento():
    """Commands related to Magento."""
    pass


@magento.command()
@click.option('--version', default='2.4', help='Magento version to setup. Default is 2.4.')
@click.option('--folder', default='magento', help='Folder name for the new Magento project. Default is "magento".')
def new(version, folder):
    """Create new Magento project."""
    create_new_magento_project(version, folder)


def create_new_magento_project(version, folder):
    console.print(f"[bold blue]Installing Magento {version} in folder {folder}...[/bold blue]")
    try:
        subprocess.run(['composer', 'create-project', f'magento/project-community-edition={version}', folder],
                       check=True)
        click.echo(f"Successfully set up Magento {version} in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred setting up Magento: {e}", err=True)
