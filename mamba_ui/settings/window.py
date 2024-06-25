from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.settings.themes import ThemeDropdownRowComponent
from mamba_ui.settings.gridshape import GridShapeRowComponent
from mamba_ui.components.lines import HorizontalLineComponent


class SettingsWindowComponent(BaseComponent):

    name = 'Settings Window'

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
                ThemeDropdownRowComponent().component,
                HorizontalLineComponent('sm', index='0').component,
                GridShapeRowComponent().component,
                HorizontalLineComponent('sm', index='1').component
            ],
            style=body_style
        )

    @property
    def _footer(self) -> dbc.ModalFooter:
        return dbc.ModalFooter()

    @property
    def component(self) -> dbc.Modal:
        return dbc.Modal(
            id=self.id,
            children=[
                dcc.Store('settings-store', storage_type='memory'),
                self._header,
                self._body,
                self._footer
            ],
            size='lg'
        )
