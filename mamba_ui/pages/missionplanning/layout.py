from dash import html, dcc

from .input_container import InputContainer
from .output_container import OutputContainer
from mamba_ui.components import VerticalLine
from .download_modal import DownloadModal
from .input_alert import InputAlert

page_style = {
    'display': 'flex',
    'flexDirection': 'row',
    'justify-content': 'center',
    'width': '100%',
    'margin': '10px'
}


layout = html.Div(
    id='mission-planning-page',
    children=[
        dcc.Store(id='mission-planning-input-store', storage_type='memory'),
        dcc.Store(id='mission-planning-output-store', storage_type='memory'),
        InputContainer,
        VerticalLine('lg'),
        OutputContainer,
        DownloadModal,
        InputAlert
    ],
    style=page_style
)
