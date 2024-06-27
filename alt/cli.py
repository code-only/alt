import os
import sys
import click
import yaml
import subprocess
from rich.console import Console
from alt.commands import *


console = Console()

def load_config():
    # Check for local config file in current directory
    local_config_path = os.path.join(os.getcwd(), '.alt', 'config.yaml')
    default_config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    
    config_path = local_config_path if os.path.exists(local_config_path) else default_config_path
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

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
    ╚═╝  ╚═╝╚══════╝╚═╝ [/bold yellow]"""

    console.print(banner)          
    console.print(f"[bold green]    Advanced Local Toolkit![/bold green]")
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

# Custom command loader
# Scans `.alt/commands` directory for .py or .sh scripts to load as commands.
def load_custom_commands(cli_group):
    custom_command_path = os.path.join(os.getcwd(), '.alt', 'commands')
    if not os.path.exists(custom_command_path):
        return
    
    for filename in os.listdir(custom_command_path):
        if filename.endswith('.py'):
            # Import Python script as module
            command_module = {}
            exec(open(os.path.join(custom_command_path, filename)).read(), command_module)
            cli_group.add_command(command_module[filename[:-3]])
        elif filename.endswith('.sh'):
            command_name = filename[:-3]
            
            @cli.command(name=command_name)
            @click.pass_context
            def shell_command(ctx, cmd_name=command_name):
                """Run custom shell command."""
                result = subprocess.run([os.path.join(custom_command_path, f"{cmd_name}.sh")], shell=True)
                if result.returncode != 0:
                    click.echo(f'{cmd_name} failed.')
                else:
                    click.echo(f'{cmd_name} executed successfully.')

if config.get('enabled_commands', {}).get('custom', True):  # Default to True
    load_custom_commands(cli)

if __name__ == '__main__':
    cli('--help'.split())