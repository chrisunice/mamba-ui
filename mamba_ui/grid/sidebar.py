from dash import html, callback_context
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Output, State, MATCH, Trigger

from mamba_ui import app
from mamba_ui.components import HorizontalLine
from mamba_ui.widgets.base import BaseWidget


class WidgetGridSidebarComponent(BaseWidget):

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
            # 'width': 'max(25%, 350px)',
            'width': 0,
            'height': f'calc(100% - {self.top_offset}px)',
            'zIndex': 1000,
            'padding': '10px 0px',
            'boxShadow': '10px 0px 10px gray',
            'transition': 'width 0.5s',
            'overflow': 'hidden'
        }

        sidebar = html.Div(
            id={'type': 'widget-side-bar', 'index': self.index},
            className='sidebar-visible bg-light',
            children=[
                html.H3('Menu', className='text-dark'),
                HorizontalLine('sm'),
                dbc.Button('My Button')
            ],
            style=sidebar_style
        )

        not_sidebar = html.Div(
            children=[],
            id={'type': 'not-sidebar', 'index': self.index},
            style={
                'position': 'fixed',
                'top': 0,
                'left': 0,
                'zIndex': 999,
                'width': '100vw',
                'height': '100vh',
                'visibility': 'visible',
            }
        )

        return html.Div(
            id={'type': 'sidebar-wrapper', 'index': self.index},
            children=[sidebar, not_sidebar],
        )


@app.callback(
    Output({'type': 'widget-side-bar', 'index': MATCH}, 'style'),
    Output({'type': 'not-sidebar', 'index': MATCH}, 'style'),
    Output({'type': 'widget-hamburger-button', 'index': MATCH}, 'className'),
    [
        Trigger({'type': 'widget-hamburger-button', 'index': MATCH}, 'n_clicks'),
        Trigger({'type': 'not-sidebar', 'index': MATCH}, 'n_clicks'),
    ],
    [
        State({'type': 'widget-side-bar', 'index': MATCH}, 'style'),
        State({'type': 'not-sidebar', 'index': MATCH}, 'style'),
    ]
)
def toggle_sidebar(sidebar_style: dict, not_sidebar_style: dict) -> tuple[dict, dict, str]:

    if callback_context.triggered_id is None:
        raise PreventUpdate
    else:

        action = callback_context.triggered_id['type']

        if action == 'widget-hamburger-button':
            # Open the sidebar
            sidebar_style.update({'width': 'max(25%, 350px)'})
            not_sidebar_style.update({'visibility': 'visible'})
            menu_icon = 'fa-solid fa-xmark fa-xl text-primary'
        elif action == 'not-sidebar':
            sidebar_style.update({'width': 0})
            not_sidebar_style.update({'visibility': 'hidden'})
            menu_icon = 'fa-solid fa-bars fa-xl text-primary'
        else:
            raise PreventUpdate

        return sidebar_style, not_sidebar_style, menu_icon
