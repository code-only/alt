import pytest
from click.testing import CliRunner
from unittest.mock import patch
import subprocess
import os

from alt.commands.drupal import drupal

@pytest.fixture
def runner():
    return CliRunner()

def test_cache_clear(runner):
    result = runner.invoke(drupal, ['cache_clear'])
    assert result.exit_code == 0
    assert 'Drupal cache cleared.' in result.output

@patch('alt.commands.drupal.subprocess.run')
@patch('os.chdir')
def test_create_new_drupal(mock_chdir, mock_run, runner):
    mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0)
    result = runner.invoke(drupal, ['new', '--version', '9.3.0', '--folder', 'mydrupal'])
    assert result.exit_code == 0
    assert 'Starting new Drupal 9.3.0 project in folder mydrupal' in result.output
