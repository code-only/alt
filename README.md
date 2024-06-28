# ALT: Advanced Local Toolkit

ALT (Advanced Local Toolkit) is a powerful tool that streamlines local development workflows by providing an easy-to-use
CLI for managing projects, especially for Drupal. It offers configurable command registration and supports custom
command additions.

## Features

- **Drupal Commands**: Set up and manage Drupal projects effortlessly.
- **WordPress Commands**: Integrate WordPress management (optional).
- **Custom Command Loader**: Load custom commands from `.py` or `.sh` scripts.
- **Configuration Based**: Enable or disable commands through a configuration file.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Ensure that you have Python installed, and optionally ensure Composer is available for Drupal commands.

3. Install required Python packages (if there are any dependencies):

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

ALT uses a configuration file to determine which command groups are enabled. The configuration file should be in YAML
format and located at `.alt/config.yaml` in your project directory. Alternatively, a default configuration can be placed
in `config.yaml` at the root of the repository.

Example configuration:

```yaml
enabled_commands:
  drupal: true
  wordpress: false
  custom: true
```

In this configuration:

- The Drupal commands are enabled.
- The WordPress commands are disabled.
- Custom commands (from the `.alt/commands` directory) are enabled.

## Usage

### Running the CLI

To run the CLI and see the available commands, execute:

```bash
python alt/cli.py --help
```

This shows the top-level commands and options available.

### Drupal Commands

If enabled, the Drupal command group provides a set of commands to manage your Drupal projects.

1. **Setup a New Drupal Project**

    ```bash
    python alt/cli.py drupal new --version 10.3 --folder my_drupal_project
    ```

   This command sets up a new Drupal project with the specified version and folder name.

2. **Clear Drupal Cache**

    ```bash
    python alt/cli.py drupal cache_clear
    ```

   This command clears the Drupal cache.

3. **Drupal Project Report**

    ```bash
    python alt/cli.py drupal report
    ```

   This command provides a report on the Drupal project.

### Custom Commands

You can add custom commands by placing `.py` or `.sh` scripts in the `.alt/commands` directory.

#### Example: Python Custom Command

Create a file `.alt/commands/custom_command.py` with the following content:

```python
@click.command()
def custom_command():
    click.echo("Running custom Python command.")
```

#### Example: Shell Custom Command

Create a file `.alt/commands/custom_script.sh` with the following content:

```bash
#!/bin/bash
echo "Running custom shell command."
```

Make sure the shell script is executable:

```bash
chmod +x .alt/commands/custom_script.sh
```

These commands can then be invoked through the CLI:

```bash
python alt/cli.py custom_command
python alt/cli.py custom_script
```

## Example Project Structure

A typical project structure using ALT might look like this:

```
your_project/
│
├── .alt/
│   ├── commands/
│   │   ├── custom_command.py
│   │   └── custom_script.sh
│   └── config.yaml
├── commands/
│   ├── __init__.py
│   └── groups/
│       ├── __init__.py
│       └── new.py
├── alt/
│   ├── __init__.py
│   ├── cli.py
│   └── commands/
│       ├── __init__.py
│       ├── drupal.py
│       └── wordpress.py
├── config.yaml
├── README.md
└── requirements.txt
```

## Further Development

Feel free to add more commands or edit the existing ones based on your needs. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or suggestions, please feel free to open an issue or contact the maintainers.

Enjoy using ALT for an enhanced local development experience!