import subprocess
import click
import os

from alt.helpers.package import composer, php


@click.command()
@click.argument('folder', required=False, default='drupal')
@click.option('--version', default='10.3', help='Drupal version to set up. Default is 10.3.')
def new_command(version, folder):
    """Create new Drupal Project"""
    click.echo(f"Starting new Drupal {version} project")
    create_new_drupal(version, folder)


def create_new_drupal(version, folder):
    composer.ensure_composer_installed()

    # Ensure PHP is installed before proceeding
    php.ensure_php_installed()

    click.echo(f"Installing Drupal {version}...")
    # Compose the Composer create-project command
    composer_command = [
        'composer', 'create-project', '--no-install', f'drupal/recommended-project:{version}', folder
    ]

    # Execute the Composer command
    try:
        click.echo(f"Running command: {' '.join(composer_command)}")
        subprocess.run(composer_command, check=True)

        # Change directory to the new project folder
        os.chdir(os.path.join(os.getcwd(), folder))
        # Run the command to check platform requirements and get the result in JSON format
        composer.install_missing_requirements()
        subprocess.run(['composer', 'install'], check=True)
        click.echo(f"Successfully set up Drupal {version} in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred while setting up Drupal: {e}", err=True)
        return

    # Additional setup steps can go here, e.g., initializing git, setting up environment files, etc.
    click.echo(f"Additional setup steps can be added here if needed.")