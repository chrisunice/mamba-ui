from dash import dcc, html
import plotly.graph_objects as go

from mamba_ui.components.base import BaseComponent


class LinearPlotComponent(BaseComponent):

    name = 'Linear Plot'

    def __init__(self, index: str, name: str = None):
        super().__init__(name, index)

    @property
    def _graph(self) -> dcc.Graph:
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
            id=self.get_child_id('graph'),
            figure=go.Figure(
                data=go.Scatter({'x': None, 'y': None}),
                layout=linear_layout
            ),
            config={'scrollZoom': True},
            responsive=True,
            style=graph_style
        )

    @property
    def component(self) -> html.Div:
        component_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'width': '100%',
            'height': '100%'
        }

        return html.Div(
            children=[
                self._graph
            ],
            style=component_style
        )