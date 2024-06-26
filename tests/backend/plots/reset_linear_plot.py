"""
NOTE would this callback work for polar and linear plots if name was changed to ALL?
"""

from dash.exceptions import PreventUpdate
from dash import Input, Output, MATCH, State

import mamba_ui as mui


@mui.app.callback(
    Output(
        component_id={'name': 'linear-plot', 'type': 'graph', 'index': MATCH},
        component_property='figure',
        allow_duplicate=True
    ),
    Input(
        component_id={'name': 'plot-menu-submit-button-group', 'type': 'reset', 'index': MATCH},
        component_property='n_clicks'
    ),
    State(
        component_id={'name': 'linear-plot', 'type': 'graph', 'index': MATCH},
        component_property='figure'
    ),
    prevent_initial_call=True
)
def reset_linear_plot(reset_click: int, figure):
    if reset_click is None:
        raise PreventUpdate

    figure['data'] = []
    return figure
