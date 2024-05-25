from dash import html
import dash_bootstrap_components as dbc

NewWidgetIcon = dbc.DropdownMenu(
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
        dbc.DropdownMenuItem('Widget 1'),
        dbc.DropdownMenuItem('Widget 2'),
        dbc.DropdownMenuItem('Widget 3')
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
