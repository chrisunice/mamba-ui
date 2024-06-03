from dash import html


class WidgetGridMenuComponent:
    def __init__(self):
        super().__init__()

    @property
    def component(self) -> html.Div:

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
                    id={'type': 'widget-hamburger-button', 'index': ''},
                    className='fa-solid fa-bars fa-xl text-primary',
                    style={'cursor': 'pointer'},
                    title='Widget Menu'
                ),
                html.I(
                    id={'type': 'widget-trash-button', 'index': ''},
                    className='fa-solid fa-trash-can fa-xl text-primary',
                    style={'cursor': 'position'},
                    title='Remove Widget'
                )
            ],
            className='bg-secondary',
            style=menu_bar_style
        )
