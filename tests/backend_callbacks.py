import dash
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

import mamba_ui as mui
from mamba_ui.widgets import LinearPlotWidget, PolarPlotWidget


@mui.app.callback(
    Output({'type': 'widget-container', 'index': MATCH}, 'children'),
    [
        Input({'type': 'linear-plot-option', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'polar-plot-option', 'index': MATCH}, 'n_clicks')

    ]

)
def display_widget(*widgets):
    """
    Displays the user selected widget
    NOTE this could be a backend callback or it could go with the widget-container component
    """
    if all(click is None for click in widgets):
        raise PreventUpdate
    else:
        widget_clicked_name = dash.callback_context.triggered_id['type']
        widget_clicked_uid = dash.callback_context.triggered_id['index']
        if widget_clicked_name == 'polar-plot-option':
            return PolarPlotWidget(widget_clicked_uid)
        elif widget_clicked_name == 'linear-plot-option':
            return LinearPlotWidget(widget_clicked_uid)
        else:
            raise PreventUpdate
