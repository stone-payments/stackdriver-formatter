"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages

setup(
    description='Stackdriver Formatter',
    install_requires=['python-json-logger>=0.1.11'],
    long_description=open('README.md').read().strip(),
    name='stackdriver_formatter',
    packages=find_packages(exclude=['tests']),
    py_modules=['stackdriver_formatter'],
    url='https://github.com/stone-payments/stackdriver-formatter',
    version='1.0.1',
)
