from dash import html

from mamba_ui.components.base import BaseComponent


class WidgetGridMenubarComponent(BaseComponent):

    name = 'Widget Menubar'
    min_height = 50

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

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
            id=self.id,
            children=[
                html.I(
                    id=self.get_child_id('hamburger-button'),
                    className='fa-solid fa-bars fa-xl text-primary',
                    style={'cursor': 'pointer'},
                    title='Widget Menu'
                ),
                html.I(
                    id=self.get_child_id('trash-button'),
                    className='fa-solid fa-trash-can fa-xl text-primary',
                    style={'cursor': 'position'},
                    title='Remove Widget'
                )
            ],
            className='bg-secondary',
            style=menu_bar_style
        )
