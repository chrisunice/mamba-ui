from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui import config

_AVAILABLE_THEMES = [theme for theme in dir(dbc.themes) if not theme.startswith('_')]

label = html.Label(
    'Theme:',
    style={
        'fontWeight': 'bold'
    }
)

dropdown = dcc.Dropdown(
    id='theme-dropdown',
    placeholder=config['default']['theme'],
    options=[{'label': theme, 'value': getattr(dbc.themes, theme)} for theme in _AVAILABLE_THEMES]
)


ThemeDropdownRow = dbc.Row(
    [
        dbc.Col(label, width=6),
        dbc.Col(dropdown, width=6)
    ],
    align='center'
)
