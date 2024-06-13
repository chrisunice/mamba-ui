from dash import html, dcc
from mamba_ui.components.base import BaseComponent


class PlotControlPanelComponent(BaseComponent):

    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

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
            'width': '25%'
        }

        return html.Div(
            children=[
                html.Div(
                    html.I(className='fa-solid fa-circle-arrow-left fa-2xl'),
                    style=column_style
                ),
                html.Div(
                    dcc.Dropdown(placeholder='Select...', style={'width': '100%'}),
                    style=column_style
                ),
                html.Div(
                    html.Label(),
                    style=column_style
                ),
                html.Div(
                    html.I(className='fa-solid fa-circle-arrow-right fa-2xl'),
                    style=column_style
                )
            ],
            style=control_style
        )
