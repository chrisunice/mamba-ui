from abc import abstractmethod

from mamba_ui.components.base import BaseComponent


class BaseWidget(BaseComponent):

    name = 'Base Widget'

    def __init__(self, index: str, name: str = None):
        """ Wrapper for BaseComponent that adds menu as a mandatory property just like component """
        super().__init__(name=name, index=index)

    @property
    @abstractmethod
    def component(self):
        pass

    @property
    @abstractmethod
    def menu(self) -> list:
        pass
