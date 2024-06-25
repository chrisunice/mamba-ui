from dash import html

from mamba_ui.components.base import BaseComponent
from mamba_ui.grid.menu import WidgetGridMenubarComponent
from mamba_ui.grid.sidebar import WidgetGridSidebarComponent
from mamba_ui.grid.container import WidgetGridContainerComponent


class WidgetGridTileComponent(BaseComponent):

    name = 'Widget Grid Tile'

    def __init__(self, name: str = None, index: str = None):
        """ The entire tile in the widget grid which includes the menu bar and the widget container"""
        super().__init__(name, index)

    @property
    def component(self) -> html.Div:

        tile_style = {
            'display': 'flex',
            'width': '100%',
            'height': '100%',
            'flexDirection': 'column',
            'justifyContent': 'space-between',
            'alignItems': 'center',
            'margin': '0px 5px 0px 5px',
            'padding': '0px',
            'borderRadius': '5px',
            'backgroundColor': 'rgba(0, 0, 0, 0)',
            'boxShadow': '0px 0px 10px gray',
            'position': 'relative',
        }

        index = self.id.get('index')
        menubar = WidgetGridMenubarComponent(index=index)
        sidebar = WidgetGridSidebarComponent(top_offset=menubar.min_height, index=index)
        container = WidgetGridContainerComponent(index=index)

        return html.Div(
            id=self.id,
            children=[
                menubar.component,
                sidebar.component,
                container.component,
                html.Div(style=menubar.component.style)
            ],
            className='bg-transparent border border-security',
            style=tile_style
        )
