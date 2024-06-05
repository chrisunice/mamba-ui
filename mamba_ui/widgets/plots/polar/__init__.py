from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.plots.polar.component import PolarPlotComponent
from mamba_ui.widgets.plots.polar.menu import PolarPlotMenuComponent


class PolarPlotWidget(BaseWidget):

    widget_name = 'Polar Plot'

    def __init__(self, index: str = ""):
        """

        :param index:
        """
        super().__init__(index)

    @property
    def component(self):
        return PolarPlotComponent(self.index).component

    @property
    def menu(self):
        return PolarPlotMenuComponent(self.index).component
