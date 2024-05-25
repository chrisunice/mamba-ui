from dash import html, dcc
from dash_extensions import DeferScript

from mamba_ui.grid import widget_grid as WidgetGrid
from mamba_ui.components import NavBar
from mamba_ui.components import Footer
from mamba_ui import STANDARD_WIDTH, STANDARD_HEIGHT


def serve_layout():

    app_styles = {
        'display': 'flex',
        'flexDirection': 'column',
        'width': '100%',
        'minHeight': '100vh',
        # 'max-width': STANDARD_WIDTH,
        # 'max-height': STANDARD_HEIGHT
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
            dcc.Store(id='session-store', storage_type='session'),
            html.Link(id='external-stylesheet', rel='stylesheet', href=''),
            html.Div(id='upload-data-output'),
            NavBar,
            html.Div(id='page-container', children=[WidgetGrid()], style=container_styles),
            Footer,
            # DeferScript(src=r'./assets/gridstack/gridstack-init.js')
        ],
        style=app_styles
    )
