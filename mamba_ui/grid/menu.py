from dash import html

from mamba_ui.grid.base import WidgetGridBase


class WidgetGridMenuComponent(WidgetGridBase):

    min_height = 50

    def __init__(self, index: str = ""):
        super().__init__()
        self.index = index

    @property
    def component(self):

        menu_bar_style = {
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'space-between',
            'width': '100%',
            'padding': '0px 10px',
            'minHeight': f'{self.min_height}px',
            'borderRadius': '5px'
        }

        return html.Div(
            id={'type': 'widget-menu-bar', 'index': self.index},
            children=[
                html.I(
                    id={'type': 'widget-hamburger-button', 'index': self.index},
                    className='fa-solid fa-bars fa-xl text-primary',
                    style={'cursor': 'pointer'},
                    title='Widget Menu'
                ),
                html.I(
                    id={'type': 'widget-trash-button', 'index': self.index},
                    className='fa-solid fa-trash-can fa-xl text-primary',
                    style={'cursor': 'position'},
                    title='Remove Widget'
                )
            ],
            className='bg-secondary',
            style=menu_bar_style
        )
