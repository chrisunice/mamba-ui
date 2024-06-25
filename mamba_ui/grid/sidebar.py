from dash import html

from mamba_ui.components.base import BaseComponent
from mamba_ui.components.lines import HorizontalLineComponent


class WidgetGridSidebarComponent(BaseComponent):

    name = 'Widget Sidebar'
    width_open = 'max(25%, 350px)'
    width_closed = 0

    def __init__(self, top_offset, name: str = None, index: str = None):
        super().__init__(name, index)
        self.top_offset = top_offset

    @property
    def _menu_container(self):
        """ This container will hold the user defined components for any given widget """

        style = {
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'height': '100%',
            'width': '100%',
            'padding': '10px'
        }

        return html.Div(
            id=self.get_child_id('menu-container'),
            children=[html.H4('Build some menu items', className='text-dark')],
            style=style
        )

    @property
    def component(self):

        sidebar_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'position': 'absolute',
            'top': f'{self.top_offset}px',
            'left': 0,
            'width': f'{self.width_closed}',
            'height': f'calc(100% - {self.top_offset}px)',
            'zIndex': 1000,
            'padding': '10px 0px',
            'boxShadow': '10px 0px 10px gray',
            'transition': 'width 0.5s',
            'overflow': 'hidden'
        }

        return html.Div(
            id=self.id,
            className='sidebar-visible bg-light',
            children=[
                html.H3('Menu', className='text-dark', style={'margin': 0}),
                HorizontalLineComponent('md').component,
                self._menu_container,
            ],
            style=sidebar_style
        )
