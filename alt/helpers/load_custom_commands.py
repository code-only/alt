import os
import click
from rich.console import Console
import subprocess

console = Console()

# Custom command loader
# Scans `.alt/commands` directory for .py or .sh scripts to load as commands.
def load_custom_commands(cli_group, cwd=os.getcwd()):
    custom_command_path = os.path.join(cwd, '.alt', 'commands')
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
            @cli_group.command(name=command_name)
            @click.pass_context
            @click.argument('params', nargs=-1)
            def shell_command(ctx, params, cmd_name=command_name):
                """Run custom shell command: {cmd_name}.""".format(cmd_name=cmd_name)
                result = subprocess.run([os.path.join(custom_command_path, f"{cmd_name}.sh")] + list(params), shell=True)
                if result.returncode != 0:
                    click.echo(f'{cmd_name} failed.')
                else:
                    click.echo(f'{cmd_name} executed successfully.')
            #cli_group.add_command(command_name)
