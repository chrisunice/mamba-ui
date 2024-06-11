from dash import dcc
from mamba_ui.components.base import BaseComponent


class ChecklistComponent(BaseComponent):
    def __init__(self, name, options: list = None, index: str = ''):
        super().__init__()
        self.name = name
        if options is None:
            options = []
        self.options = options
        self.index = index

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
            id={'type': f'{self.name}-checklist', 'index': self.index},
            options=self.options,
            style=checklist_style,
            inputStyle=input_style,
            labelStyle=label_style
        )
