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
            'polarization': ['HH', 'VV']
        },
        index=uid
    ).component

# TODO need to come up with a way so that the process is...
#  data load -> pick up data columns -> select params to display (look vs rcs) -> build filters on other params (f, p)