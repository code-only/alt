import os
from click.testing import CliRunner
import pytest
import shutil

from alt.cli import cli

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def mock_config():
    os.makedirs('.alt', exist_ok=True)
    with open('.alt/config.yaml', 'w') as file:
        file.write("""
enabled_commands:
  drupal: true
  wordpress: false
  custom: true
        """)
    yield
    shutil.rmtree('.alt')

def test_cli_help(runner, mock_config):
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Advanced Local development Tool!' in result.output

def test_drupal_command_is_loaded(runner, mock_config):
    result = runner.invoke(cli, ['drupal', '--help'])
    assert result.exit_code == 0
    assert 'Commands related to Drupal CMS' in result.output

def test_wordpress_command_is_not_loaded(runner, mock_config):
    result = runner.invoke(cli, ['wordpress', '--help'])
    assert result.exit_code == 2  # Error code for command not found

def test_custom_command_loading(runner, mock_config):
    os.makedirs('.alt/commands', exist_ok=True)
    with open('.alt/commands/custom_command.py', 'w') as file:
        file.write("""
import click

@click.command()
def custom_command():
    click.echo('Running custom command.')
""")
    result = runner.invoke(cli, ['custom_command'])
    assert result.exit_code == 0
    assert 'Running custom command.' in result.output

def test_custom_shell_command_loading(runner, mock_config):
    os.makedirs('.alt/commands', exist_ok=True)
    with open('.alt/commands/custom_script.sh', 'w') as file:
        file.write("""
#!/bin/bash
echo "Running custom shell script."
""")
    os.chmod('.alt/commands/custom_script.sh', 0o755)
    result = runner.invoke(cli, ['custom_script'])
    assert result.exit_code == 0
    assert 'Running custom shell script.' in result.output
