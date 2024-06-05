from dash import dcc, html
import dash_uploader as du
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.components.lines import HorizontalLineComponent


class PlotMenuDataItemComponent(BaseComponent):
    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

    @property
    def _upload(self) -> du.Upload:
        return du.Upload(
            id={'type': 'plot-menu-data-upload', 'index': self.index},
            text='Upload Data',
            max_files=10
        )

    @property
    def _checklist(self) -> dcc.Checklist:

        checklist_style = {
            'maxHeight': '300px',
            'overflowY': 'auto'
        }

        input_style = {
            'marginRight': '10px'
        }

        label_style = {
            'display': 'flex',
            'alignItems': 'center'
        }

        return dcc.Checklist(
            id={'type': 'plot-menu-data-checklist', 'index': self.index},
            options=[],
            style=checklist_style,
            inputStyle=input_style,
            labelStyle=label_style
        )

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[
                self._upload,
                HorizontalLineComponent('sm').component,
                self._checklist
            ],
            title=html.H4('Data')
        )
