"""
TODO:
 need to add callbacks to handle what the arrows do
 somehow pass the values for each categorical variable so they can be cycled through
"""

from dash import html, dcc
from mamba_ui.components.base import BaseComponent


class PlotControlPanelComponent(BaseComponent):

    name = 'Plot Control Panel'

    def __init__(self, index: str = ''):
        super().__init__()
        self.id = {
            'parent-component': self.uid,
            'index': index
        }

    def _build_icon(self, side: str):
        icon_id = self.id.copy()
        icon_id.update(
            {'child-component': f'arrow-{side}'}
        )

        icon_style = {}

        return html.I(
            id=icon_id,
            className=f'fa-solid fa-circle-arrow-{side} fa-2xl',
            style=icon_style
        )

    @property
    def _dropdown(self):
        dropdown_id = self.id.copy()
        dropdown_id.update(
            {'child-component': 'dropdown'}
        )

        dropdown_style = {
            'width': '100%'
        }

        return dcc.Dropdown(
            id=dropdown_id,
            placeholder='Select ... ',
            style=dropdown_style
        )

    @property
    def component(self):
        control_style = {
            'display': 'flex',
            'width': '50%',
            'justifyContent': 'space-evenly',
            'alignItems': 'center'

        }

        column_style = {
            'display': 'flex',
            'justifyContent': 'center',
            'width': '100%'
        }

        return html.Div(
            children=[
                html.Div(self._build_icon('left'), style=column_style),
                html.Div(self._dropdown, style=column_style),
                html.Div(self._build_icon('right'), style=column_style)
            ],
            style=control_style
        )
