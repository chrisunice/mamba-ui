from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components import HorizontalLine


AVAILABLE_THEMES = [theme for theme in dir(dbc.themes) if not theme.startswith('_')]

layout = dbc.Container(
    id='settings-page',
    children=[
        dcc.Store('settings-store'),
        dbc.Row([html.H3('Settings')], className='my-3'),
        dbc.Row([HorizontalLine('lg')]),
        dbc.Row([
            dbc.Col([html.Label('Theme', style=dict(fontSize='x-large'))]),
            dbc.Col([
                dcc.Dropdown(
                    id='theme-dropdown',
                    placeholder='Select a theme',
                    options=[{'label': theme, 'value': theme} for theme in AVAILABLE_THEMES]
                )
            ])
        ])
    ]
)

