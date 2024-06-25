import os
import json
from dash_extensions.enrich import Trigger, Output, State

import mamba_ui as mui


@mui.app.callback(
    Output('session-store', 'data'),
    Trigger('dash-layout', 'children'),
    State('session-store', 'data')
)
def create_test_client(session_data):
    if session_data is None:
        # Make client folder, if it doesn't already exist
        root_dir = mui.config['paths']['root_directory']
        username = 'ui_test_client'
        client_dir = f"{root_dir}/clients/{username}"
        os.makedirs(client_dir, exist_ok=True)

        # Store the session data
        session_data = {
            'username': username,
            'uploads': {},
            'settings': {}
        }
        return json.dumps(session_data)
    else:
        return session_data
