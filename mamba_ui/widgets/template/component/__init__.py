from dash import html

from mamba_ui.components.base import BaseComponent


class TemplateExampleComponent(BaseComponent):

    name = 'Template Example Component'

    def __init__(self, index: str = ""):
        super().__init__()
        self.id = {
            'parent': self.uid,     # template-example-component
            'index': index
        }

    @property
    def component(self) -> html.Div:

        component_id = self.id.copy()
        component_id.update(
            {'child': 'component'}
        )

        return html.Div(
            id=component_id,
            children=['Template Widget Component']
        )
