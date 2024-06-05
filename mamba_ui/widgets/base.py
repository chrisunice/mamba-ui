from abc import ABC, abstractmethod

from mamba_ui.components.base import BaseComponent


class BaseWidget(BaseComponent):

    widget_name: str = 'base'

    def __init__(self, index: str):
        super().__init__()
        self.index = index

    @property
    @abstractmethod
    def component(self):
        pass

    @property
    @abstractmethod
    def menu(self) -> list:
        pass
