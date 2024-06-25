from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.plots.polar.component import PolarPlotComponent
from mamba_ui.widgets.plots.polar.menu import PolarPlotMenuComponent


class PolarPlotWidget(BaseWidget):

    name = 'Polar Plot Widget'

    def __init__(self, index: str, name: str = None):
        super().__init__(index=index, name=name)

    @property
    def component(self):
        return PolarPlotComponent(index=self.id.get('index')).component

    @property
    def menu(self):
        return PolarPlotMenuComponent(index=self.id.get('index')).component
