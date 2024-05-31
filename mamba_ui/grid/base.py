from abc import ABC, abstractmethod


class WidgetGridComponentBase(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def component(self):
        pass

    @property
    def json(self) -> dict:
        return self.component.to_plotly_json()
