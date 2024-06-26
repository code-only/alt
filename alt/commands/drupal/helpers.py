import os
import subprocess

from rich.console import Console

console = Console()


def check_drush_availability(cwd=os.getcwd(), environment=None):
    """Check if drush is available as a CLI command."""
    try:
        # Check if drush works directly
        os.chdir(cwd)
        subprocess.run(['drush', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return ['drush']
    except (subprocess.CalledProcessError, FileNotFoundError):
        # If direct drush command is not available, check for the alias
        if os.path.exists('vendor/bin/drush'):
            return ['php', 'vendor/bin/drush']
        else:
            console.print("[bold red]Drush is not available.[/bold red]")
            return None
