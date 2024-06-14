import json
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback_context
from dash_extensions.enrich import Input, Output, MATCH, ALL

from mamba_ui import app
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.dropdown_checklist import DropdownChecklistComponent
from mamba_ui.components.numerical_input import NumericalInputComponent


class PlotMenuFilterItemComponent(BaseComponent):
    def __init__(
            self,
            categorical_filters: dict[str, list] = None,
            numerical_filters: dict[str, dict] = None,
            index: str = ''
    ):
        """
        A dbc.AccordionItem that contains functionality for filtering data

        :param categorical_filters: a dictionary of categorical filters where the key is the filter name as a string \
         and the value is the options for the filter as a list (e.g. Pass, Polarization, Frequency)
        :param numerical_filters: a dictionary describing the filtering where the key is the filter name as a string \
         and the value is a dictionary of arguments min, max, and step to pass to the NumericalInputComponent \
         (e.g. Look, Depression, Twist, Range)
        :param index: unique index for the component
        """
        super().__init__()
        if categorical_filters is None:
            categorical_filters = {}
        self.categorical_filters = categorical_filters

        if numerical_filters is None:
            numerical_filters = {}
        self.numerical_filters = numerical_filters

        self.index = index

    def _build_categorical_filter(self, name, options) -> html.Div:
        """ Builds a dropdown checklist component """

        style = {
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'center',
            'width': '100%',
            'minHeight': '50px',
            'height': '100%',
            'margin': '10px 0px'
        }

        return html.Div(
            children=[
                html.Div(
                    html.Label(name.capitalize(), style={'fontSize': 'larger'}),
                    style={'width': '50%'}
                ),
                html.Div(
                    DropdownChecklistComponent(name, options=options, index=self.index).component,
                    style={'width': '50%'}
                )
            ],
            style=style
        )

    def _build_numerical_filter(self, name, minimum, maximum, step) -> html.Div:
        """ Builds a range slider component """

        style = {
            'display': 'flex',
            'flexDirection': 'row',
            'alignItems': 'center',
            'width': '100%',
            'minHeight': '50px',
            'height': '100%',
            'margin': '10px 0px'
        }

        return html.Div(
            children=[
                html.Div(
                    html.Label(name.capitalize(), style={'fontSize': 'larger'}),
                    style={'width': '50%'}
                ),
                html.Div(
                    NumericalInputComponent(
                        name, minimum=minimum, maximum=maximum, step=step, index=self.index
                    ).component,
                    style={'width': '50%'}
                )
            ],
            style=style
        )

    @property
    def component(self) -> dbc.AccordionItem:
        categorical_items = [self._build_categorical_filter(k.lower(), v) for k, v in self.categorical_filters.items()]
        numerical_items = [self._build_numerical_filter(k.lower(), **dct) for k, dct in self.numerical_filters.items()]

        return dbc.AccordionItem(
            children=[
                dcc.Store(id={'type': 'plot-menu-filter-store', 'index': self.index}, storage_type='memory'),
                *categorical_items,
                *numerical_items
            ],
            title=html.H4('Filter'),
        )


@app.callback(
    Output({'type': 'plot-menu-filter-store', 'index': MATCH}, 'data'),
    Input({'parent-component': ALL, 'child-component': 'checklist', 'index': MATCH}, 'value'),
    Input({'parent-component': ALL, 'child-component': 'min-input', 'index': MATCH}, 'value'),
    Input({'parent-component': ALL, 'child-component': 'max-input', 'index': MATCH}, 'value'),
    Input({'parent-component': ALL, 'child-component': 'switch', 'index': MATCH}, 'value')
)
def store_filters(*_):
    ctx = callback_context
    if ctx.triggered_id is None:
        raise PreventUpdate

    filters = {}
    for info, value in ctx.inputs.items():
        component_id = json.loads(info.rstrip('.value'))
        filter_name = component_id['parent-component'].split('-')[0]
        if component_id['child-component'] == 'checklist':
            filters[filter_name] = value
        elif component_id['child-component'] == 'min-input':
            try:
                filters[filter_name].update({'min': value})
            except KeyError:
                filters[filter_name] = {'min': value}
        elif component_id['child-component'] == 'max-input':
            try:
                filters[filter_name].update({'max': value})
            except KeyError:
                filters[filter_name] = {'max': value}
        elif component_id['child-component'] == 'switch':
            try:
                filters[filter_name].update({'inclusive': value})
            except KeyError:
                filters[filter_name] = {'inclusive': value}
        else:
            raise ValueError('Unhandled input!')

    return json.dumps(filters)
