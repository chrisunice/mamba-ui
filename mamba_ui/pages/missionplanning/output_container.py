from dash import html

from mamba_ui.components import HorizontalLine
from .container_title import container_title as ContainerTitle
from mamba_ui import STANDARD_WIDTH

col_style = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'width': '50%',
    'max-width': STANDARD_WIDTH/2,
    'padding': '10px',
    'margin-left': '5px',
    # 'background-color': 'rgba(0, 0, 255, 0.25)'
}

log_style = {
    'display': 'flex',
    'flex': '1',
    'width': '80%',
    'border': '5px ridge white',
    'background': 'lightgray'
}

OutputContainer = html.Div(
    id='col-right',
    children=[
        ContainerTitle('Output'),
        HorizontalLine('lg'),
        html.Div(
            id='output-log',
            style=log_style
        )
    ],
    style=col_style
)
