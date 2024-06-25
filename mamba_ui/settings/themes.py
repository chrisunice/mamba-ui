from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import Input, Output, State, MATCH

from mamba_ui import app
from mamba_ui import config
from mamba_ui.components.base import BaseComponent


class ThemeDropdownRowComponent(BaseComponent):

    name = 'Theme Dropdown Row'
    themes = sorted(config['themes']['light'] + config['themes']['dark'])

    def __init__(self):
        super().__init__()

    @property
    def _label(self):
        return html.Label(
            'Theme:',
            style={
                'fontWeight': 'bold'
            }
        )

    @property
    def _dropdown(self):
        return dcc.Dropdown(
            id=self.get_child_id('dropdown'),
            placeholder=config['themes']['default'],
            options=[
                {'label': theme, 'value': getattr(dbc.themes, theme)} for theme in self.themes
            ],
            clearable=False,
            style={'color': 'gray'}
        )

    @property
    def component(self):
        return dbc.Row(
            [
                dbc.Col(self._label, width=6),
                dbc.Col(self._dropdown, width=6)
            ],
            align='center'
        )


# Callbacks


