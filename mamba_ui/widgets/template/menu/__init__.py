from dash import html

from mamba_ui.components.base import BaseComponent


class TemplateExampleMenuComponent(BaseComponent):

    name = 'Template Example Menu'

    def __init__(self, index: str = ""):
        super().__init__()
        self.id = {
            'parent': self.uid,     # template-example-menu
            'index': index
        }

    @property
    def component(self) -> html.Div:

        component_id = self.id.copy()
        component_id.update(
            {'child': 'menu'}
        )

        return html.Div(
            id=component_id,
            children=['Template Widget Menu Component']
        )
