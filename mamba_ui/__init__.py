import os
import json

PKG_DIR = os.path.dirname(__file__)

with open(f"{PKG_DIR}\\config.json") as json_file:
    config = json.load(json_file)

STANDARD_WIDTH = int(config['window']['standard_width'])
STANDARD_HEIGHT = int(config['window']['standard_height'])

from mamba_ui.app import app
from mamba_ui.layout import serve_layout
