import platform
import subprocess

def is_php_installed():
    """Check if PHP is installed."""
    try:
        result = subprocess.run(["php", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_php(version="latest"):
    """Install PHP depending on the platform, with an optional version."""
    try:
        os_name = platform.system().lower()
        if 'darwin' in os_name:
            if version == "latest":
                subprocess.run(["brew", "install", "php"], check=True)
            else:
                subprocess.run(["brew", "install", f"php@{version}"], check=True)
        elif 'linux' in os_name:
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            if version == "latest":
                subprocess.run(["sudo", "apt-get", "install", "-y", "php"], check=True)
            else:
                subprocess.run(["sudo", "apt-get", "install", "-y", f"php{version}"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install PHP: {e}")
        return False

def is_php_extension_installed(extension_name):
    """Check if a PHP extension is installed."""
    try:
        result = subprocess.run(["php", "-m"], capture_output=True, text=True)
        installed_extensions = result.stdout.split()
        return extension_name in installed_extensions
    except subprocess.CalledProcessError as e:
        print(f"Failed to check PHP extension {extension_name}: {e}")
        return False

def install_php_extension(extension_name):
    """Install a PHP extension depending on the platform."""
    try:
        os_name = platform.system().lower()
        if 'darwin' in os_name:
            subprocess.run(["brew", "install", f"php-{extension_name}"], check=True)
        elif 'linux' in os_name:
            subprocess.run(["sudo", "apt-get", "install", "-y", f"php-{extension_name}"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install PHP extension {extension_name}: {e}")
        return False

def ensure_php_installed():
    """Ensure PHP is installed."""
    if not is_php_installed():
        print("PHP is not installed. Installing now...")
        if install_php():
            print("PHP installed successfully.")
        else:
            print("Failed to install PHP.")
    else:
        print("PHP is already installed.")

def ensure_php_extension_installed(extension_name):
    """Ensure PHP extension is installed; install if it's not."""
    if not is_php_extension_installed(extension_name):
        print(f"PHP extension {extension_name} is not installed. Installing now...")
        if install_php_extension(extension_name):
            print(f"PHP extension {extension_name} installed successfully.")
        else:
            print(f"Failed to install PHP extension {extension_name}.")
    else:
        print(f"PHP extension {extension_name} is already installed.")