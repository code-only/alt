import subprocess

import click
from rich.console import Console

console = Console()


@click.group()
def laravel():
    """Commands related to Laravel."""
    pass


@laravel.command()
@click.option('--version', default='8.x', help='Laravel version to setup. Default is 8.x.')
@click.option('--folder', default='laravel', help='Folder name for the new Laravel project. Default is "laravel".')
def new(version, folder):
    """Create new Laravel project."""
    create_new_laravel_project(version, folder)


def create_new_laravel_project(version, folder):
    console.print(f"[bold blue]Installing Laravel {version} in folder {folder}...[/bold blue]")
    try:
        subprocess.run(['composer', 'create-project', f'laravel/laravel={version}', folder], check=True)
        click.echo(f"Successfully set up Laravel {version} in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred setting up Laravel: {e}", err=True)


@laravel.command()
@click.argument('command')
def artisan(command):
    """Run Artisan command."""
    try:
        subprocess.run(['php', 'artisan', command], check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred running Artisan command: {e}", err=True)


if __name__ == '__main__':
    laravel()
