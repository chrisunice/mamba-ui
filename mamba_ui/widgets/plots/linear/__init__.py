from dash import dcc
import plotly.graph_objects as go

from mamba_ui.widgets.plots.base import BasePlotWidget


class LinearPlotWidget(BasePlotWidget):

    widget_name = 'Linear Plot'

    def __init__(self, index: str = ''):
        super().__init__(index)

    @property
    def component(self) -> dcc.Graph:

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
            id={'type': 'linear-plot', 'index': self.index},
            figure=go.Figure(
                data=go.Scatter({'x': None, 'y': None}),
                layout=linear_layout
            ),
            config={'scrollZoom': True},
            responsive=True,
            style=graph_style
        )
