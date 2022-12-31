from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

# Get required packages for the project
required_packages = [str(req.requirement) for req in parse_requirements('./requirements.txt', session='')]

setup(
    name='mamba-ui',
    version='1.0.0',
    author='Chris Unice',
    author_email='cunice@denmartech.com',
    packages=find_packages(include=['mamba_ui', 'mamba_ui.*']),
    url='http://pypi.python.org/pypi/mamba-ui/',
    description='Mamba User Interface',
    long_description='',
    install_requires=required_packages,
    include_package_data=True
)
