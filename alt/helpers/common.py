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
    with open(filepath, 'w') as file:
        yaml.safe_dump(data, file)
