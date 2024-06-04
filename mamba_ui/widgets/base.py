from abc import ABC, abstractmethod

from mamba_ui.utils.component2json import component2json


class BaseWidget(ABC):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def component(self):
        pass

    def to_plotly_json(self) -> dict:
        return component2json(self.component)
