from dash import html
from datetime import datetime

from mamba_ui import config
from mamba_ui.components.base import BaseComponent


class FooterComponent(BaseComponent):

    name = 'Footer'

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

    @property
    def component(self) -> html.Footer:

        style = {
            'display': 'flex',
            'justifyContent': 'space-between',
            'padding': '0px 10px'
        }

        return html.Footer(
            id=self.id,
            children=[
                html.Span(),
                html.Span(f'© {datetime.now().year} Denmar Technical Services, Inc. All rights reserved.'),
                html.Span(f"Version {config.get('version')}")
            ],
            className='bg-primary text-light',
            style=style
        )
