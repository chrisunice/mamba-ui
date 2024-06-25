import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback_context
from dash_extensions.enrich import Input, Output, MATCH, ALL

from mamba_ui import app
from mamba_ui.widgets.base import BaseComponent


class NumericalInputComponent(BaseComponent):
    def __init__(
            self,
            name: str,
            minimum: int | float,
            maximum: int | float,
            step: int | float,
            index: str = ''
    ):
        super().__init__()
        self.name = name
        self.minimum = minimum
        self.maximum = maximum
        self.step = step
        self.id = {
            'parent': f'{self.name}-numerical-input',
            'index': index
        }

    def _build_input(self, name) -> dcc.Input:
        input_id = self.id.copy()
        input_id.update({'child': f'{name}-input'})

        input_style = {
            'display': 'flex',
            'margin': '0px 10px'
        }

        return dcc.Input(
            id=input_id,
            type='number',
            debounce=True,
            min=self.minimum,
            max=self.maximum,
            step=self.step,
            style=input_style
        )

    @property
    def _row1(self):

        row_style = {
            'display': 'flex',
            'flexWrap': 'wrap',
            'justifyContent': 'space-evenly',
            'alignItems': 'center',
            'width': '100%',
        }

        return html.Div(
            children=[
                html.Div(
                    children=[html.Label('Min:'), self._build_input('min')],
                    style={'display': 'flex'}
                ),
                html.Div(
                    children=[html.Label('Max:'), self._build_input('max')],
                    style={'display': 'flex'}
                )
            ],
            style=row_style
        )

    @property
    def _row2(self):

        switch_id = self.id.copy()
        switch_id.update({'child': 'switch'})

        label_id = self.id.copy()
        label_id.update({'child': 'switch-label'})

        row_style = {
            'display': 'flex',
            'flexWrap': 'wrap',
            'justifyContent': 'space-evenly',
            'alignItems': 'center',
            'width': '50%',
        }

        label = html.Label(
            children=['Inclusive'],
            id=label_id
        )

        switch = dbc.Switch(
            value=True,
            style={'margin': 0},
            id=switch_id
        )

        return html.Div(
            children=[label, switch],
            style=row_style
        )

    @property
    def component(self):

        container_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
        }

        return html.Div(
            children=[
                self._row1,
                self._row2
            ],
            style=container_style
        )


@app.callback(
    Output({'parent': ALL, 'child': 'switch-label', 'index': MATCH}, 'children'),
    Input({'parent': ALL, 'child': 'switch', 'index': MATCH}, 'value')
)
def update_switch_label(switch_values):
    if callback_context.triggered_id is None:
        raise PreventUpdate

    return ['Inclusive' if value else 'Exclusive' for value in switch_values]
