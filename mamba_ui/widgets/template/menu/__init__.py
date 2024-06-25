from dash import html

from mamba_ui.components.base import BaseComponent


class TemplateExampleMenuComponent(BaseComponent):

    name = 'Template Example Menu'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)

    @property
    def component(self) -> html.Div:

        return html.Div(
            id=self.get_child_id('menu'),
            children=['Template Widget Menu Component']
        )
