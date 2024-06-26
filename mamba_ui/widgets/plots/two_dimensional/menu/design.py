from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class TwoDimensionalPlotMenuDesignItemComponent(BaseComponent):

    name = '2D Plot Menu Design'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[],
            title=html.H4('Design')
        )
