from dash import html, dcc
import dash_bootstrap_components as dbc
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
            'parent-component': f'{self.name}-range-slider',
            'index': index
        }

    def _build_input(self) -> dcc.Input:
        input_id = self.id.copy()
        input_id.update({'child-component': 'input'})

        input_style = {
            'display': 'flex',
            'marginLeft': '10px'
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
    def component(self):

        container_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
        }

        row1_style = {
            'display': 'flex',
            'flexWrap': 'wrap',
            'justifyContent': 'space-evenly',
            'alignItems': 'center',
            'width': '100%',
        }

        row2_style = row1_style.copy()
        row2_style.update({'width': '50%'})

        return html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            [
                                html.Label('Min:'),
                                self._build_input()
                            ],
                            style={'display': 'flex'}
                        ),
                        html.Div(
                            [
                                html.Label('Max:'),
                                self._build_input()
                            ],
                            style={'display': 'flex'}
                        )
                    ],
                    style=row1_style
                ),
                html.Div(
                    children=[
                        html.Label('Inclusive'),
                        dbc.Switch(value=True, style={'margin': 0})
                    ],
                    style=row2_style
                )
            ],
            style=container_style
        )
