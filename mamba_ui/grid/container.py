from dash import html

from mamba_ui.grid.icon import WidgetGridIconComponent


class WidgetGridContainerComponent:
    def __init__(self):
        super().__init__()

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
            id={'type': 'widget-container', 'index': ''},
            className='bg-transparent',
            children=[WidgetGridIconComponent().component],
            style=container_style
        )
