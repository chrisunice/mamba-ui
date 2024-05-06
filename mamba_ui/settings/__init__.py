from dash import dcc, html
import dash_bootstrap_components as dbc

from .themes import ThemeDropdownRow
from .gridshape import GridShapeRow
from mamba_ui.components import HorizontalLine

SettingsWindow = dbc.Modal(
    [
        dcc.Store('settings-store', storage_type='memory'),
        dbc.ModalHeader(html.H3('Settings')),
        dbc.ModalBody(
            [
                ThemeDropdownRow,
                HorizontalLine('sm'),
                GridShapeRow,
                HorizontalLine('sm')
            ],
            style={'height': '50vh'}
        ),
        dbc.ModalFooter()
    ],
    id='settings-window',
    size='lg'
)
