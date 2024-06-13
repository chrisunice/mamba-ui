from dash import callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.base.menu.items.display import PlotMenuDisplayItemComponent


@mui.app.callback(
    Output({'type': 'plot-menu-display-container', 'index': MATCH}, 'children'),
    Input({'type': 'plot-menu-data-checklist', 'index': MATCH}, 'value'),
    State({'type': 'plot-menu-data-store', 'index': MATCH}, 'data')
)
def populate_menu_display(selected_files, data):
    if callback_context.triggered_id is None:
        raise PreventUpdate
    elif not selected_files:
        options = None
    else:
        # Getting column names from all selected files
        column_names = [set(data[ds_name].columns) for ds_name in selected_files]

        # Put the im one list
        column_names = list(set.intersection(*column_names))

        # Build options dictionary for dropdown component
        options = [dict(label=name, value=name, disabled=False) for name in sorted(column_names)]

    # Send back component
    uid = callback_context.triggered_id.index
    return PlotMenuDisplayItemComponent(options, uid).component

