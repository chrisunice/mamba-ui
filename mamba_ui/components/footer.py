from dash import html
from datetime import datetime

from mamba_ui import config
from mamba_ui.components.base import BaseComponent


class Footer(BaseComponent):
    def __init__(self):
        super().__init__()

    @property
    def component(self) -> html.Footer:

        style = {
            'display': 'flex',
            'justifyContent': 'space-between',
            'padding': '0px 10px'
        }

        return html.Footer(
            children=[
                html.Span(),
                html.Span(f'© {datetime.now().year} Denmar Technical Services, Inc. All rights reserved.'),
                html.Span(f"Version {config.get('version')}")
            ],
            className='bg-primary text-light',
            style=style
        )
