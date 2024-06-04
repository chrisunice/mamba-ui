import dash
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.polar import PolarPlotWidget
from mamba_ui.widgets.plots.linear import LinearPlotWidget


@mui.app.callback(
    Output({'type': 'widget-container', 'index': MATCH}, 'children'),
    Output({'type': 'widget-dropdown-menu', 'index': MATCH}, 'style'),
    [
        Input({'type': 'linear-plot-option', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'polar-plot-option', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'widget-trash-button', 'index': MATCH}, 'n_clicks')
    ],
    [
        State({'type': 'widget-container', 'index': MATCH}, 'children'),
        State({'type': 'widget-dropdown-menu', 'index': MATCH}, 'style')
    ]
)
def display_widget(*args):
    """
    Displays the user selected widget
    """
    if dash.callback_context.triggered_id is None:
        raise PreventUpdate
    else:
        # Get which button in the container was clicked
        button_clicked = dash.callback_context.triggered_id['type']
        button_clicked_uid = dash.callback_context.triggered_id['index']

        # Get the container children and dropdown menu style
        container, dropdown_style = args[-2:]

        if button_clicked == 'polar-plot-option':
            container.append(PolarPlotWidget(button_clicked_uid).component)
            dropdown_style.update({'display': 'none'})
            return container, dropdown_style

        elif button_clicked == 'linear-plot-option':
            container.append(LinearPlotWidget(button_clicked_uid).component)
            dropdown_style.update({'display': 'none'})
            return container, dropdown_style

        elif button_clicked == 'widget-trash-button':
            container = container[:1]
            dropdown_style.update({'display': 'flex'})
            return container, dropdown_style

        else:
            raise PreventUpdate
