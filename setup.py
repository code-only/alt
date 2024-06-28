# setup.py
import os
import sys

from setuptools import setup, find_packages

# Explicitly add the current directory to the sys.path to ensure custom install command is found
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from post_install import CustomInstallCommand

setup(
    name='alt-cli',
    version='0.3',
    packages=find_packages(include=['alt', 'alt.*']),
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'alt=alt.cli:cli',
        ]
    },
    cmdclass={
        'install': CustomInstallCommand,
    },
)
