from dash import dcc
import plotly.graph_objects as go

graph_style = {
    'height': '100%',
    'width': '100%'
}

PolarPlot = dcc.Graph(
    id='polar-plot',
    figure=go.Figure(
        data=go.Scatterpolargl(
            dict(
                r=None,
                theta=None,
            )
        ),
        layout=go.Layout(
            autosize=True,
            paper_bgcolor='rgba(0, 0, 0, 0)',
            polar=dict(
                angularaxis=dict(
                    gridcolor='rgba(255, 255, 255, 0.5)',
                    tickcolor='white',
                    tick0=0,
                    dtick=15,
                    ticklabelstep=2,
                    rotation=90,
                    direction='clockwise',
                    linecolor='rgba(255, 255, 255, 0.5)'
                ),
                radialaxis=dict(
                    gridcolor='rgba(255, 255, 255, 0.5)',
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
                color='white',
                size=15
            ),
        )
    ),
    responsive=True,
    config={'scrollZoom': True},
    style=graph_style
)

LinearPlot = dcc.Graph(
    id='linear-plot',
    figure=go.Figure(
        data=go.Scatter(dict(x=None, y=None)),
        layout=go.Layout(
            autosize=True,
            paper_bgcolor='black',
            plot_bgcolor='black',
            font=dict(color='white'),
            yaxis=dict(gridcolor='white'),
            xaxis=dict(gridcolor='white')
        )
    ),
    config={'scrollZoom': True},
    responsive=True,
    style=graph_style
)
