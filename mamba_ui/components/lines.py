from dash import html
from abc import ABC, abstractmethod

from mamba_ui.components.base import BaseComponent


class LineComponent(BaseComponent, ABC):

    weights = {'sm': '1px', 'md': '2.5px', 'lg': '4px'}

    def __init__(self, weight_name: str, name: str = None, index: str = None):
        super().__init__(name, index)
        try:
            self.weight_px = self.weights[weight_name]
        except KeyError:
            raise KeyError(f"Valid inputs are {list(self.weights.keys())}. Received {weight_name}")
        else:
            self.weight_name = weight_name

    @property
    @abstractmethod
    def component(self):
        pass


class HorizontalLineComponent(LineComponent):

    name = 'Horizontal Line'

    def __init__(self, weight: str = 'sm', name: str = None, index: str = None):
        super().__init__(weight, name, index)

    @property
    def component(self) -> html.Hr:

        horizontal_style = {
            'width': '100%',
            'height': self.weight_px
        }

        return html.Hr(id=self.id, style=horizontal_style)


class VerticalLineComponent(LineComponent):

    name = 'Vertical Line'

    def __init__(self, weight: str = 'sm', name: str = None, index: str = None):
        super().__init__(weight, name, index)

    @property
    def component(self):

        vertical_style = {
            'width': self.weight_px,
            'height': 'auto',
        }

        return html.Hr(id=self.id, style=vertical_style)
