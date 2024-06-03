from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.widgets.plots.polar import PolarPlotWidget
from mamba_ui.widgets.plots.linear import LinearPlotWidget


class WidgetGridIconComponent:
    def __init__(self):
        super().__init__()

    @property
    def component(self) -> dbc.DropdownMenu:

        menu_label_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'height': '100%'
        }

        menu_label = html.Div(
            children=[
                html.I(className='fa-solid fa-circle-plus fa-2xl text-dark', style={'marginBottom': '1.25rem'}),
                dbc.Label('Add a Widget', className='text-dark')
            ],
            style=menu_label_style
        )

        return dbc.DropdownMenu(
            className='widget-dropdown-menu',
            label=menu_label,
            children=[
                self.create_menu_item(LinearPlotWidget.widget_name),
                self.create_menu_item(PolarPlotWidget.widget_name)
            ],
            size='lg',
            toggle_style={
                'background': 'transparent',
                'border': 'none'
            },
            caret=False,
            style={
                'display': 'flex',
            }
        )

    @staticmethod
    def create_menu_item(widget_name: str) -> dbc.DropdownMenuItem:
        """ Converts a widget to a menu item"""
        widget_type = '-'.join(widget_name.lower().split())
        return dbc.DropdownMenuItem(
            widget_name,
            id={'type': f'{widget_type}-option', 'index': ''}
        )
