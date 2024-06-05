from dash import html
import dash_bootstrap_components as dbc

# generic components
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.submit_button_group import SubmitButtonGroupComponent

# widget components
from mamba_ui.widgets.plots.base.menu.items.data import PlotMenuDataItemComponent
from mamba_ui.widgets.plots.base.menu.items.filter import PlotMenuFilterItemComponent
from mamba_ui.widgets.plots.base.menu.items.design import PlotMenuDesignItemComponent
from mamba_ui.widgets.plots.base.menu.items.export import PlotMenuExportItemComponent


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
                        PlotMenuDataItemComponent(self._index).component,
                        PlotMenuFilterItemComponent(self._index).component,
                        PlotMenuDesignItemComponent(self._index).component,
                        PlotMenuExportItemComponent(self._index).component
                    ],
                    always_open=True,
                ),
                SubmitButtonGroupComponent(name='widget', index=self._index).component
            ],
            style=container_style
        )
