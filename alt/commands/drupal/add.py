import subprocess

import click

from alt.helpers.package import composer


@click.group()
def add():
    pass


@add.command()
@click.argument('module_names', nargs=-1)
@click.option('--with-dependencies', is_flag=True, default=False, help='Install modules with dependencies')
def module(module_names, with_dependencies):
    """Install Drupal modules using Composer."""

    if not module_names:
        click.echo("No module names provided. Please specify at least one module to install.")
        return

    module_names = [
        f'drupal/{name}' if '/' not in name else name
        for name in module_names
    ]

    for module_name in module_names:
        click.echo(f"Installing Drupal module: {module_name}...")
        try:
            composer.add_package(module_name, with_dependencies=with_dependencies)
        except subprocess.CalledProcessError:
            click.echo(f"Failed to install module: {module_name}", err=True)
    """Install Drupal modules using Composer."""

    if not module_names:
        click.echo("No module names provided. Please specify at least one module to install.")
        return

    module_names = [
        f'drupal/{name}' if '/' not in name else name
        for name in module_names
    ]

    for module_name in module_names:
        click.echo(f"Installing Drupal module: {module_name}...")
        try:
            composer.add_package(module_name)
        except subprocess.CalledProcessError:
            click.echo(f"Failed to install module: {module_name}", err=True)


@add.command()
@click.argument('package')
@click.argument('patch')
@click.argument('description')
def patch(package, patch, description):
    """Install Drupal patch using Composer.
    
    PACKAGE        Composer package name.  
    PATCH          URL or path to patch.
    DESCRIPTION    Patch Description.
    """
    if not composer.is_valid_package(package):
        click.echo(f"{package} is not a valid package.")
        return
    """Add a patch to a Composer package."""
    # Validate that patch and description arguments are not empty
    if not patch or not description:
        click.echo("Both patch and description are required.")
        return

    if composer.is_patch_installed(package, patch):
        click.echo("Patch already added.")
        return

    """Install Patch"""
    if not composer.is_package_installed("cweagans/composer-patches"):
        composer.add_package("cweagans/composer-patches", "~1.0", with_dependencies=True)
    try:
        composer.add_patch(package, description, patch)
        composer.update_lock()
    except subprocess.CalledProcessError:
        click.echo(f"Failed to add patch in: {package}", err=True)


if __name__ == '__main__':
    add()
    """Install Patch"""
    if not composer.is_package_installed("cweagans/composer-patches"):
        composer.add_package("cweagans/composer-patches", "~1.0", True)
    try:
        composer.add_patch(package, patch, description)
    except subprocess.CalledProcessError:
        click.echo(f"Failed to add patch in: {package}", err=True)

import datetime


def some_example():
    """Print today's date, time, and year."""

    # Get the current date and time
    now = datetime.datetime.now()

    # Extract the date, time, and year
    current_date = now.date()
    current_time = now.time()
    current_year = now.year

    # Print the date, time, and year
    print(f"Today's date: {current_date}")
    print(f"Current time: {current_time}")
    print(f"Current year: {current_year}")


if __name__ == '__main__':
    add()
