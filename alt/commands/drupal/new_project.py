import click
from rich.console import Console
import subprocess

console = Console()

@click.command()
@click.option('--version', default='10.3', help='Drupal version to set up. Default is 10.3.')
@click.option('--folder', default='drupal', help='Folder name for the new Drupal project. Default is "drupal".')
def drupal_project_command(version, folder):
    """Create new Drupal Project"""
    click.echo(f"Starting new Drupal {version} project")
    create_new_drupal(version, folder)

@click.command()
@click.option('--version', default='10.3', help='Drupal version to set up. Default is 10.3.')
@click.option('--folder', default='drupal', help='Folder name for the new Drupal project. Default is "drupal".')
def new_command(version, folder):
    """Create new Drupal Project"""
    click.echo(f"Starting new Drupal {version} project")
    create_new_drupal(version, folder)

def create_new_drupal(version, folder):
    console.print(f"[bold blue]Installing Drupal {version}...[/bold blue]")
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
        click.echo(f"Error occurred while setting up Drupal: {e}", err=True)
        return

    # Change directory to the new project folder
    import os
    os.chdir(folder)

    # Additional setup steps can go here, e.g., initializing git, setting up environment files, etc.
    console.print(f"[bold blue]Additional setup steps can be added here if needed.[/bold blue]")
