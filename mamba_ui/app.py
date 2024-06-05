import requests
import dash_uploader
import dash_bootstrap_components as dbc
from dash_extensions.enrich import DashProxy, MultiplexerTransform, ServersideOutputTransform, FileSystemStore, \
    TriggerTransform, NoOutputTransform, CycleBreakerTransform

from mamba_ui import config


# Stylesheets
# try:
#     request = requests.get("http://www.google.com", timeout=1)
#     sheets = [
#         dbc.themes.CYBORG,
#         dbc.icons.FONT_AWESOME,
#         './assets/style.css',
#         # GRIDSTACK_CSS
#     ]
# except (requests.exceptions.ConnectionError, requests.Timeout):
#     pass
    # sheets = [
    #     './assets/cyborg/bootstrap.min.css'
    #     './assets/fontawesome/all.css'
    # ]

# Application set up
app = DashProxy(
    name=__name__,
    title='Mamba',
    external_stylesheets=[
        getattr(dbc.themes, config['themes']['default']),       # dash bootstrap themes
        dbc.icons.FONT_AWESOME,                                 # font awesome icons
        dbc.icons.BOOTSTRAP,                                    # bootstrap icons
    ],
    external_scripts=[],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=False,
    transforms=[
        MultiplexerTransform(),
        ServersideOutputTransform(
            backend=FileSystemStore(cache_dir=config['paths']['cache_directory'])
        ),
        TriggerTransform(),
        NoOutputTransform(),
        CycleBreakerTransform()
    ]
)

# Configure upload to server
dash_uploader.configure_upload(
    app=app,
    folder=config['paths']['upload_directory'],
    use_upload_id=True
)
