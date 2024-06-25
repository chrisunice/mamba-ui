from dash import html, dcc
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class GridShapeRowComponent(BaseComponent):

    name = 'Grid Shape Row'

    def __init__(self):
        super().__init__()

    def _build_input_item(self, name: str) -> dcc.Input:
        return dcc.Input(
            id=self.get_child_id(f'{name}-input'),
            type='number',
            placeholder=f'{name.capitalize()}',
            value=1,
            min=1,
            max=4,
            required=True,
            debounce=True,
            style={
                'maxWidth': '100%'
            }
        )

    @property
    def component(self):
        return dbc.Row(
            children=[
                dbc.Col(html.Label('Widget Grid:', style={'fontWeight': 'bold'}), width=6),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Col(html.Label('Rows:'),  width=3),
                            dbc.Col(self._build_input_item('rows'), width=3),
                            dbc.Col(html.Label('Columns:'), width=3),
                            dbc.Col(self._build_input_item('columns'), width=3)
                        ],
                        justify='around'
                    ),
                    width=6
                )
            ],
            align='center'
        )
