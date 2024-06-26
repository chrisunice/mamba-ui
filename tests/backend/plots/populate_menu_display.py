from dash import callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, MATCH, ALL

import mamba_ui as mui
from mamba_ui.widgets.plots.base.menu.display import PlotMenuDisplayItemComponent


@mui.app.callback(
    Output(
        component_id={'name': ALL, 'type': 'display-container', 'index': MATCH},
        component_property='children'
    ),
    Input(
        component_id={'name': 'plot-menu-data-checklist', 'index': MATCH},
        component_property='value'
    ),
    State(
        component_id={'name': 'plot-menu-data', 'type': 'data-store', 'index': MATCH},
        component_property='data'
    )
)
def populate_menu_display(selected_files, data):
    """ Populates the plot menu display items based on the selected data files """

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
    return [
        PlotMenuDisplayItemComponent(
            index=callback_context.triggered_id.index,
            options=options
        ).component
    ]


