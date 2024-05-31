from dash import html, dcc

from mamba_ui.components import NavBar
from mamba_ui.components import Footer
from mamba_ui.grid import WidgetGridComponent


def serve_layout():

    app_styles = {
        'display': 'flex',
        'flexDirection': 'column',
        'width': '100%',
        'minHeight': '100vh',
    }

    container_styles = {
        'display': 'flex',
        'flex': '1',
        'width': '100%'
    }

    widget_grid = WidgetGridComponent().json

    return html.Div(
        id='dash-layout',
        children=[
            dcc.Location(id='url', refresh=True),
            dcc.Store(id='session-store', storage_type='session'),
            html.Link(id='external-stylesheet', rel='stylesheet', href=''),
            html.Div(id='upload-data-output'),
            NavBar,
            html.Div(widget_grid, id='page-container', style=container_styles),
            Footer,
        ],
        style=app_styles
    )
