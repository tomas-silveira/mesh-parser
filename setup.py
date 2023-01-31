from setuptools import find_packages, setup

setup(
    name='meshparser',
    version='0.1.0',
    description='A simple parser for mesh files to work with CSD',
    packages=find_packages(include=['meshparser']),
    author='Tomas Silveira',
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)
