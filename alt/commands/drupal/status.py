import click
from rich.console import Console
import subprocess
import os
from .helpers import check_drush_availability

console = Console()
drush = check_drush_availability()

@click.command()
@click.option('--working-dir', default=os.getcwd(), help='Working directory for the Drupal project.')
def status_command(working_dir):
    """Get Drupal site status using Drush."""
    if drush:
        try:
            # Save the current directory
            original_cwd = os.getcwd()
            
            # Change to the specified working directory
            os.chdir(working_dir)
            console.print(f"[green]Running {' '.join(drush)} status in {working_dir}[/green]")
            subprocess.run(drush + ['status'], check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Failed to get status: {e}", err=True)
        finally:
            # Change back to the original directory
            os.chdir(original_cwd)
    else:
        console.print("[bold red]Drush is not available. Please ensure Drush is installed and available in your PATH.[/bold red]")

if __name__ == '__main__':
    status_command()
