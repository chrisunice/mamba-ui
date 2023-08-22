from setuptools import setup, find_packages

# Get required packages for the project
with open(r'.\requirements.txt') as f:
    lines = f.read().splitlines()
required_packages = [line for line in lines if not line.startswith('#') and not line == '']

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
