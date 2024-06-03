"""
this dudes gonna hold the menu bar at the top
the widget container in the middle
    this will switch between the icon and the widget itself
the space at the bottom will also be a div

"""
from dash import html

from mamba_ui.grid.menu import WidgetGridMenuComponent
from mamba_ui.grid.container import WidgetGridContainerComponent


class WidgetGridTileComponent:
    def __init__(self):
        """ The entire tile in the widget grid which includes the menu bar and the widget container"""
        super().__init__()
        pass

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
        }

        return html.Div(
            id={'type': 'grid-tile', 'index': ''},
            children=[
                WidgetGridMenuComponent().component,
                WidgetGridContainerComponent().component,
                html.Div(style=WidgetGridMenuComponent().component.style)
            ],
            className='bg-transparent border border-security',
            style=tile_style
        )
