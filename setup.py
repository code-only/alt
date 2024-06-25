from setuptools import setup, find_packages

setup(
    name='alt-cli',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        alt=alt.cli:cli
    ''',
)