from dash import Input, Output
from dash_extensions.enrich import Trigger

import mamba_ui as mui


@mui.app.callback(
    Output(
        component_id={'name': 'settings-window', 'index': ''},
        component_property='is_open'
    ),
    Input(
        component_id={'name': 'navbar', 'type': 'settings-icon', 'index': ''},
        component_property='n_clicks'
    ),
    Trigger(
        component_id='dash-layout',
        component_property='children'
    )
)
def toggle_settings_window(click):
    if click is not None:
        return True
