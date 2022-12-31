from dash import html
from mamba_ui.components import TabBar
from mamba_ui.components import DataBar
from mamba_ui.components.plots import PolarPlot

page_styles = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'width': '100%',
    'padding': '10px',
}

row1_styles = {
    'width': '75%'
}

row2_styles = {
    'display': 'flex',
    'flex': '1',
    'align-items': 'center',
    'justify-content': 'center',
    'width': '90%',
    'margin': '10px',
}

layout = html.Div(
    id='data-vis-page',
    children=[
        DataBar,
        html.Div(id='row-1', children=[TabBar], style=row1_styles),
        html.Div(id='row-2', children=[PolarPlot], style=row2_styles)
    ],
    style=page_styles
)
