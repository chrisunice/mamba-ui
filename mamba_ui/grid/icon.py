from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.widgets.plots.polar import PolarPlotWidget
from mamba_ui.widgets.plots.linear import LinearPlotWidget
from mamba_ui.widgets.imagery.viewer import ImageryViewerWidget


class WidgetGridIconComponent(BaseComponent):

    name = 'Widget Icon'

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

    def _create_menu_item(self, widget_name: str) -> dbc.DropdownMenuItem:
        """ Converts a widget to a menu item"""
        widget_name = widget_name.replace('Widget', '')

        html_name = '-'.join(widget_name.lower().split())
        html_name = html_name + '-option'                   # i.e. linear-plot-option

        return dbc.DropdownMenuItem(
            widget_name,
            id=self.get_child_id(html_name)     # {'name': 'widget-icon', 'type': 'linear-plot-option', 'index': ''}
        )

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
            id=self.get_child_id('dropdown-menu'),
            className='widget-dropdown-menu',
            label=menu_label,
            children=[
                self._create_menu_item(LinearPlotWidget.name),
                self._create_menu_item(PolarPlotWidget.name),
                self._create_menu_item(ImageryViewerWidget.name)
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


