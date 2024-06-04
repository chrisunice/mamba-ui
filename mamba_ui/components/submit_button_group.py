from dash import html
import dash_bootstrap_components as dbc


class SubmitButtonGroup:

    def __init__(self, name: str, index: str = ''):
        """
        :param name: unique identifier for the component
        :param index:
        """

        self.name = name
        self.index = index

    @property
    def component(self) -> html.Div:

        style = {
            'display': 'flex',
            'flexDirection': 'column',
            'flex': '1',
            'justify-content': 'flex-end',
            'align-items': 'left',
            'width': 'min(100%, 750px)',
            'padding': '10px'
        }

        return html.Div(
            children=[
                html.Div(
                    children=[
                        dbc.Button(
                            html.Label('Submit'),
                            id={'type': f'{self.name}-submit-button', 'index': self.index},
                            color='primary',
                            style={'width': '60%'}
                        ),
                        dbc.Button(
                            html.Label('Reset'),
                            id={'type': f'{self.name}-reset-button', 'index': self.index},
                            color='secondary',
                            style={'width': '35%'}
                        )
                    ],
                    style={'display': 'flex', 'justify-content': 'space-between', 'margin-top': '10px'}
                ),
            ],
            style=style
        )
