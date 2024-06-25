from dash import html

from mamba_ui.components.base import BaseComponent
from mamba_ui.grid.icon import WidgetGridIconComponent


class WidgetGridContainerComponent(BaseComponent):

    name = 'Widget Container'

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

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
            id=self.id,
            className='bg-transparent',
            children=[
                WidgetGridIconComponent(index=self.id.get('index')).component
            ],
            style=container_style
        )
