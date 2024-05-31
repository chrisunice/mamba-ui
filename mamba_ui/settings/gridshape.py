import itertools
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State

from mamba_ui import app
from mamba_ui.grid import WidgetGridComponent


# Component

def input_item(name: str) -> dcc.Input:
    return dcc.Input(
        id=f'grid-{name}',
        type='number',
        placeholder=f'{name.capitalize()}',
        value=1,
        min=1,
        max=4,
        required=True,
        debounce=True,
        style={
            'maxWidth': '100%'
        }
    )


GridShapeRow = dbc.Row(
    [
        dbc.Col(html.Label('Widget Grid:', style={'fontWeight': 'bold'}), width=6),
        dbc.Col(
            dbc.Row(
                [
                    dbc.Col(html.Label('Rows:'),  width=3),
                    dbc.Col(input_item('rows'), width=3),
                    dbc.Col(html.Label('Columns:'), width=3),
                    dbc.Col(input_item('columns'), width=3)
                ],
                justify='around'
            ),
            width=6
        )
    ],
    align='center'
)

# Callback


@app.callback(
    Output('page-container', 'children'),
    Input('grid-rows', 'value'),
    Input('grid-columns', 'value'),
    State('settings-window', 'is_open'),
    State('grid-layout', 'children')
)
def update_grid_layout(nrows, ncols, settings_open, current_grid):
    # Do nothing if settings window is open
    if not settings_open:
        raise PreventUpdate

    # Extract the widgets from layout regardless of where they're located
    widgets = [row_container['props']['children'] for row_container in current_grid]
    widgets = list(itertools.chain.from_iterable(widgets))

    # Send back new grid component that is built with prior widgets
    return WidgetGridComponent(shape=(nrows, ncols), widgets=widgets).json
