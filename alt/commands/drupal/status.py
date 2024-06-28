import click
from rich.console import Console
import subprocess
import os
from .helpers import check_drush_availability

console = Console()

@click.command()
@click.argument('drupal_path', type=click.Path(exists=True))
def status_command(drupal_path = os.getcwd()):
    """Get Drupal site status using Drush.
    
    DRUPAL_PATH   Absolute path to Drupal directory if it is not current directory.
    """
    if not os.path.exists(drupal_path):
        console.print(f"[red]Dir {drupal_path} not found.[/red ]")
        return
    drush = check_drush_availability(drupal_path)
    if drush:
        try:
            # Save the current directory
            original_cwd = os.getcwd()
            # Change to the specified working directory
            os.chdir(drupal_path)
            console.print(f"[green]Running {' '.join(drush)} status in {drupal_path}[/green]")
            subprocess.run(drush + ['status'], check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Failed to get status: {e}", err=True)
        finally:
            # Change back to the original directory
            os.chdir(original_cwd)
    else:
        console.print("[bold red]Please ensure Drush is installed and available in your PATH.[/bold red]")

if __name__ == '__main__':
    status_command()
