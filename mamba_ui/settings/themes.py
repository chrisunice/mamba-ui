from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui import config

AVAILABLE_THEMES = sorted(config['themes']['light'] + config['themes']['dark'])

label = html.Label(
    'Theme:',
    style={
        'fontWeight': 'bold'
    }
)

dropdown = dcc.Dropdown(
    id='theme-dropdown',
    placeholder=config['themes']['default'],
    options=[
        {'label': theme, 'value': getattr(dbc.themes, theme)} for theme in AVAILABLE_THEMES
    ]
)

ThemeDropdownRow = dbc.Row(
    [
        dbc.Col(label, width=6),
        dbc.Col(dropdown, width=6)
    ],
    align='center'
)
