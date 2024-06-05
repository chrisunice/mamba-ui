from dash import html

from mamba_ui.components.base import BaseComponent


class TemplateExampleMenuComponent(BaseComponent):
    def __init__(self, _index: str = ""):
        super().__init__()
        self._index = _index

    @property
    def component(self) -> html.Div:
        return html.Div(
            id={'type': 'template-menu', 'index': self._index},
            children=['Template Widget Menu Component']
        )
