from abc import abstractmethod

from mamba_ui.widgets.base import BaseWidget
from mamba_ui.widgets.plots.menu import PlotMenuComponent


class BasePlotWidget(BaseWidget):

    widget_name = 'Base Plot'

    def __init__(self, index: str = ''):
        super().__init__(index)

    @property
    @abstractmethod
    def component(self):
        """ To be implemented by actual plotting widgets """
        pass

    @property
    def menu(self):
        """ Common menu items used between plots """
        return PlotMenuComponent(self.index).component
