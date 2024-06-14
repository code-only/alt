from setuptools import setup, find_packages

setup(
    name='alt',
    version='0.1.0',
    author='Aman Srivastava',
    author_email='credevator@outlook.com',
    description='A CLI tool for local development',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/code-only/alt',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'alt=cli:cmd',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
