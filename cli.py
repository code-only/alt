import os
import click
import subprocess
import importlib.util
from rich.console import Console
from rich.table import Table

COMMANDS_DIR = os.path.join(os.path.dirname(__file__), 'commands')
console = Console()

@click.group()
def cmd():
    """ALT: A CLI tool for local development"""
    pass

@cmd.command()
@click.argument('name')
def hello(name):
    """Say hello to NAME."""
    console.print(f"[bold green]Hello, {name}![/bold green]")

def load_additional_commands():
    for filename in os.listdir(COMMANDS_DIR):
        file_path = os.path.join(COMMANDS_DIR, filename)
        if filename.endswith('.py') and filename != '__init__.py':
            command_name = filename[:-3]
            cmd.add_command(create_python_command(command_name, file_path))
        elif os.access(file_path, os.X_OK) and filename.endswith('.sh'):
            command_name = os.path.splitext(filename)[0]
            cmd.add_command(create_shell_command(command_name, file_path))

def create_python_command(name, file_path):
    @click.command(name)
    @click.argument('args', nargs=-1)
    def command(args):
        spec = importlib.util.spec_from_file_location(name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.run(args)
    return command

def create_shell_command(name, file_path):
    @click.command(name)
    @click.argument('args', nargs=-1)
    def command(args):
        cmd = [file_path] + list(args)
        subprocess.run(cmd, check=True)
    return command

load_additional_commands()

if __name__ == '__main__':
    cmd()