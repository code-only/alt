import subprocess
import click
import os
from rich.console import Console

console = Console()

def run_local_command(command, description):
    """
    Helper function to run a shell command with error handling.

    :param command: List of command arguments.
    :param description: Description of the command being run.
    """
    click.echo(f"{description}...")
    try:
        os.chdir(os.getcwd())
        subprocess.run(command, check=True)
        click.echo(f"{description} completed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to {description.lower()}: {e}", err=True)


if __name__ == '__main__':
    cli()
