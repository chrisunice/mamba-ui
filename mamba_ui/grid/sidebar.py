from dash import html
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Input, Output, State, MATCH

from mamba_ui import app
from mamba_ui.components import HorizontalLine
from mamba_ui.widgets.base import BaseWidget


class WidgetGridSidebarComponent(BaseWidget):

    width_open = 'max(25%, 350px)'
    width_closed = 0

    def __init__(self, top_offset, index: str = ""):
        super().__init__()
        self.top_offset = top_offset
        self.index = index

    @property
    def component(self):

        sidebar_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'position': 'absolute',
            'top': f'{self.top_offset}px',
            'left': 0,
            'width': f'{self.width_closed}',
            'height': f'calc(100% - {self.top_offset}px)',
            'zIndex': 1000,
            'padding': '10px 0px',
            'boxShadow': '10px 0px 10px gray',
            'transition': 'width 0.5s',
            'overflow': 'hidden'
        }

        return html.Div(
            id={'type': 'widget-side-bar', 'index': self.index},
            className='sidebar-visible bg-light',
            children=[
                html.H3('Menu', className='text-dark', style={'margin': 0}),
                HorizontalLine('sm')
            ],
            style=sidebar_style
        )


@app.callback(
    Output({'type': 'widget-side-bar', 'index': MATCH}, 'style'),
    Output({'type': 'widget-hamburger-button', 'index': MATCH}, 'className'),
    Input({'type': 'widget-hamburger-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'widget-side-bar', 'index': MATCH}, 'style'),
    State({'type': 'widget-hamburger-button', 'index': MATCH}, 'className')
)
def toggle_sidebar(hamburger_clicked: int, sidebar_style: dict, menu_class: str) -> tuple[dict, str]:
    """ Handles the opening and close of the widget tile's sidebar """
    if hamburger_clicked is None:
        raise PreventUpdate
    else:
        if 'fa-bars' in menu_class:
            # Open the sidebar
            sidebar_style.update({'width': WidgetGridSidebarComponent.width_open})
            menu_class = menu_class.replace('fa-bars', 'fa-xmark')
        elif 'fa-xmark' in menu_class:
            # Close the sidebar
            sidebar_style.update({'width': WidgetGridSidebarComponent.width_closed})
            menu_class = menu_class.replace('fa-xmark', 'fa-bars')
        else:
            raise PreventUpdate
        return sidebar_style, menu_class
