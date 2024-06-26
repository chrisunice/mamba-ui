from dash.exceptions import PreventUpdate
from dash import Input, Output, State, MATCH, callback_context

import mamba_ui as mui
from mamba_ui.grid.sidebar import WidgetGridSidebarComponent


@mui.app.callback(
    [
        Output(
            component_id={'name': 'widget-sidebar', 'index': MATCH},
            component_property='style',
            allow_duplicate=True
        ),
        Output(
            component_id={'name': 'widget-menubar', 'type': 'hamburger-button', 'index': MATCH},
            component_property='className',
            allow_duplicate=True
        ),
    ],
    Input(
        component_id={'name': 'plot-menu-submit-button-group', 'type': 'submit', 'index': MATCH},
        component_property='n_clicks'
    ),
    [
        State(
            component_id={'name': 'widget-sidebar', 'index': MATCH},
            component_property='style'
        ),
        State(
            component_id={'name': 'widget-menubar', 'type': 'hamburger-button', 'index': MATCH},
            component_property='className'
        ),
    ],
    prevent_initial_call=True
)
def close_sidebar_on_submit(submit_click: int, sidebar_style: dict, menu_class: str):
    if callback_context.triggered_id is None or submit_click is None:
        raise PreventUpdate

    # Close the sidebar
    sidebar_style.update({'width': WidgetGridSidebarComponent.width_closed})

    # Fix the menu icon
    menu_class = menu_class.replace('fa-xmark', 'fa-bars')

    return sidebar_style, menu_class
