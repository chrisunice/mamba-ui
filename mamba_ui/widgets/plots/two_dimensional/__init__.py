from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.plots.two_dimensional.component import TwoDimensionalPlotComponent
from mamba_ui.widgets.plots.two_dimensional.menu import TwoDimensionalPlotMenuComponent


class TwoDimensionalPlotWidget(BaseWidget):

    name = '2D Plot Widget'

    def __init__(self, index: str, name: str = None):
        super().__init__(index=index, name=name)

    @property
    def component(self):
        return TwoDimensionalPlotComponent(self.id.get('index')).component

    @property
    def menu(self):
        return TwoDimensionalPlotMenuComponent(self.id.get('index')).component
