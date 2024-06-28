import click

from .local_reset import local_reset_command
from .local_setup import local_setup_command
from .local_sync import local_sync_command


@click.group()
def acquia():
    """Commands related to Acquia local setup and management."""
    pass


acquia.add_command(local_setup_command, "local:setup")
acquia.add_command(local_sync_command, "local:sync")
acquia.add_command(local_reset_command, "local:reset")
