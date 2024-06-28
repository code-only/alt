import os
import subprocess

import click

from alt.helpers.package import composer


@click.command()
@click.argument('version')
def upgrade(version):
    """Upgrade Drupal core to the specified version."""
    repo_path = os.getcwd()

    def run_command(command, cwd=None):
        """Run a shell command."""
        try:
            subprocess.run(command, check=True, shell=True, cwd=cwd)
        except subprocess.CalledProcessError as e:
            click.echo(f"Command failed: {e}")
            exit(1)

    click.echo("Pulling the latest changes from the Git repository...")
    run_command("git pull", cwd=repo_path)

    click.echo(f"Updating Drupal core to version {version}...")
    if composer.is_package_installed("drupal/core-recommended"):
        composer.add_package("drupal/core-recommended", version, True)
    else:
        composer.add_package("drupal/core", version, True)

    click.echo("Applying database updates...")
    run_command("drush updb -y", cwd=repo_path)

    click.echo("Exporting configuration...")
    run_command("drush config-export -y", cwd=repo_path)

    click.echo("Committing and pushing changes to the Git repository...")
    run_command("git add .", cwd=repo_path)
    run_command(f"git commit -m 'Upgrade Drupal core to version {version}'", cwd=repo_path)
    run_command("git push", cwd=repo_path)

    click.echo("Drupal upgrade completed successfully.")
