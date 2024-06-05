from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent


class PlotMenuFilterItemComponent(BaseComponent):
    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index

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
            id={'type': 'plot-menu-filter-checklist', 'index': self.index},
            options=[],
            style=checklist_style,
            inputStyle=input_style,
            labelStyle=label_style
        )

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[
                dbc.Accordion(
                    children=[
                        dbc.AccordionItem([], title='Frequency'),
                        dbc.AccordionItem([], title='Polarization')
                    ]
                ),
                # self._checklist
            ],
            title=html.H4('Filter')
        )
