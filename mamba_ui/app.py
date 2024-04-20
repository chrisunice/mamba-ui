import requests
import dash_uploader
import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, MultiplexerTransform, ServersideOutputTransform, FileSystemStore, \
    TriggerTransform, NoOutputTransform, CycleBreakerTransform

from mamba_ui import config


# GRIDSTACK_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/gridstack.js/0.6.4/gridstack.min.css'
# GRIDSTACK_JS = 'https://cdnjs.cloudflare.com/ajax/libs/gridstack.js/0.6.4/gridstack.min.js'

# Stylesheets
try:
    request = requests.get("http://www.google.com", timeout=1)
    sheets = [
        dbc.themes.CYBORG,
        dbc.icons.FONT_AWESOME,
        './assets/style.css',
        # GRIDSTACK_CSS
    ]
except (requests.exceptions.ConnectionError, requests.Timeout):
    sheets = [
        './assets/cyborg/bootstrap.min.css'
        './assets/fontawesome/all.css'
    ]

# Application set up
app = DashProxy(
    name=__name__,
    title='Mamba',
    external_stylesheets=sheets,
    # external_scripts=[GRIDSTACK_JS],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=False,
    transforms=[
        MultiplexerTransform(),
        ServersideOutputTransform(
            backend=FileSystemStore(cache_dir=config['init']['cache_dir'])
        ),
        TriggerTransform(),
        NoOutputTransform(),
        CycleBreakerTransform()
    ]
)

# Configure upload to server
dash_uploader.configure_upload(
    app=app,
    folder=config['home']['upload_folder'],
    use_upload_id=True
)
