from dash import html
from abc import ABC, abstractmethod

from mamba_ui.components.base import BaseComponent


class LineComponent(BaseComponent, ABC):

    weights = {'sm': '1px', 'md': '2.5px', 'lg': '4px'}

    def __init__(self, weight_name: str):
        super().__init__()
        try:
            self.weight_px = self.weights[weight_name]
        except KeyError:
            raise KeyError(f"Valid inputs are {list(self.weights.keys())}. Received {self.weight_name}")
        else:
            self.weight_name = weight_name

    @property
    @abstractmethod
    def component(self):
        pass


class HorizontalLineComponent(LineComponent):

    def __init__(self, weight: str = 'sm'):
        super().__init__(weight)

    @property
    def component(self) -> html.Hr:

        horizontal_style = {
            'width': '100%',
            'height': self.weight_px
        }

        return html.Hr(style=horizontal_style)


class VerticalLineComponent(LineComponent):
    def __init__(self, weight: str = 'sm'):
        super().__init__(weight)

    @property
    def component(self):

        vertical_style = {
            'width': self.weight_px,
            'height': 'auto',
        }

        return html.Hr(style=vertical_style)
