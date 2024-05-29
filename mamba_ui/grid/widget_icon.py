from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.widgets import LinearPlotWidget
from mamba_ui.widgets import PolarPlotWidget


def widget2menuitem(widget):
    """ Converts a widget to a menu item"""
    widget_type = widget.id['type']
    widget_uid = widget.id['index']
    widget_name = ' '.join(map(lambda x: x.capitalize(), widget_type.split('-')))
    return dbc.DropdownMenuItem(widget_name, id={'type': f'{widget_type}-option', 'index': widget_uid})


def build_widget_icon(row, col):
    return dbc.DropdownMenu(
        className='widget-dropdown-menu',
        label=html.Div(
            [
                html.I(
                    className='fa-solid fa-circle-plus fa-2xl text-dark',
                    style={
                        'marginBottom': '1.25rem'
                    }
                ),
                dbc.Label('Add a Widget', className='text-dark')
            ],
            style={
                'display': 'flex',
                'flexDirection': 'column',
                'height': '100%'
            }
        ),
        children=[
            widget2menuitem(LinearPlotWidget(f'r{row}c{col}')),
            widget2menuitem(PolarPlotWidget(f'r{row}c{col}'))
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
