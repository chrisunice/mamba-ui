"""
this dudes gonna hold the menu bar at the top
the widget container in the middle
    this will switch between the icon and the widget itself
the space at the bottom will also be a div

"""
from dash import html

from mamba_ui.widgets.base import BaseWidget
from mamba_ui.grid.menu import WidgetGridMenuComponent
from mamba_ui.grid.sidebar import WidgetGridSidebarComponent
from mamba_ui.grid.container import WidgetGridContainerComponent


class WidgetGridTileComponent(BaseWidget):
    def __init__(self, index: str = ""):
        """ The entire tile in the widget grid which includes the menu bar and the widget container"""
        super().__init__()
        self.index = index

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

        menu = WidgetGridMenuComponent(self.index)

        return html.Div(
            id={'type': 'grid-tile', 'index': self.index},
            children=[
                menu.component,
                WidgetGridSidebarComponent(menu.min_height, self.index).component,
                WidgetGridContainerComponent(self.index).component,
                html.Div(style=menu.component.style)
            ],
            className='bg-transparent border border-security',
            style=tile_style
        )
