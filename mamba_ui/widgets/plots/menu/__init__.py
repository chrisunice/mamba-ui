from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.components.submit_button_group import SubmitButtonGroupComponent
from mamba_ui.widgets.plots.menu.items.data import PlotMenuDataItemComponent
from mamba_ui.widgets.plots.menu.items.filter import PlotMenuFilterItemComponent
from mamba_ui.widgets.plots.menu.items.design import PlotMenuDesignItemComponent
from mamba_ui.widgets.plots.menu.items.export import PlotMenuExportItemComponent


class PlotMenuComponent(BaseComponent):
    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

    @property
    def component(self) -> html.Div:

        container_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
            'height': '100%'
        }

        accordion_style = {
            # 'width': '100%'
        }

        return html.Div(
            children=[
                dbc.Accordion(
                    className='text-dark',
                    children=[
                        PlotMenuDataItemComponent(self.index).component,
                        PlotMenuFilterItemComponent(self.index).component,
                        PlotMenuDesignItemComponent(self.index).component,
                        PlotMenuExportItemComponent(self.index).component
                    ],
                    style=accordion_style
                ),
                SubmitButtonGroupComponent(name='widget', index=self.index).component
            ],
            style=container_style
        )
