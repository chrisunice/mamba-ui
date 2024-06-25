import json
from dash.exceptions import PreventUpdate
from dash import Input, Output, State, MATCH

import mamba_ui as mui


@mui.app.callback(
    Output({'parent': 'plot-control-panel', 'child': 'category-dropdown', 'index': MATCH}, 'value'),
    Output({'parent': 'plot-control-panel', 'child': 'value-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'widget-submit-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'plot-menu-filter-store', 'index': MATCH}, 'data'),
    State({'parent': 'plot-control-panel', 'child': 'store', 'index': MATCH}, 'data')
)
def init_control_panel_values(submit_click: int, filter_store: str, control_panel_store: str):
    if submit_click is None:
        raise PreventUpdate

    # Convert from json to dictionary
    filter_store = json.loads(filter_store)
    control_panel_store = json.loads(control_panel_store
                                     )
    print('hello')