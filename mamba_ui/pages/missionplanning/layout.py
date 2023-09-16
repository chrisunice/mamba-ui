from dash import html, dcc

from .input_container import InputContainer
from .output_container import OutputContainer
from mamba_ui.components import VerticalLine
from .download_modal import DownloadModal

page_style = {
    'display': 'flex',
    'flex-direction': 'row',
    'justify-content': 'center',
    'width': '100%',
    'margin': '10px'
}


layout = html.Div(
    id='mission-planning-page',
    children=[
        dcc.Store(id='mission-planning-input-store', storage_type='memory'),
        dcc.Store(id='mission-planning-output-store', storage_type='memory'),
        html.P(id='mission-planning-placeholder', style=dict(display='none')),
        InputContainer,
        VerticalLine('lg'),
        OutputContainer,
        DownloadModal
    ],
    style=page_style
)
