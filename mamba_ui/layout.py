from dash import html, dcc

from mamba_ui.components.navbar import NavbarComponent
from mamba_ui.components.footer import FooterComponent
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

    return html.Div(
        id='dash-layout',
        children=[
            dcc.Location(id='url', refresh=True),
            dcc.Store(id='session-store', storage_type='session'),
            html.Link(id='external-stylesheet', rel='stylesheet', href=''),
            NavbarComponent().component,
            html.Div(WidgetGridComponent().component, id='page-container', style=container_styles),
            FooterComponent().component,
        ],
        style=app_styles
    )
