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
            'width': '100%',
            'padding': '0px 10px',
            'minHeight': '25px',
            'borderRadius': '5px'
        }

        return html.Div(
            id={'type': 'widget-menu-bar', 'index': ''},
            children=[
                html.I(
                    className='fa-regular fa-circle-xmark fa-lg',
                    style={
                        'color': 'red',
                        'cursor': 'pointer'
                    },
                    title='Remove Widget')
            ],
            className='bg-secondary',
            style=menu_bar_style
        )
