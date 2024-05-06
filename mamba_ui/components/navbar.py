from dash import html
import dash_bootstrap_components as dbc
from mamba_ui.settings import SettingsWindow

NavBar = dbc.Navbar(
    id='navbar',
    children=[
        html.H2('Mamba'),
        html.I(
            id='settings-icon',
            className='fa-solid fa-gear fa-2xl',
        ),
        SettingsWindow
    ],
    color='primary',
    style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'padding': '0px 10px'
    }
)
