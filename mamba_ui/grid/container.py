from dash import html

from mamba_ui.components.base import BaseComponent
from mamba_ui.grid.icon import WidgetGridIconComponent


class WidgetGridContainerComponent(BaseComponent):
    def __init__(self, index: str = ""):
        super().__init__()
        self.index = index

    @property
    def component(self) -> html.Div:

        container_style = {
            'display': 'flex',
            'justifyContent': 'center', 
            'alignItems': 'center',
            'width': '100%',
            'height': '100%',
        }

        return html.Div(
            id={'type': 'widget-container', 'index': self.index},
            className='bg-transparent',
            children=[WidgetGridIconComponent(self.index).component],
            style=container_style
        )
