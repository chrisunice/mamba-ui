import dash
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.polar import PolarPlotWidget
from mamba_ui.widgets.plots.linear import LinearPlotWidget
from mamba_ui.grid.container import WidgetGridContainerComponent


@mui.app.callback(
    Output({'type': 'widget-container', 'index': MATCH}, 'children'),
    [
        Input({'type': 'linear-plot-option', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'polar-plot-option', 'index': MATCH}, 'n_clicks'),
        # Input({'type': 'widget-trash-button', 'index': MATCH}, 'n_clicks')
    ]

)
def display_widget(*buttons):
    """
    Displays the user selected widget
    NOTE this could be a backend callback or it could go with the widget-container component
    """
    if all(click is None for click in buttons):
        raise PreventUpdate
    else:
        button_clicked = dash.callback_context.triggered_id['type']
        button_clicked_uid = dash.callback_context.triggered_id['index']
        if button_clicked == 'polar-plot-option':
            return PolarPlotWidget(button_clicked_uid).component
        elif button_clicked == 'linear-plot-option':
            return LinearPlotWidget(button_clicked_uid).component
        # elif button_clicked == 'trash-widget-button':
        #     return WidgetGridContainerComponent()
        else:
            raise PreventUpdate
