from abc import abstractmethod

from mamba_ui.components.base import BaseComponent


class BaseWidget(BaseComponent):

    name = 'Base Widget'

    def __init__(self, index: str, name: str = None):
        """
        Wrapper for BaseComponent that adds menu as a mandatory property just like component

        :param index: a unique index that should specify the location of the component
        :param name: the name of the component; if no name is given then the class attribute name will be used
        """
        super().__init__(name=name, index=index)

    @property
    @abstractmethod
    def component(self):
        pass

    @property
    @abstractmethod
    def menu(self) -> list:
        pass
