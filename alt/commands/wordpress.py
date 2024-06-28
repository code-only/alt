import shutil
import subprocess

import click
from rich.console import Console

console = Console()


@click.group()
def wordpress():
    """Commands related to WordPress CMS."""
    pass


@wordpress.command()
def update_plugins():
    """Update WordPress plugins."""
    click.echo('WordPress plugins updated.')


@wordpress.command()
@click.option('--version', default='latest', help='WordPress version to setup. Default is "latest".')
@click.option('--folder', default='wordpress',
              help='Folder name for the new WordPress project. Default is "wordpress".')
def new(version, folder):
    """Create Wordpress Site."""
    create_new_wordpress(version, folder)


def create_new_wordpress(version, folder):
    console.print(f"[bold blue]Installing WordPress {version}...[/bold blue]")
    wp_cli_url = 'https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar'

    # Check if WP-CLI is installed
    if not shutil.which('wp'):
        console.print("[yellow]WP-CLI not found. Downloading WP-CLI...[/yellow]")
        subprocess.run(['curl', '-O', wp_cli_url])
        subprocess.run(['chmod', '+x', 'wp-cli.phar'])
        subprocess.run(['sudo', 'mv', 'wp-cli.phar', '/usr/local/bin/wp'])

    # Compose the WP-CLI core download command
    wp_command = [
        'wp', 'core', 'download', '--path={}'.format(folder)
    ]

    if version != 'latest':
        wp_command.append(f'--version={version}')

    # Execute the WP-CLI command
    try:
        click.echo(f"Running command: {' '.join(wp_command)}")
        subprocess.run(wp_command, check=True)
        click.echo(f"Successfully set up WordPress {version} in folder '{folder}'")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error occurred setting up WordPress: {e}", err=True)
        return

    # Additional setup steps can go here, e.g., configuring wp-config.php, setting up database, etc.
    click.echo("Additional setup steps can be added here if needed.")
