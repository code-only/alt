import subprocess

import click
from alt.helpers.package import composer

@click.command()
@click.argument('machinename')
def local_sync_command(machinename):
    """Sync local environment with Acquia environment specified by MACHINENAME."""
    click.echo(f"Syncing local environment with Acquia environment '{machinename}'...")
    try:
        # Example sync command; replace with actual sync instructions
        #subprocess.run(["bash", "sync-environment.sh", machinename], check=True)
        composer.is_package_installed('drupal/acsf')
        #TODO: Check if it is ACSF or ACE

        #TODO: Read the alias.

        #TODO: Check if DB is available.

        #TODO: Run drush sql:sync @alias @self -machinename
        click.echo(f"Local environment synced with Acquia environment '{machinename}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to sync environment: {e}", err=True)


if __name__ == '__main__':
    local_sync_command()
