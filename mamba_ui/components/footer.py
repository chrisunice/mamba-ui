from dash import html
from datetime import datetime


footer_style = {
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
    'height': '50px',
    'color': 'white'
}


Footer = html.Footer(
    children=[
        f'© {datetime.now().year} Denmar Technical Services, Inc. All rights reserved.'
    ],
    style=footer_style,
    className='footer bg-secondary'
)
