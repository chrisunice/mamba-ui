import dash
import requests
import dash_uploader
import dash_bootstrap_components as dbc

from mamba_ui import config


# Stylesheets
try:
    request = requests.get("http://www.google.com", timeout=1)
    sheets = [
        dbc.themes.CYBORG,
        dbc.icons.FONT_AWESOME,
        './assets/style.css'
    ]
except (requests.exceptions.ConnectionError, requests.Timeout):
    sheets = [
        './assets/cyborg/bootstrap.min.css'
        './assets/fontawesome/all.css'
    ]

# Application set up
app = dash.Dash(
    name=__name__,
    title='Mamba',
    external_stylesheets=sheets,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=False,
)

# Configure upload to server
dash_uploader.configure_upload(
    app=app,
    folder=config['home']['upload_folder'],
    use_upload_id=True
)
