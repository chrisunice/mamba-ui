from dash import html, dcc
import dash_bootstrap_components as dbc
from mamba_ui.components.base import BaseComponent


class PlotMenuDisplayItemComponent(BaseComponent):
    def __init__(self, options: list = None, index: str = ''):
        super().__init__()

        if options is None:
            options = []
        self.options = options

        self.index = index

    def _build_dropdown(self, variable_type: str) -> dcc.Dropdown:
        dropdown_style = {
            'width': '100%'
        }
        return dcc.Dropdown(
            placeholder=f'{variable_type.capitalize()} Variable',
            options=self.options,
            multi=False,
            style=dropdown_style
        )

    @property
    def _verses(self) -> html.Label:
        label_style = {
            'margin': '0px 10px'
        }

        return html.Label(
            children=['vs.'],
            style=label_style
        )

    @property
    def component(self) -> dbc.AccordionItem:
        container_style = {
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center'
        }

        return dbc.AccordionItem(
            children=[
                html.Div(
                    children=[
                        self._build_dropdown('independent'),
                        self._verses,
                        self._build_dropdown('dependent')
                    ],
                    style=container_style
                )
            ],
            title=html.H4('Display')
        )
