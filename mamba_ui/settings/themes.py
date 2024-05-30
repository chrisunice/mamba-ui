from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, MATCH

from mamba_ui import app
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


@app.callback(
    Output('external-stylesheet', 'href'),
    Input('theme-dropdown', 'value')
)
def update_app_theme(selected_theme):
    """ Updates the theme of the application """
    if selected_theme is not None:
        return selected_theme


@app.callback(
    Output({'type': 'linear-plot', 'index': MATCH}, 'figure'),
    Input('theme-dropdown', 'value'),
    State({'type': 'linear-plot', 'index': MATCH}, 'figure'),
    State('theme-dropdown', 'options')

)
def update_linear_plot_theme(theme_value, figure, theme_options):
    """ Updates the styling of the linear plot based on the overall application theme """
    if theme_value is None:
        raise PreventUpdate
    else:
        theme_map = {option['value']: option['label'] for option in theme_options}
        theme_name = theme_map[theme_value]
        if theme_name in config['themes']['light']:
            layout_updates = {
                'font': {'color': 'black'},
                'yaxis': {
                    'gridcolor': 'gray',
                    'zerolinecolor': 'black',
                    'zerolinewidth': 2,
                },
                'xaxis': {
                    'gridcolor': 'gray',
                    'zerolinecolor': 'black',
                    'zerolinewidth': 2,
                }
            }
        elif theme_name in config['themes']['dark']:
            layout_updates = {
                'font': {'color': 'white'},
                'yaxis': {
                    'gridcolor': 'lightgray',
                    'zerolinecolor': 'white',
                    'zerolinewidth': 2

                },
                'xaxis': {
                    'gridcolor': 'lightgray',
                    'zerolinecolor': 'white',
                    'zerolinewidth': 2,

                }
            }
        else:
            layout_updates = {}
        figure['layout'].update(layout_updates)
        return figure
