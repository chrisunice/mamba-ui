from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class PlotMenuDesignItemComponent(BaseComponent):
    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[],
            title=html.H4('Design')
        )
