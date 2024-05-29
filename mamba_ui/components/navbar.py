from dash import html
from mamba_ui.settings import SettingsWindow


NavBar = html.Div(
    id='navbar',
    className='bg-primary',
    children=[
        html.H2('Mamba', className='text-light'),
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
        'padding': '0px 10px'
    }
)
