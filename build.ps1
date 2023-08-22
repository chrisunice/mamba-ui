# Simulating network drive
# This is necessary only on the unclass side
subst U: C:\VaultNet\

# Update project environment
.\update.ps1

# Download requirements from internet
pip download -r .\requirements.txt --dest U:\PyPI

# Build mamba-ui
python setup.py bdist_wheel --dist-dir U:\PyPI

# remove some of the junk files
Remove-Item .\build\ -r -Force
Remove-Item .\*.egg-info -r -Force
Remove-Item .\*.pytest_cache -r -Force
