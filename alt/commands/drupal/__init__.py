import click
from rich.console import Console
#from .cache_clear import cache_clear_command
from .new_project import new_command, drupal_project_command
from .status import status_command
from .helpers import check_drush_availability

console = Console()

@click.group()
def drupal():
    """Commands related to Drupal CMS."""
    pass

#drupal.add_command(cache_clear_command, "cache-clear")
drupal.add_command(status_command, "status")
drupal.add_command(new_command, "new")
#drupal.add_command(drupal_project_command, "drupal-project")

# Check for drush availability and set the drush variable
drush = check_drush_availability()
