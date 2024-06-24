import os
import json
import pandas as pd
from dash import dcc, html
import dash_uploader as du
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import MATCH, ServersideOutput, State, Input, Output, Trigger

from mamba_ui import app
from mamba_ui import config
from mamba_ui.components.base import BaseComponent
from mamba_ui.components.lines import HorizontalLineComponent
from mamba_ui.components.checklist import ChecklistComponent


class PlotMenuDataItemComponent(BaseComponent):

    name = 'Plot Menu Data'

    def __init__(self, index: str = ''):
        super().__init__()
        self.index = index
        self.id = {
            'parent-component': self.uid,
            'index': index
        }

    @property
    def _data_store(self):
        """ To store the data server side """
        store_id = self.id.copy()
        store_id.update({'child-component': 'data-store'})
        return dcc.Store(id=store_id, storage_type='session')

    @property
    def _selected_store(self):
        """ To store which of the loaded files has been selected by the user """
        store_id = self.id.copy()
        store_id.update({'child-component': 'selected-store'})
        return dcc.Store(id=store_id, storage_type='memory')

    @property
    def _upload(self) -> html.Div:
        """ The dash uploader Upload component """
        upload_id = self.id.copy()
        upload_id.update({'child-component': 'upload'})

        upload_style = {
            'fontSize': 'larger'
        }

        return du.Upload(
            id=upload_id,
            text='Upload Data',
            max_files=10,
            default_style=upload_style
        )

    @property
    def component(self) -> dbc.AccordionItem:
        return dbc.AccordionItem(
            children=[
                self._data_store,
                self._upload,
                HorizontalLineComponent('sm').component,
                self._selected_store,
                ChecklistComponent(self.uid, index=self.index).component
            ],
            title=html.H4('Data')
        )


@app.callback(
    ServersideOutput({'parent-component': 'plot-menu-data', 'child-component': 'data-store', 'index': MATCH}, 'data'),
    Input({'parent-component': 'plot-menu-data', 'child-component': 'upload', 'index': MATCH}, 'isCompleted'),
    State({'parent-component': 'plot-menu-data', 'child-component': 'upload', 'index': MATCH}, 'fileNames'),
    State({'parent-component': 'plot-menu-data', 'child-component': 'data-store', 'index': MATCH}, 'data')
)
def store_data(is_complete: bool, files: list[str], data: None | dict):
    if not is_complete:
        raise PreventUpdate

    # Handle incoming data
    full_file_paths = [f"{config['paths']['upload_directory']}\\{file}" for file in files]
    incoming_data = {os.path.basename(fpath).rstrip('.csv'): pd.read_csv(fpath) for fpath in full_file_paths}

    # Update data store
    if data is None:
        data = {}
    data.update(incoming_data)
    return data


@app.callback(
    Output({'type': 'plot-menu-data-checklist', 'index': MATCH}, 'options'),
    Input({'parent-component': 'plot-menu-data', 'child-component': 'data-store', 'index': MATCH}, 'data'),
    Trigger('dash-layout', 'children')
)
def populate_checklist(data: dict):
    if data is None:
        raise PreventUpdate

    return list(data.keys())


@app.callback(
    Output({'parent-component': 'plot-menu-data', 'child-component': 'selected-store', 'index': MATCH}, 'data'),
    Input({'type': 'plot-menu-data-checklist', 'index': MATCH}, 'value')
)
def store_user_selection(selected_files: list):
    if selected_files is None:
        raise PreventUpdate

    return json.dumps(selected_files)
