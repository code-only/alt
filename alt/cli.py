import os
import sys
import click
import yaml
import subprocess
from rich.console import Console
from alt.commands.drupal import drupal
from alt.commands.wordpress import wordpress
#from .commands.groups import groups
from alt.commands.groups.new import new

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
    console.print(f"[bold green]Advanced Local development Tool![/bold green]")
    pass

cli.add_command(new)

# Conditional command group registration based on config
if config.get('enabled_commands', {}).get('drupal', True):  # Default to True
    cli.add_command(drupal)

if config.get('enabled_commands', {}).get('wordpress', False):
    cli.add_command(wordpress)

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