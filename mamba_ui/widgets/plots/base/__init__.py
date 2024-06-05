from abc import abstractmethod

from mamba_ui.widgets.base import BaseWidget
from mamba_ui.widgets.plots.base.menu import BasePlotMenuComponent
from mamba_ui.widgets.plots.base.component import BasePlotComponent


class BasePlotWidget(BaseWidget):

    widget_name = 'Base Plot'

    def __init__(self, index: str = ''):
        super().__init__(index)

    @property
    def component(self):
        """ To be implemented by actual plotting widgets """
        return BasePlotComponent(self.index).component

    @property
    def menu(self):
        """ Common menu items used between plots """
        return BasePlotMenuComponent(self.index).component
