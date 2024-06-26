from dash import html, dcc

from mamba_ui.components import HorizontalLine
from .container_title import container_title as ContainerTitle
from mamba_ui import STANDARD_WIDTH

col_style = {
    'display': 'flex',
    'flexDirection': 'column',
    'align-items': 'center',
    'width': '50%',
    'max-width': STANDARD_WIDTH/2,
    'padding': '10px',
    'marginLeft': '5px',
}

log_style = {
    'display': 'flex',
    'flex': '1',
    'width': '80%',
    'border': '5px ridge white',
    'background': 'lightgray',
    'color': 'black',
}

OutputContainer = html.Div(
    id='col-right',
    children=[
        ContainerTitle('Output'),
        HorizontalLine('lg'),
        dcc.Interval(id='output-interval', interval=1000),
        dcc.Textarea(id='output-log', disabled=True, style=log_style),
    ],
    style=col_style
)
