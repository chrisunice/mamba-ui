from dash import Input, Output
from dash_extensions.enrich import Trigger

import mamba_ui as mui


@mui.app.callback(
    Output('settings-window', 'is_open'),
    Input(
        component_id={'name': 'navbar', 'type': 'settings-icon', 'index': ''},
        component_property='n_clicks'
    ),
    Trigger('dash-layout', 'children')
)
def toggle_settings_window(click):
    if click is not None:
        return True
