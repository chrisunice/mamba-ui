from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.settings.themes import ThemeDropdownRow
from mamba_ui.settings.gridshape import GridShapeRow
from mamba_ui.components.lines import HorizontalLineComponent


class SettingsWindow(BaseComponent):

    def __init__(self):
        super().__init__()

    @property
    def _header(self) -> dbc.ModalHeader:
        return dbc.ModalHeader(
            children=[
                html.H2('Settings')
            ]
        )

    @property
    def _body(self) -> dbc.ModalBody:
        body_style = {
            'height': '50vh'
        }

        return dbc.ModalBody(
            children=[
                ThemeDropdownRow,
                HorizontalLineComponent('sm').component,
                GridShapeRow,
                HorizontalLineComponent('sm').component
            ],
            style=body_style
        )

    @property
    def _footer(self) -> dbc.ModalFooter:
        return dbc.ModalFooter()

    @property
    def component(self) -> dbc.Modal:
        return dbc.Modal(
            children=[
                dcc.Store('settings-store', storage_type='memory'),
                self._header,
                self._body,
                self._footer
            ],
            id='settings-window',
            size='lg'
        )
