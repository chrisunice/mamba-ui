from dash import dcc
from mamba_ui.components.base import BaseComponent


class ChecklistComponent(BaseComponent):

    name = 'Checklist'

    def __init__(self, options: list, name: str = None, index: str = None):
        """ Generic checklist component with custom styling """
        super().__init__(name, index)
        self.options = options

    @property
    def component(self) -> dcc.Checklist:

        checklist_style = {
            'maxHeight': '300px',
            'overflowY': 'auto'
        }

        input_style = {
            'marginRight': '10px'
        }

        label_style = {
            'display': 'flex',
            'alignItems': 'center',
            'color': 'text-dark',
            'fontSize': 'larger'
        }

        return dcc.Checklist(
            id=self.id,
            options=self.options,
            style=checklist_style,
            inputStyle=input_style,
            labelStyle=label_style
        )
