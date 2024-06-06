from abc import ABC, abstractmethod


class BaseComponent(ABC):

    name = 'Base Component'

    def __init__(self):
        super().__init__()

    @property
    def uid(self):
        """ Unique ID for dash components """
        return '-'.join(self.name.lower().split())

    @property
    @abstractmethod
    def component(self):
        pass


