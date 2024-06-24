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
    def __init__(self, _index: str = ''):
        super().__init__()
        self._index = _index

    @property
    def component(self) -> html.Div:

        container_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'width': '100%',
            'height': '100%'
        }

        return html.Div(
            children=[
                dbc.Accordion(
                    className='text-dark',
                    children=[
                        html.Div(
                            PlotMenuDataItemComponent(index=self._index).component,
                            id={'type': 'plot-menu-data-container', 'index': self._index}
                        ),
                        html.Div(
                            PlotMenuDisplayItemComponent(index=self._index).component,
                            id={'type': 'plot-menu-display-container', 'index': self._index}
                        ),
                        html.Div(
                            PlotMenuFilterItemComponent(index=self._index).component,
                            id={'type': 'plot-menu-filter-container', 'index': self._index}
                        ),
                        html.Div(
                            PlotMenuDesignItemComponent(index=self._index).component,
                            id={'type': 'plot-menu-design-container', 'index': self._index}
                        ),
                        html.Div(
                            PlotMenuExportItemComponent(index=self._index).component,
                            id={'type': 'plot-menu-export-container', 'index': self._index}
                        )
                    ],
                    always_open=True,
                ),
                SubmitButtonGroupComponent(name='widget', index=self._index).component
            ],
            style=container_style
        )
