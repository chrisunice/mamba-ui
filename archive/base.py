from abc import abstractmethod


class WidgetGridBase:
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def component(self):
        pass
