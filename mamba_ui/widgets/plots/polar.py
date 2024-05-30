import plotly.graph_objects as go
from dash import dcc, callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH

from mamba_ui import app


# Component


def build_polar_plot_widget(unique_id: str):

    graph_style = {
        'height': '100%',
        'width': '100%'
    }

    polar_layout = go.Layout(
        autosize=True,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        polar=dict(
            angularaxis=dict(
                # gridcolor='rgba(255, 255, 255, 0.5)',
                # tickcolor='white',
                tick0=0,
                dtick=15,
                ticklabelstep=2,
                rotation=90,
                direction='clockwise',
                # linecolor='rgba(255, 255, 255, 0.5)'
            ),
            radialaxis=dict(
                # gridcolor='rgba(255, 255, 255, 0.5)',
                angle=0,
                range=[-50, 20],
                dtick=10,
                tickangle=0,
                showline=True,
                linewidth=2
            ),
            bgcolor='rgba(0, 0, 0, 0)'
        ),
        font=dict(
            # color='white',
            size=15
        ),
    )

    return dcc.Graph(
        id={'type': 'polar-plot', 'index': unique_id},
        figure=go.Figure(
            data=go.Scatterpolargl({'r': None, 'theta': None}),
            layout=polar_layout
        ),
        responsive=True,
        config={'scrollZoom': True},
        style=graph_style
    )


# Callbacks



