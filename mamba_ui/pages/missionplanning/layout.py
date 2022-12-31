from dash import html, dcc

from .input_container import InputContainer
from .output_container import OutputContainer
from mamba_ui.components import VerticalLine

page_style = {
    'display': 'flex',
    'flex-direction': 'row',
    'justify-content': 'center',
    'width': '100%',
    # 'background-color': 'rgba(255, 0, 0, 0.25)',
    'margin': '10px'
}


layout = html.Div(
    id='mission-planning-page',
    children=[
        dcc.Store(id='mission-planning-store', storage_type='memory'),
        InputContainer,
        VerticalLine('lg'),
        OutputContainer
    ],
    style=page_style
)
