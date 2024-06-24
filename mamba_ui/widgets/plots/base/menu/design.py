from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class PlotMenuDesignItemComponent(BaseComponent):

    name = 'Plot Menu Design'

    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index
        self.id = {
            'parent-component': self.uid,
            'index': self.index
        }

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[],
            title=html.H4('Design')
        )
