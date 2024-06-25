import itertools
from dash.exceptions import PreventUpdate
from dash import Input, Output, State

import mamba_ui as mui
from mamba_ui.grid import WidgetGridComponent


@mui.app.callback(
    Output(
        component_id='page-container',
        component_property='children'
    ),
    [
        Input(
            component_id={'name': 'grid-shape-row', 'type': 'rows-input', 'index': ''},
            component_property='value'
        ),
        Input(
            component_id={'name': 'grid-shape-row', 'type': 'columns-input', 'index': ''},
            component_property='value'
        ),
    ],
    [
        State(
            component_id={'name': 'settings-window', 'index': ''},
            component_property='is_open'
        ),
        State(
            component_id={'name': 'widget-grid', 'type': 'layout', 'index': ''},
            component_property='children'
        )
    ]
)
def update_grid_layout(nrows, ncols, settings_open, current_grid):
    # Do nothing if settings window is open
    if not settings_open:
        raise PreventUpdate

    # Extract the widgets from layout regardless of where they're located
    widgets = [row_container['props']['children'] for row_container in current_grid]
    widgets = list(itertools.chain.from_iterable(widgets))

    # Send back new grid component that is built with prior widgets
    return WidgetGridComponent(shape=(nrows, ncols), widgets=widgets).component
