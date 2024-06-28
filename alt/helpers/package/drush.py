import subprocess


def run_drush_command(site_url, command, *args):
    """
    Run a Drush command with a site alias based on the provided site URL.

    :param site_url: The site URL used to construct the Drush alias.
    :param command: The Drush command to run.
    :param args: Additional arguments for the Drush command.
    :return: The output of the Drush command.
    """
    # Construct site alias
    site_alias = f"@{site_url.replace('https://', '').replace('http://', '').replace('/', '_')}"

    # Construct full Drush command
    drush_command = ["drush", site_alias, command] + list(args)

    try:
        # Execute command
        result = subprocess.run(drush_command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(drush_command)}' failed with error: {e.stderr}")
        return None


def drush_cache_clear(site_url):
    """
    Clears the cache on the specified Drupal site.

    :param site_url: The site URL used to construct the Drush alias.
    """
    return run_drush_command(site_url, 'cr')


def drush_config_export(site_url):
    """
    Exports the configuration from the specified Drupal site.

    :param site_url: The site URL used to construct the Drush alias.
    """
    return run_drush_command(site_url, 'config-export', '-y')


def drush_config_import(site_url):
    """
    Imports the configuration to the specified Drupal site.

    :param site_url: The site URL used to construct the Drush alias.
    """
    return run_drush_command(site_url, 'config-import', '-y')


def drush_database_update(site_url):
    """
    Applies database updates to the specified Drupal site.

    :param site_url: The site URL used to construct the Drush alias.
    """
    return run_drush_command(site_url, 'updb', '-y')
