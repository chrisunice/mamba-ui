from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.grid.base import WidgetGridBase
from mamba_ui.widgets import PolarPlotWidget
from mamba_ui.widgets import LinearPlotWidget


class WidgetIconComponent(WidgetGridBase):
    def __init__(self, row_id: int = 0, column_id: int = 0):
        super().__init__()
        self.row_id = row_id
        self.column_id = column_id

    @property
    def component(self):
        uid = f'r{self.row_id}c{self.column_id}'

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
                self.widget2menuitem(LinearPlotWidget(uid)),
                self.widget2menuitem(PolarPlotWidget(uid))
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
    def widget2menuitem(widget) -> dict:
        """ Converts a widget to a menu item"""
        widget_type = widget.id['type']
        widget_uid = widget.id['index']
        widget_name = ' '.join(map(lambda x: x.capitalize(), widget_type.split('-')))
        menu_item_component = dbc.DropdownMenuItem(widget_name, id={'type': f'{widget_type}-option', 'index': widget_uid})
        menu_item_json = menu_item_component.to_plotly_json()
        return menu_item_json
