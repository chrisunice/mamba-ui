from dash import dcc, html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.components.dropdown_checklist import DropdownChecklist


class PlotMenuFilterItemComponent(BaseComponent):
    def __init__(
            self,
            categorical_filters: dict = None,
            numerical_filters: dict = None,
            index: str = ''
    ):
        """
        :param filters: a dictionary describing the filtering
            keys - filter names that match columns in the data (i.e. frequency, polarization)
            values - data nature (i.e. discrete or continuous)
        :param index:
        """
        super().__init__()
        if categorical_filters is None:
            categorical_filters = {}
        self.categorical_filters = categorical_filters

        if numerical_filters is None:
            numerical_filters = {}
        self.numerical_filters = numerical_filters

        self.index = index

    def _build_categorical_filter(self, name: str, options: list):
        """ Builds a dropdown checklist component """

        style = {
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'center',
            'width': '100%',
            'minHeight': '50px',
            'height': '100%'
        }

        return html.Div(
            children=[
                html.Div(
                    html.Label(name.capitalize(), style={'fontSize': 'larger'}),
                    style={'width': '50%'}
                ),
                html.Div(
                    DropdownChecklist(name, options=options, index=self.index).component,
                    style={'width': '50%'}
                )
            ],
            style=style
        )

    def _build_numerical_filter(self, name: str):
        """ Builds a range slider component """
        return

    @property
    def component(self) -> dbc.AccordionItem:

        filter_items = [self._build_categorical_filter(k, v) for k, v in self.categorical_filters.items()] + \
                       [self._build_numerical_filter(k, v) for k, v in self.numerical_filters.items()]

        return dbc.AccordionItem(
            children=filter_items,
            title=html.H4('Filter')
        )
