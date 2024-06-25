from dash.exceptions import PreventUpdate
from dash import Input, Output, State, MATCH, callback_context

import mamba_ui as mui
from mamba_ui.grid.sidebar import WidgetGridSidebarComponent


@mui.app.callback(
    [
        Output(
            component_id={'name': 'widget-sidebar', 'index': MATCH},
            component_property='style'
        ),
        Output(
            component_id={'name': 'widget-menubar', 'type': 'hamburger-button', 'index': MATCH},
            component_property='className'
        )
    ],
    [
        Input(
            component_id={'name': 'widget-menubar', 'type': 'hamburger-button', 'index': MATCH},
            component_property='n_clicks'
        )
    ],
    [
        State(
            component_id={'name': 'widget-sidebar', 'index': MATCH},
            component_property='style'
        ),
        State(
            component_id={'name': 'widget-menubar', 'type': 'hamburger-button', 'index': MATCH},
            component_property='className'
        )
    ]
)
def toggle_sidebar(hamburger_clicked: int, sidebar_style: dict, menu_class: str) -> tuple[dict, str]:
    """ Handles the opening and close of the widget tile's sidebar """
    if callback_context.triggered_id is None or hamburger_clicked is None:
        raise PreventUpdate
    else:
        if 'fa-bars' in menu_class:
            # Open the sidebar
            sidebar_style.update({'width': WidgetGridSidebarComponent.width_open})
            menu_class = menu_class.replace('fa-bars', 'fa-xmark')
        elif 'fa-xmark' in menu_class:
            # Close the sidebar
            sidebar_style.update({'width': WidgetGridSidebarComponent.width_closed})
            menu_class = menu_class.replace('fa-xmark', 'fa-bars')
        else:
            raise PreventUpdate
        return sidebar_style, menu_class
