from dash import html
import dash_bootstrap_components as dbc

# generic components
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.submit_button_group import SubmitButtonGroupComponent

# widget components
from mamba_ui.widgets.plots.two_dimensional.menu.data import TwoDimensionalPlotMenuDataItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.display import TwoDimensionalPlotMenuDisplayItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.filter import TwoDimensionalPlotMenuFilterItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.design import TwoDimensionalPlotMenuDesignItemComponent
from mamba_ui.widgets.plots.two_dimensional.menu.export import TwoDimensionalPlotMenuExportItemComponent


class TwoDimensionalPlotMenuComponent(BaseComponent):

    name = '2D Plot Menu'

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
                            children=[TwoDimensionalPlotMenuDataItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('display-container'),
                            children=[TwoDimensionalPlotMenuDisplayItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('filter-container'),
                            children=[TwoDimensionalPlotMenuFilterItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('design-container'),
                            children=[TwoDimensionalPlotMenuDesignItemComponent(index=index).component]
                        ),
                        html.Div(
                            id=self.get_child_id('export-container'),
                            children=[TwoDimensionalPlotMenuExportItemComponent(index=index).component]
                        )
                    ],
                    className='text-dark',
                    always_open=True
                ),
                SubmitButtonGroupComponent(name='2d-plot-menu-submit-button-group', index=index).component
            ],
            style=container_style
        )
