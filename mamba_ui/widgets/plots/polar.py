from dash import dcc
import plotly.graph_objects as go


# Component


def build_polar_plot_widget(unique_id: str):

    graph_style = {
        'height': '100%',
        'width': '100%'
    }

    # Layout based on defaul theme being light
    polar_layout = go.Layout(
        autosize=True,
        paper_bgcolor='rgba(0, 0, 0, 0)',
        polar={
            'angularaxis': {
                'gridcolor': 'gray',
                'linecolor': 'gray',
                'tick0': 0,
                'dtick': 15,
                'ticklabelstep': 2,
                'rotation': 90,
                'direction': 'clockwise'
            },
            'radialaxis': {
                'gridcolor': 'gray',
                'angle': 0,
                'showline': True,
                'linecolor': 'black',
                'linewidth': 2
            },
            'bgcolor': 'rgba(0, 0, 0, 0)'
        },
        font={'color': 'black'},
    )

    return dcc.Graph(
        id={'type': 'polar-plot', 'index': unique_id},
        figure=go.Figure(
            data=go.Scatterpolar({'r': None, 'theta': None}),
            layout=polar_layout
        ),
        responsive=True,
        config={'scrollZoom': True},
        style=graph_style
    )
