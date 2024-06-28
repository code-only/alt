import os

import click
import yaml
import alt.helpers.common as common

CONFIG_PATH = os.path.expanduser('~/.alt/config.yaml')


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f) or {}

@click.group()
def command():
    """Manage commands"""
    pass


@command.command()
@click.argument('cmd')
def enable(cmd):
    """Enable a command"""
    config = load_config()
    config.setdefault('enabled_commands', {})
    config['enabled_commands'][cmd] = True
    common.save_yaml(CONFIG_PATH, config)
    click.echo(f"Enabled command: {cmd}")

@command.command()
@click.argument('cmd')
def disable(cmd):
    """Disable a command"""
    config = load_config()
    if 'enabled_commands' in config and cmd in config['enabled_commands']:
        config['enabled_commands'][cmd] = False
    common.save_yaml(CONFIG_PATH, config)
    click.echo(f"Disabled command: {cmd}")


if __name__ == '__main__':
    command()
