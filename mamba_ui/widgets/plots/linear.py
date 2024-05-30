import plotly.graph_objects as go
from dash import dcc, callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

from mamba_ui import app


# Component


def build_linear_plot_widget(unique_id: str):

    graph_style = {
        'height': '100%',
        'width': '100%'
    }

    # Layout based on default theme being light
    linear_layout = go.Layout(
        autosize=True,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        font={'color': 'black'},
        yaxis={
            'gridcolor': 'gray',
            'zerolinecolor': 'black',
            'zerolinewidth': 2
        },
        xaxis={
            'gridcolor': 'gray',
            'zerolinecolor': 'black',
            'zerolinewidth': 2
        }
    )

    return dcc.Graph(
        id={'type': 'linear-plot', 'index': unique_id},
        figure=go.Figure(
            data=go.Scatter({'x': None, 'y': None}),
            layout=linear_layout
        ),
        config={'scrollZoom': True},
        responsive=True,
        style=graph_style
    )


# Callbacks



