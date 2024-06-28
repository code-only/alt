import os
import sys
import click
import yaml
import subprocess
from rich.console import Console
from alt.commands import *
from alt.helpers import load_custom_commands

console = Console()

def load_config():
    # Define config paths
    paths = [
        os.path.join(os.path.dirname(__file__), '..', 'config'),  # Lowest priority without extension
        os.path.expanduser('~/.alt/config'),            # Middle priority without extension
        os.path.join(os.getcwd(), '.alt', 'config')     # Highest priority without extension
    ]
    
    config = {}
    for base_path in paths:
        for ext in ['.yaml', '.yml']:
            path = base_path + ext
            if os.path.exists(path):
                with open(path, 'r') as f:
                    new_config = yaml.safe_load(f)
                    config.update(new_config or {})
                    print(config)
    return config

# Load user configuration
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
    ('wordpress', False),
    ('laravel', True),
    ('magento', False),
    ('acquia', True)
]

# Conditional command group registration based on config
for command, default_enabled in commands:
    if config.get('enabled_commands', {}).get(command, default_enabled):
        cli.add_command(locals()[command])

if config.get('enabled_commands', {}).get('custom', True):  # Default to True
    load_custom_commands(cli, os.path.expanduser('~'))
    load_custom_commands(cli)

if __name__ == '__main__':
    cli()