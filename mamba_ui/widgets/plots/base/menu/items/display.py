import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback_context
from dash_extensions.enrich import Input, Output, State, MATCH

from mamba_ui import app
from mamba_ui.components.base import BaseComponent


class PlotMenuDisplayItemComponent(BaseComponent):
    def __init__(self, options: list = None, index: str = ''):
        """
        A dbc.AccordionItem that contains the functionality of displaying two parameters against one another

        :param options: the names of variables that will be used as independent or dependent variables for plotting
        :param index: unique index for the component
        """
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
            id={'type': f'{variable_type}-dropdown', 'index': self.index},
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


@app.callback(
    [
        Output({'type': 'independent-dropdown', 'index': MATCH}, 'options'),
        Output({'type': 'dependent-dropdown', 'index': MATCH}, 'options')
    ],
    [
        Input({'type': 'independent-dropdown', 'index': MATCH}, 'value'),
        Input({'type': 'dependent-dropdown', 'index': MATCH}, 'value')
    ],
    [
        State({'type': 'independent-dropdown', 'index': MATCH}, 'options'),
        State({'type': 'dependent-dropdown', 'index': MATCH}, 'options')
    ]

)
def update_other_dropdown(ivar_value: str, dvar_value: str, ivar_opts: list, dvar_opts: list):
    if callback_context.triggered_id is None:
        raise PreventUpdate

    def toggle_option(options: list[dict], value: str):
        if value is None:
            for option in options:
                option.update({'disabled': False})
        else:
            for option in options:
                if option['value'] == value:
                    option.update({'disabled': not option['disabled']})

    triggered = callback_context.triggered_id['type']
    if triggered == 'independent-dropdown':
        toggle_option(dvar_opts, ivar_value)

    if triggered == 'dependent-dropdown':
        toggle_option(ivar_opts, dvar_value)

    return ivar_opts, dvar_opts
