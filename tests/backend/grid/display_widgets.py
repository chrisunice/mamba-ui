from dash.exceptions import PreventUpdate
from dash import html, callback_context, Input, Output, State, MATCH

import mamba_ui as mui
from mamba_ui.widgets.plots.polar import PolarPlotWidget
from mamba_ui.widgets.plots.linear import LinearPlotWidget
from mamba_ui.widgets.imagery.viewer import ImageryViewerWidget


@mui.app.callback(
    [
        Output(
            component_id={'name': 'widget-container', 'index': MATCH},
            component_property='children'
        ),
        Output(
            component_id={'name': 'widget-sidebar', 'type': 'menu-container', 'index': MATCH},
            component_property='children'
        ),
        Output(
            component_id={'name': 'widget-icon', 'type': 'dropdown-menu', 'index': MATCH},
            component_property='style'
        ),
    ],
    [
        Input(
            component_id={'name': 'widget-icon', 'type': 'linear-plot-option', 'index': MATCH},
            component_property='n_clicks'
        ),
        Input(
            component_id={'name': 'widget-icon', 'type': 'polar-plot-option', 'index': MATCH},
            component_property='n_clicks'
        ),
        Input(
            component_id={'name': 'widget-icon', 'type': 'imagery-viewer-option', 'index': MATCH},
            component_property='n_clicks'
        ),
        Input(
            component_id={'name': 'widget-menubar', 'type': 'trash-button', 'index': MATCH},
            component_property='n_clicks'
        ),
    ],
    [
        State(
            component_id={'name': 'widget-container', 'index': MATCH},
            component_property='children'
        ),
        State(
            component_id={'name': 'widget-icon', 'type': 'dropdown-menu', 'index': MATCH},
            component_property='style'
        )
    ]
)
def display_widget(*args):
    """
    Displays the user selected widget
    """
    if callback_context.triggered_id is None:
        raise PreventUpdate
    else:
        # Get which button in the container was clicked
        button_clicked = callback_context.triggered_id['type']
        button_clicked_uid = callback_context.triggered_id['index']

        # Get the container children and dropdown menu style
        container, dropdown_style = args[-2:]

        if button_clicked == 'polar-plot-option':
            widget = PolarPlotWidget(button_clicked_uid)
            container.append(widget.component)
            dropdown_style.update({'display': 'none'})
            return container, widget.menu, dropdown_style

        elif button_clicked == 'linear-plot-option':
            widget = LinearPlotWidget(button_clicked_uid)
            container.append(widget.component)
            dropdown_style.update({'display': 'none'})
            return container, widget.menu, dropdown_style

        elif button_clicked == 'imagery-viewer-option':
            widget = ImageryViewerWidget(button_clicked_uid)
            container.append(widget.component)
            dropdown_style.update({'display': 'none'})
            return container, widget.menu, dropdown_style

        elif button_clicked == 'trash-button':
            container = container[:1]
            default_menu = html.H4('Build some menu components', className='text-dark')
            dropdown_style.update({'display': 'flex'})
            return container, default_menu, dropdown_style

        else:
            raise PreventUpdate
