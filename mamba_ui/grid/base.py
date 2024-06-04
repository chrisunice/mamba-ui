from abc import abstractmethod
from mamba_ui.widgets.base import BaseWidget


class WidgetGridBase(BaseWidget):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def component(self):
        pass
