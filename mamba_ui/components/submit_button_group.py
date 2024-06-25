from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class SubmitButtonGroupComponent(BaseComponent):

    name = 'Submit Button Group'

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

    @property
    def _submit_button(self) -> dbc.Button:

        submit_style = {
            'width': '60%'
        }

        return dbc.Button(
            id=self.get_child_id('submit'),
            children=[html.Label('Submit')],
            color='primary',
            style=submit_style
        )

    @property
    def _reset_button(self) -> dbc.Button:

        reset_style = {
            'width': '35%'
        }

        return dbc.Button(
            id=self.get_child_id('reset'),
            children=[html.Label('Reset')],
            color='secondary',
            style=reset_style
        )

    @property
    def component(self) -> html.Div:

        component_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'flex': '1',
            'justify-content': 'flex-end',
            'alignItems': 'left',
            'width': 'min(100%, 750px)',
            'padding': '10px'
        }

        button_container_style = {
            'display': 'flex',
            'justify-content': 'space-between',
            'marginTop': '10px'
        }

        return html.Div(
            id=self.id,
            children=[
                html.Div(
                    children=[self._submit_button, self._reset_button],
                    style=button_container_style
                ),
            ],
            style=component_style
        )
