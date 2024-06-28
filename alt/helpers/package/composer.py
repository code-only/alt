import json
import os
import re
import subprocess

import click


def is_composer_installed():
    """Check if Composer is installed."""
    try:
        result = subprocess.run(["composer", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def install_composer():
    """Install Composer globally."""
    install_script_url = "https://getcomposer.org/installer"
    try:
        # Download the installer script
        subprocess.run(["php", "-r", f"copy('{install_script_url}', 'composer-setup.php');"], check=True)
        # Run the installer script
        subprocess.run(["php", "composer-setup.php"], check=True)
        # Move Composer to a global location
        subprocess.run(["php", "-r", "unlink('composer-setup.php');"], check=True)
        subprocess.run(["mv", "composer.phar", "/usr/local/bin/composer"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to install Composer: {e}")
        return False


def ensure_composer_installed():
    """Ensure Composer is installed; install it if it's not."""
    if not is_composer_installed():
        click.echo("Composer is not installed. Installing now...")
        if install_composer():
            click.echo("Composer installed successfully.")
        else:
            click.echo("Failed to install Composer.")
    else:
        click.echo("Composer is already installed.")


def add_package(package, version=None, with_dependencies=False):
    """Add a Composer package, with option to include a specific version and dependencies."""
    try:
        command = ["composer", "require"]
        if version:
            command.append(f"{package}:{version}")
        else:
            command.append(package)
        if with_dependencies:
            command.append("--with-all-dependencies")

        subprocess.run(command, check=True)
        version_info = f"version: {version}" if version else "latest version"
        click.echo(f"Successfully added package: {package} ({version_info}, with dependencies: {with_dependencies})")
    except subprocess.CalledProcessError as e:
        version_info = f"version: {version}" if version else "latest version"
        click.echo(f"Failed to add package: {package} ({version_info}, with dependencies: {with_dependencies}) - {e}")


def remove_package(package):
    """Remove a Composer package."""
    try:
        command = ["composer", "remove", package]
        subprocess.run(command, check=True)
        click.echo(f"Successfully removed package: {package}")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to remove package: {e}")


def is_package_installed(package):
    """Check if a package is installed."""
    try:
        result = subprocess.run(["composer", "show", package], capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def get_dependencies():
    """Get list of installed packages and their dependencies."""
    try:
        result = subprocess.run(["composer", "show", "-f", "json"], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to get dependencies: {e}")
        return None


def print_dependencies():
    """Print installed packages and their dependencies in a readable format."""
    dependencies = get_dependencies()
    if dependencies is None:
        return

    print("\nInstalled Packages and Dependencies:")
    for package in dependencies.get('installed', []):
        click.echo(f"- {package['name']} ({package['version']})")
        if 'require' in package:
            print("  Dependencies:")
            for dep, version in package['require'].items():
                print(f"    - {dep} ({version})")
        click.echo("\n")


def load_composer_json(filepath='composer.json'):
    """Load composer.json file."""
    if not os.path.exists(filepath):
        click.echo(f"{filepath} does not exist.")
        return None

    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            click.echo(f"Failed to load JSON from {filepath}: {e}")
            return None


def save_composer_json(data, filepath='composer.json'):
    """Save changes to composer.json file."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def add_patch(package, patch_description, patch_url):
    """Add a patch to composer.json."""
    composer_data = load_composer_json()
    if composer_data is None:
        return

    if 'extra' not in composer_data:
        composer_data['extra'] = {}
    if 'patches' not in composer_data['extra']:
        composer_data['extra']['patches'] = {}

    patches_section = composer_data['extra']['patches']

    if patch_exists(patches_section, package, patch_description):
        print(f"Patch already exists for {package} with description: '{patch_description}'")
        return

    if package not in patches_section:
        patches_section[package] = {}

    patches_section[package][patch_description] = patch_url
    composer_data['extra']['patches'] = patches_section
    save_composer_json(composer_data)

    print(f"Added patch for {package}: {patch_description} -> {patch_url}")


def remove_patch(package, patch_url):
    """Remove a patch from composer.json."""
    composer_data = load_composer_json()
    if composer_data is None:
        return
    patches_section = composer_data.get('extra', {}).get('patches', {})
    if package not in patches_section:
        click.echo(f"No patches found for package: {package}")
        return
    initial_length = len(patches_section[package])
    patches_section[package] = [patch for patch in patches_section[package] if patch != patch_url]

    if len(patches_section[package]) == initial_length:
        click.echo(f"No patch with URL: {patch_url} found for package: {package}")
    else:
        if not patches_section[package]:
            del patches_section[package]

        if not patches_section:
            del composer_data['extra']['patches']
        elif 'extra' not in composer_data:
            composer_data['extra'] = {}

        composer_data['extra']['patches'] = patches_section
        save_composer_json(composer_data)
        click.echo(f"Removed patch for {package}.")


def patch_exists(patches_section, package, patch_description):
    """Check if a patch already exists for a package."""
    if package in patches_section and patch_description in patches_section[package]:
        return True
    return False


def is_patch_installed(package, patch_url):
    """Verify if a patch is already installed."""
    composer_data = load_composer_json()
    if composer_data is None:
        return False

    patches_section = composer_data.get('extra', {}).get('patches', {})
    if package in patches_section:
        for patch in patches_section[package]:
            print(patch)
            print(patch_url)
            if patch == patch_url:
                return True
    return False


def is_valid_package(package):
    """Check if the given package name is valid."""
    # Basic pattern to match composer package names, which are usually in the form 'vendor/package'
    pattern = r'^[a-z0-9\-]+/[a-z0-9\-]+$'
    return re.match(pattern, package) is not None


def update_lock():
    """Update the Composer lock file."""
    try:
        # Run the 'composer update' command to refresh the lock file
        result = subprocess.run(["composer", "update", "--lock"], check=True)
        click.echo("Successfully updated the composer.lock file.")
    except subprocess.CalledProcessError as e:
        click.echo(f"Failed to update the composer.lock file: {e}")


# Example usage
if __name__ == "__main__":
    ensure_composer_installed()
    package = "monolog/monolog"
    patch_url = "https://example.com/patch.diff"
    patch_description = "Example patch"

    if is_valid_package(package):
        if not is_patch_installed(package, patch_url):
            add_patch(package, patch_url, patch_description)
            click.echo("Patch added.")
        else:
            remove_patch(package, patch_url)
            click.echo("Patch removed.")
    else:
        click.echo(f"Invalid package name: {package}")
