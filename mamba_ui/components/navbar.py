from dash import html
from dash_extensions.enrich import Input, Output, Trigger

from mamba_ui import app
from mamba_ui.settings.window import SettingsWindow


ApplicationTitle = html.H1(
    'D\u2074',
    # 'Mamba',
    title='Denmar Data analysis Dashboard and Database',
    style={
        'fontStyle': 'oblique',
        'cursor': 'pointer'
    },
    className='text-light'
)

NavBar = html.Div(
    id='navbar',
    className='bg-primary',
    children=[
        ApplicationTitle,
        html.I(
            id='settings-icon',
            className='fa-solid fa-gear fa-2xl text-light',
        ),
        SettingsWindow
    ],
    style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'align-items': 'center',
        'padding': '0px 20px'
    }
)


@app.callback(
    Output('settings-window', 'is_open'),
    Input('settings-icon', 'n_clicks'),
    Trigger('dash-layout', 'children')
)
def open_settings(click):
    if click is not None:
        return True
