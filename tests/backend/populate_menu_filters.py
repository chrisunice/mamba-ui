import numpy as np
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.base.menu.items.filter import PlotMenuFilterItemComponent


@mui.app.callback(
    Output({'type': 'plot-menu-filter-container', 'index': MATCH}, 'children'),
    Input({'type': 'widget-container', 'index': MATCH}, 'children')
)
def populate_menu_filters(widget_container):
    if widget_container is None:
        raise PreventUpdate

    options = np.arange(2000, 18000, 1000)
    options = [dict(label=i, value=i) for i in options]

    ctx = callback_context
    uid = ctx.args_grouping.id.index

    return PlotMenuFilterItemComponent(
        categorical_filters={
            'frequency': options,
            'polarization': ['HH', 'VV'],
            'pass': [1, 2, 3, 4]
        },
        numerical_filters={
            'look': dict(minimum=0, maximum=360, step=1),
            'depression': dict(minimum=-90, maximum=90, step=5),
            'twist': dict(minimum=-30, maximum=30, step=1)
        },
        index=uid
    ).component
