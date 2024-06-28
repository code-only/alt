import os

import click
import yaml
from rich.console import Console

import alt
from alt.helpers import load_custom_commands, load_config
from alt.commands import *

console = Console()
config = load_config()


@click.group()
def cli():
    banner = f"""[bold yellow]
     █████╗ ██╗  ████████╗
    ██╔══██╗██║  ╚══██╔══╝
    ███████║██║     ██║   
    ██╔══██║██║     ██║   
    ██║  ██║███████╗██║   
    ╚═╝  ╚═╝╚══════╝╚═╝ 
    [/bold yellow]"""

    console.print(banner)
    console.print(f"[bold yellow]    Advanced Local Toolkit![/bold yellow]")
    pass


commands = [
    ('drupal', True),
    ('wordpress', True),
    ('laravel', True),
    ('magento', False),
    ('acquia', True)
]

cli.add_command(alt.commands.command)

# Conditional command group registration based on config
for command, default_enabled in commands:
    if config.get('enabled_commands', {}).get(command, default_enabled):
        cli.add_command(locals()[command])

if config.get('enabled_commands', {}).get('custom', True):  # Default to True
    load_custom_commands(cli, os.path.expanduser('~'))
    load_custom_commands(cli)

if __name__ == '__main__':
    cli()
