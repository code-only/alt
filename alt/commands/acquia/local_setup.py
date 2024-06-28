import subprocess

import click


@click.command()
def local_setup_command():
    """Set up local Acquia environment."""
    click.echo("Setting up local Acquia environment...")
    try:
        # Example setup command; replace with actual setup instructions
        subprocess.run(["bash", "setup-local-environment.sh"], check=True)
        click.echo("Local Acquia environment setup completed successfully.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to set up local environment: {e}", err=True)


if __name__ == "__main__":
    local_setup_command()
