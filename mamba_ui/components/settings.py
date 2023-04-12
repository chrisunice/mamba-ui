from dash import dcc, html
import dash_daq as daq
import dash_bootstrap_components as dbc

Settings = dbc.Modal(
    id='settings-modal',
    children=[
        dcc.Store('settings-store'),
        dbc.ModalHeader(html.H5('Settings')),
        dbc.ModalBody(
            daq.BooleanSwitch(
                id='monitor-imagery-switch',
                on=True
            )
        ),
    ],
    centered=True,
    is_open=False
)
