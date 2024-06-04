from abc import ABC, abstractmethod


class BaseComponent(ABC):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def component(self):
        pass
