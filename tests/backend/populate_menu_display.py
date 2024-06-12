import numpy as np
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.base.menu.items.display import PlotMenuDisplayItemComponent


@mui.app.callback(
    Output({'type': 'plot-menu-display-container', 'index': MATCH}, 'children'),
    Input({'type': 'widget-container', 'index': MATCH}, 'children')
)
def populate_menu_display(widget_container):
    if widget_container is None:
        raise PreventUpdate

    options = ['Look', 'Depression', 'Twist', 'Frequency', 'Polarization', 'RCS', 'Pass', 'Range']
    options = [dict(label=opt, value=opt, disabled=False) for opt in options]

    ctx = callback_context
    uid = ctx.args_grouping.id.index

    return PlotMenuDisplayItemComponent(options, uid).component
