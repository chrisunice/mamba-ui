from dash import html

from mamba_ui.grid.base import WidgetGridComponentBase


class WidgetGridMenuComponent(WidgetGridComponentBase):
    def __init__(self):
        super().__init__()

    @property
    def component(self):

        menu_bar_style = {
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'space-between',
            'width': '100%',
            'padding': '0px 10px',
            'minHeight': '50px',
            'borderRadius': '5px'
        }

        return html.Div(
            id={'type': 'widget-menu-bar', 'index': ''},
            children=[
                html.I(
                    className='fa-solid fa-bars fa-xl text-primary',
                    style={'cursor': 'pointer'},
                    title='Widget Menu'
                ),
                html.I(
                    className='fa-solid fa-trash-can fa-xl text-primary',
                    style={'cursor': 'position'},
                    title='Remove Widget'
                )
            ],
            className='bg-secondary',
            style=menu_bar_style
        )
