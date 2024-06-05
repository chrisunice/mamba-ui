import dash_uploader as du
from dash_extensions.enrich import Input, Output, State, MATCH

import mamba_ui as mui


# @du.callback(
@mui.app.callback(
    Output({'type': 'widget-menu-data-checklist', 'index': MATCH}, 'options'),
    Input({'type': 'widget-menu-data-upload', 'index': MATCH}, 'isCompleted'),
    State('session-store', 'data')
)
def display_uploaded_files(is_complete, data):
    print(is_complete, data)
    return []
