from dash.exceptions import PreventUpdate
from dash import Input, Output, MATCH, ALL, callback_context

import mamba_ui as mui
from mamba_ui.widgets.plots.base.menu.data import PlotMenuDataItemComponent
from mamba_ui.widgets.plots.base.menu.display import PlotMenuDisplayItemComponent
from mamba_ui.widgets.plots.base.menu.filter import PlotMenuFilterItemComponent
from mamba_ui.widgets.plots.base.menu.design import PlotMenuDesignItemComponent
from mamba_ui.widgets.plots.base.menu.export import PlotMenuExportItemComponent


@mui.app.callback(
    [
        Output(
            component_id={'name': ALL, 'type': 'data-container', 'index': MATCH},
            component_property='children',
            allow_duplicate=True
        ),
        Output(
            component_id={'name': ALL, 'type': 'display-container', 'index': MATCH},
            component_property='children',
            allow_duplicate=True
        ),
        Output(
            component_id={'name': ALL, 'type': 'filter-container', 'index': MATCH},
            component_property='children',
            allow_duplicate=True
        ),
        Output(
            component_id={'name': ALL, 'type': 'design-container', 'index': MATCH},
            component_property='children',
            allow_duplicate=True
        ),
        Output(
            component_id={'name': ALL, 'type': 'export-container', 'index': MATCH},
            component_property='children',
            allow_duplicate=True
        )
    ],
    Input(
        component_id={'name': 'plot-menu-submit-button-group', 'type': 'reset', 'index': MATCH},
        component_property='n_clicks'
    ),
    prevent_initial_call=True
)
def reset_plot_menu(reset_click: int):
    if reset_click is None:
        raise PreventUpdate

    index = callback_context.triggered_id['index']
    return [
        [PlotMenuDataItemComponent(index=index).component],
        [PlotMenuDisplayItemComponent(index=index).component],
        [PlotMenuFilterItemComponent(index=index).component],
        [PlotMenuDesignItemComponent(index=index).component],
        [PlotMenuExportItemComponent(index=index).component]
    ]
