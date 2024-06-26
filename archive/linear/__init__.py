from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.plots.linear.component import LinearPlotComponent
from mamba_ui.widgets.plots.linear.menu import LinearPlotMenuComponent


class LinearPlotWidget(BaseWidget):

    name = 'Linear Plot Widget'

    def __init__(self, index: str):
        super().__init__(index)
        self.index = index

    @property
    def component(self):
        return LinearPlotComponent(self.index).component

    @property
    def menu(self):
        return LinearPlotMenuComponent(self.index).component
