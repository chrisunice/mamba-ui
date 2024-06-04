import dash_uploader as du
from abc import abstractmethod
import dash_bootstrap_components as dbc

from mamba_ui.widgets.base import BaseWidget
from mamba_ui.components.submit_button_group import SubmitButtonGroupComponent


class BasePlotWidget(BaseWidget):

    widget_name = 'Base Plot'

    def __init__(self, index: str = ''):
        super().__init__(index)

    @property
    @abstractmethod
    def component(self):
        """ To be implemented by actual plotting widgets """
        pass

    @property
    def _menu(self) -> list:
        """ Common menu items used between plots """

        accordion_style = {
            'width': '100%'
        }

        return [
            dbc.Accordion(
                className='text-dark',
                children=[
                    dbc.AccordionItem(
                        children=[
                            du.Upload(
                                id={'type': 'widget-menu-data-upload', 'index': self.index},
                                text='Upload Data',
                            )
                        ],
                        title='Data'
                    ),
                    dbc.AccordionItem([], title='Filters'),
                    dbc.AccordionItem([], title='Design'),
                    dbc.AccordionItem([], title='Export')
                ],
                style=accordion_style
            ),
            SubmitButtonGroupComponent(name='widget', index=self.index).component
        ]
