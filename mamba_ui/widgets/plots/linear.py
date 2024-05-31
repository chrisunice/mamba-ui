from dash import dcc
import plotly.graph_objects as go

# Component


class LinearPlotWidget:

    widget_name = 'Linear Plot'

    def __init__(self, unique_id: str = ''):
        self.uid = unique_id

    @property
    def component(self):

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
            id={'type': 'linear-plot', 'index': self.uid},
            figure=go.Figure(
                data=go.Scatter({'x': None, 'y': None}),
                layout=linear_layout
            ),
            config={'scrollZoom': True},
            responsive=True,
            style=graph_style
        )
