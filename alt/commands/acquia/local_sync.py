import click
import subprocess

@click.command()
@click.argument('machinename')
def local_sync_command(machinename):
    """Sync local environment with Acquia environment specified by MACHINENAME."""
    click.echo(f"Syncing local environment with Acquia environment '{machinename}'...")
    try:
        # Example sync command; replace with actual sync instructions
        subprocess.run(["bash", "sync-environment.sh", machinename], check=True)
        click.echo(f"Local environment synced with Acquia environment '{machinename}' successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to sync environment: {e}", err=True)

if __name__ == '__main__':
    local_sync_command()
 