from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components import HorizontalLine
from mamba_ui.settings.themes import ThemeDropdownRow
from mamba_ui.settings.gridshape import GridShapeRow


SettingsWindow = dbc.Modal(
    [
        dcc.Store('settings-store', storage_type='memory'),
        dbc.ModalHeader(html.H2('Settings')),
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
