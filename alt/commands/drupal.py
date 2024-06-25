import click
from .groups.new import new
from rich.console import Console
import subprocess
import os

console = Console()

@click.group()
def drupal():
    """Commands related to Drupal CMS."""
    pass

@drupal.command()
def cache_clear():
    """Clear Drupal cache."""
    click.echo('Drupal cache cleared.')


@new.command()
@click.option('--version', default='10.3', help='Drupal version to setup. Default is 10.3.')
@click.option('--folder', default='drupal', help='Folder name for the new Drupal project. Default is "drupal".')
def drupal_project(version, folder):
    """Create new Drupal Project"""
    click.echo("Starting new Drupal 10.3 project")
    create_new_drupal(version, folder)


@drupal.command()
@click.option('--version', default='10.3', help='Drupal version to setup. Default is 10.3.')
@click.option('--folder', default='drupal', help='Folder name for the new Drupal project. Default is "drupal".')
def new(version, folder):
    """Create new Drupal Project"""
    click.echo("Starting new Drupal 10.3 project")
    create_new_drupal(version, folder)

def create_new_drupal(version, folder):
    console.print(f"[bold blue]Installing Drupal ...[/bold blue]")
    # Compose the Composer create-project command
    composer_command = [
        'composer', 'create-project', f'drupal/recommended-project:{version}', folder
    ]

    # Execute the Composer command
    try:
        click.echo(f"Running command: {' '.join(composer_command)}")
        subprocess.run(composer_command, check=True)
        click.echo(f"Successfully set up Drupal {version} in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred setting up Drupal: {e}", err=True)
        return

    # Change directory to the new project folder
    os.chdir(folder)

    # Additional setup steps can go here, e.g., initializing git, setting up environment files, etc.
    click.echo("Additional setup steps can be added here if needed.")


@drupal.command()
def report():
    """Provide Drupal Project Report."""