from dash import html, dcc

from mamba_ui.components import NavBar
from mamba_ui.components import SideBar
from mamba_ui import STANDARD_WIDTH, STANDARD_HEIGHT


def serve_layout():

    app_styles = {
        'display': 'flex',
        'flex-direction': 'column',
        'width': '100%',
        'min-height': '100vh',
        'max-width': STANDARD_WIDTH,
        'max-height': STANDARD_HEIGHT
    }

    container_styles = {
        'display': 'flex',
        'flex': '1',
        'width': '100%'
    }
    return html.Div(
        id='dash-layout',
        children=[
            dcc.Location(id='url', refresh=True),
            dcc.Store(
                id='session-store',
                storage_type='session',
            ),
            html.Div(id='upload-data-output'),
            NavBar,
            SideBar,
            html.Div(id='page-container', style=container_styles),
        ],
        style=app_styles
    )
