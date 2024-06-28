import os

import yaml


def create_directory(directory):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False


def create_file(filepath, content=""):
    """Create a file with the given content if it does not exist."""
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write(content)
        return True
    return False


def load_yaml(filepath):
    """Load a YAML file."""
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    return {}


def save_yaml(filepath, data):
    """Save data to a YAML file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as file:
        yaml.safe_dump(data, file)


def load_config():
    # Define config paths
    paths = [
        os.path.join(os.path.dirname(__file__), '..', 'config'),  # Lowest priority without extension
        os.path.expanduser('~/.alt/config'),  # Middle priority without extension
        os.path.join(os.getcwd(), '.alt', 'config')  # Highest priority without extension
    ]
    config = {}
    for base_path in paths:
        for ext in ['.yaml', '.yml']:
            path = base_path + ext
            if os.path.exists(path):
                new_config = load_yaml(path)
                config.update(new_config or {})
    return config

