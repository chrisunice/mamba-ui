from dash import dcc, html
import plotly.graph_objects as go

from mamba_ui.components.base import BaseComponent


class PolarPlotComponent(BaseComponent):

    name = 'Polar Plot'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)

    @property
    def _graph(self):
        graph_style = {
            'height': '100%',
            'width': '100%'
        }

        # Layout based on default theme being light
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
            id=self.get_child_id('graph'),
            figure=go.Figure(
                data=go.Scatterpolar({'r': None, 'theta': None}),
                layout=polar_layout
            ),
            responsive=True,
            config={'scrollZoom': True},
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


