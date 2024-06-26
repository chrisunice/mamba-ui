import json
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback_context
from dash_extensions.enrich import Input, Output, MATCH, ALL

from mamba_ui import app
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.dropdown_checklist import DropdownChecklistComponent
from mamba_ui.components.numerical_input import NumericalInputComponent


class TwoDimensionalPlotMenuFilterItemComponent(BaseComponent):

    name = '2D Plot Menu Filter'

    def __init__(
            self,
            index: str,
            name: str = None,
            categorical_filters: dict[str, list] = None,
            numerical_filters: dict[str, dict] = None,
    ):
        """
        A dbc.AccordionItem that contains functionality for filtering data

        :param index: a unique index that should specify the location of the component
        :param name: the name of the component; if no name is given then the class attribute name will be used
        :param categorical_filters: a dictionary of categorical filters where the key is the filter name as a string \
         and the value is the options for the filter as a list (e.g. Pass, Polarization, Frequency)
        :param numerical_filters: a dictionary describing the filtering where the key is the filter name as a string \
         and the value is a dictionary of arguments min, max, and step to pass to the NumericalInputComponent \
         (e.g. Look, Depression, Twist, Range)
        """
        super().__init__(name=name, index=index)

        if categorical_filters is None:
            categorical_filters = {}
        self.categorical_filters = categorical_filters

        if numerical_filters is None:
            numerical_filters = {}
        self.numerical_filters = numerical_filters

    @property
    def _store(self):
        return dcc.Store(
            id=self.get_child_id('store'),
            storage_type='memory'
        )

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
                    DropdownChecklistComponent(options, name=name, index=self.id.get('index')).component,
                    style={'width': '50%'}
                )
            ],
            style=style
        )

    def _build_numerical_filter(self, name, minimum, maximum, step) -> html.Div:
        """ Builds a numerical input component """

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
                        minimum=minimum,
                        maximum=maximum,
                        step=step,
                        name=name,
                        index=self.id.get('index')
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
                self._store,
                *categorical_items,
                *numerical_items
            ],
            title=html.H4('Filter'),
        )


@app.callback(
    Output(
        component_id={'name': '2d-plot-menu-filter', 'type': 'store', 'index': MATCH},
        component_property='data'
    ),
    [
        Input(
            component_id={'name': ALL, 'type': 'checklist', 'index': MATCH},
            component_property='value'
        ),
        Input(
            component_id={'name': ALL, 'type': 'min-input', 'index': MATCH},
            component_property='value'
        ),
        Input(
            component_id={'name': ALL, 'type': 'max-input', 'index': MATCH},
            component_property='value'
        ),
        Input(
            component_id={'name': ALL, 'type': 'switch', 'index': MATCH},
            component_property='value'
        )
    ]
)
def store_filters(*_):
    ctx = callback_context
    if ctx.triggered_id is None:
        raise PreventUpdate

    filters = {}
    for info, value in ctx.inputs.items():
        component_id = json.loads(info.rstrip('.value'))
        filter_name = component_id['name'].split('-')[0]
        if component_id['type'] == 'checklist':
            filters[filter_name] = value
        elif component_id['type'] == 'min-input':
            try:
                filters[filter_name].update({'min': value})
            except KeyError:
                filters[filter_name] = {'min': value}
        elif component_id['type'] == 'max-input':
            try:
                filters[filter_name].update({'max': value})
            except KeyError:
                filters[filter_name] = {'max': value}
        elif component_id['type'] == 'switch':
            try:
                filters[filter_name].update({'inclusive': value})
            except KeyError:
                filters[filter_name] = {'inclusive': value}
        else:
            raise ValueError('Unhandled input!')

    return json.dumps(filters)
