# post_install.p
import os

from setuptools.command.install import install


class CustomInstallCommand(install):
    """Customized setuptools install command to run post installation scripts."""

    def run(self):
        print("[cyan]Running custom install command...[/cyan]")
        self.execute_post_install()

    def execute_post_install(self):
        # Your custom post-install actions here
        print("[cyan]Executing post-install setup for alt-cli...[/cyan]")

        # For example, you could initialize a configuration file
        config_path = os.path.join(os.path.expanduser('~'), '.alt', 'config.yaml')
        if not os.path.exists(config_path):
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, 'w') as f:
                f.write('enabled_commands:\n  drupal: true\n  wordpress: false\n  custom: true\n')
            print(f"[green]Created default configuration at {config_path}[/green]")
        else:
            print(f"[blue].alt configuration already exists.[/blue]")
