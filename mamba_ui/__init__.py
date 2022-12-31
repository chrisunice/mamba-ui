import os
from configparser import ConfigParser

config = ConfigParser()
config.read(f"{os.path.dirname(__file__)}\\config.ini")

PKG_DIR = os.path.dirname(__file__)
STANDARD_WIDTH = int(config['window']['standard_width'])
STANDARD_HEIGHT = int(config['window']['standard_height'])

from mamba_ui.app import app
from mamba_ui.layout import serve_layout

from mamba_ui import components
from mamba_ui import pages

