import os
from dash import html
import dash_bootstrap_components as dbc

# Generic components
from mamba_ui import config
from mamba_ui.components import HorizontalLine
from mamba_ui.components import SubmitButtonGroup

# Imagery page components
from .SidebarInputItem import sidebar_input_item
from .SidebarDropdownItem import sidebar_dropdown_item

sidebar_style = {
    'margin-top': '50px',
    'width': '300px'
}

container_style = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center'
}

Sidebar = dbc.Offcanvas(
    id='imagery-sidebar',
    children=[
        html.Div(
            children=[
                html.H5('Query Filter'),
                HorizontalLine,
                sidebar_dropdown_item(
                    label_text='SQL Database',
                    options=[{'label': os.path.basename(config['imagery']['database_path']),
                              'value': config['imagery']['database_path']}]
                ),
                HorizontalLine,
                sidebar_dropdown_item('Platform', multi=True),
                HorizontalLine,
                sidebar_dropdown_item('Band', multi=True),
                HorizontalLine,
                sidebar_dropdown_item('Polarization', multi=True),
                HorizontalLine,
                sidebar_input_item('Look'),
                HorizontalLine,
                sidebar_input_item('Depression')
            ],
            style=container_style
        ),
        SubmitButtonGroup('imagery-sidebar')
    ],
    scrollable=False,
    is_open=False,
    backdrop=False,
    placement='end',
    close_button=False,
    style=sidebar_style
)
