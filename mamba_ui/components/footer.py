from dash import html
from datetime import datetime
from mamba_ui import config

footer_style = {
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
    'height': '50px',
    'color': 'white'
}


Footer = html.Footer(
    children=[
        html.Span(),
        html.Span(f'© {datetime.now().year} Denmar Technical Services, Inc. All rights reserved.'),
        html.Span(f"Version {config.get('version')}")
    ],
    className='bg-primary text-light',
    style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'padding': '0px 10px'
    }
)
