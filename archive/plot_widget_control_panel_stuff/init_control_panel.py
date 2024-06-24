import json
from dash.exceptions import PreventUpdate
from dash import Input, Output, State, MATCH

import mamba_ui as mui


@mui.app.callback(
    Output({'parent-component': 'plot-control-panel', 'child-component': 'category-dropdown', 'index': MATCH}, 'value'),
    Output({'parent-component': 'plot-control-panel', 'child-component': 'value-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'widget-submit-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'plot-menu-filter-store', 'index': MATCH}, 'data'),
    State({'parent-component': 'plot-control-panel', 'child-component': 'store', 'index': MATCH}, 'data')
)
def init_control_panel_values(submit_click: int, filter_store: str, control_panel_store: str):
    if submit_click is None:
        raise PreventUpdate

    # Convert from json to dictionary
    filter_store = json.loads(filter_store)
    control_panel_store = json.loads(control_panel_store
                                     )
    print('hello')