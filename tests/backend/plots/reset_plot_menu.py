from dash.exceptions import PreventUpdate
from dash import Input, Output, MATCH, ALL, callback_context

import mamba_ui as mui
from mamba_ui.widgets.plots.two_dimensional.menu.data import TwoDimensionalPlotMenuDataItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.display import TwoDimensionalPlotMenuDisplayItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.filter import TwoDimensionalPlotMenuFilterItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.design import TwoDimensionalPlotMenuDesignItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.export import TwoDimensionalPlotMenuExportItemComponent


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
        [TwoDimensionalPlotMenuDataItemComponent(index=index).component],
        [TwoDimensionalPlotMenuDisplayItemComponent(index=index).component],
        [TwoDimensionalPlotMenuFilterItemComponent(index=index).component],
        [TwoDimensionalPlotMenuDesignItemComponent(index=index).component],
        [TwoDimensionalPlotMenuExportItemComponent(index=index).component]
    ]
