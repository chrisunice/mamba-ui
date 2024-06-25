"""
TODO:
 need to add callbacks to handle what the arrows do
 somehow pass the values for each categorical variable so they can be cycled through
"""
import json
from dash.exceptions import PreventUpdate
from dash import html, dcc, Input, Output, MATCH

from mamba_ui import app
from mamba_ui.components.base import BaseComponent


class PlotControlPanelComponent(BaseComponent):

    name = 'Plot Control Panel'

    def __init__(self, index: str = ''):
        super().__init__()
        self.id = {
            'parent': self.html_name,
            'index': index
        }

    @property
    def _store(self):
        store_id = self.id.copy()
        store_id.update({'child': 'store'})
        return dcc.Store(id=store_id, storage_type='memory')

    def _build_icon(self, side: str):
        icon_id = self.id.copy()
        icon_id.update(
            {'child': f'arrow-{side}'}
        )

        icon_style = {}

        return html.I(
            id=icon_id,
            className=f'fa-solid fa-circle-arrow-{side} fa-2xl',
            style=icon_style
        )

    def _build_dropdown(self, name: str):
        dropdown_id = self.id.copy()
        dropdown_id.update(
            {'child': f'{name}-dropdown'}
        )

        dropdown_style = {
            'width': '100%',
        }

        return dcc.Dropdown(
            id=dropdown_id,
            placeholder='Select ... ',
            style=dropdown_style
        )

    @property
    def component(self):
        control_style = {
            'display': 'flex',
            'width': '50%',
            'justifyContent': 'space-evenly',
            'alignItems': 'center'

        }

        column_style = {
            'display': 'flex',
            'justifyContent': 'center',
            'width': '100%',
            'margin': '0px 10px'
        }

        return html.Div(
            children=[
                self._store,
                html.Div(self._build_icon('left'), style=column_style),
                html.Div(self._build_dropdown('category'), style=column_style),
                html.Div(self._build_dropdown('value'), style=column_style),
                html.Div(self._build_icon('right'), style=column_style)
            ],
            style=control_style
        )


@app.callback(
    Output({'parent': 'plot-control-panel', 'child': 'category-dropdown', 'index': MATCH}, 'options'),
    Input({'parent': 'plot-control-panel', 'child': 'store', 'index': MATCH}, 'data')
)
def update_category_dropdown(control_panel_store: str):
    if control_panel_store is None:
        raise PreventUpdate

    control_panel_store = json.loads(control_panel_store)       # convert from json
    categories = list(control_panel_store.keys())               # extract category names (keys)

    return categories


@app.callback(
    Output({'parent': 'plot-control-panel', 'child': 'value-dropdown', 'index': MATCH}, 'options'),
    Input({'parent': 'plot-control-panel', 'child': 'category-dropdown', 'index': MATCH}, 'value'),
    Input({'parent': 'plot-control-panel', 'child': 'store', 'index': MATCH}, 'data')
)
def update_value_dropdown(selected_category, control_panel_store: str):
    if selected_category is None:
        raise PreventUpdate

    control_panel_store = json.loads(control_panel_store)       # convert from json
    values = control_panel_store[selected_category]             # extract values based on category

    return values
