from dash import dcc, html
import dash_uploader as du
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.components.lines import HorizontalLineComponent
from mamba_ui.components.checklist import ChecklistComponent


class PlotMenuDataItemComponent(BaseComponent):

    name = 'Plot Menu Data'

    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

    @property
    def _upload(self) -> du.Upload:
        return du.Upload(
            id={'type': f'{self.uid}-upload', 'index': self.index},
            text='Upload Data',
            max_files=10,
            default_style={
                'fontSize': 'larger'
            }
        )

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[
                self._upload,
                HorizontalLineComponent('sm').component,
                ChecklistComponent(self.uid, index=self.index).component
            ],
            title=html.H4('Data')
        )
