# Import the click module
import click

# Define the command using the click.command decorator
@click.command()
@click.option('--name', default='World', help='Name of the person to greet.')
@click.option('--greeting', default='Hello', help='Greeting message to use.')
def greet(name, greeting):
    """A custom command that greets the user."""
    click.echo(f'{greeting}, {name}!')

# Make sure the function is referenced to be picked up by the command loader
if __name__ == "__main__":
    greet()