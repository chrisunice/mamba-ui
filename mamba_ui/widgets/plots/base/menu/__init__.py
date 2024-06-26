from dash import html
import dash_bootstrap_components as dbc

# generic components
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.submit_button_group import SubmitButtonGroupComponent

# widget components
from mamba_ui.widgets.plots.base.menu.data import PlotMenuDataItemComponent
from mamba_ui.widgets.plots.base.menu.display import PlotMenuDisplayItemComponent
from mamba_ui.widgets.plots.base.menu.filter import PlotMenuFilterItemComponent
from mamba_ui.widgets.plots.base.menu.design import PlotMenuDesignItemComponent
from mamba_ui.widgets.plots.base.menu.export import PlotMenuExportItemComponent


class BasePlotMenuComponent(BaseComponent):

    name = 'Base Plot Menu'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)

    @property
    def component(self) -> html.Div:

        container_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
            'height': '100%'
        }

        index = self.id.get('index')

        return html.Div(
            children=[
                dbc.Accordion(
                    children=[
                        html.Div(
                            id=self.get_child_id('data-container'),
                            children=[PlotMenuDataItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('display-container'),
                            children=[PlotMenuDisplayItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('filter-container'),
                            children=[PlotMenuFilterItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('design-container'),
                            children=[PlotMenuDesignItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('export-container'),
                            children=[PlotMenuExportItemComponent(index=index).component]
                        )
                    ],
                    className='text-dark',
                    always_open=True
                ),
                SubmitButtonGroupComponent(name='plot-menu-submit-button-group', index=index).component
            ],
            style=container_style
        )
