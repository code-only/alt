import os
import subprocess
from rich.console import Console

console = Console()

def check_environment_availability(command, cwd=os.getcwd()):
    """Check if command is available in the current directory or given cwd."""
    command_path = os.path.join(cwd, command)
    
    if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
        return [command_path]
    
    try:
        # Check if command works directly
        subprocess.run([command, '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return [command]
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print(f"[bold red]{command} is not available.[/bold red]")
        return None