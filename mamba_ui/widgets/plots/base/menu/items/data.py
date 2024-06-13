import os
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

    @property
    def _upload(self) -> html.Div:

        return html.Div(
            children=[
                dcc.Store(id={'type': f'plot-menu-data-store', 'index': self.index}, storage_type='session'),
                du.Upload(
                    id={'type': f'plot-menu-data-upload', 'index': self.index},
                    text='Upload Data',
                    max_files=10,
                    default_style={
                        'fontSize': 'larger'
                    }
                )
            ],
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


@app.callback(
    ServersideOutput({'type': 'plot-menu-data-store', 'index': MATCH}, 'data'),
    Input({'type': 'plot-menu-data-upload', 'index': MATCH}, 'isCompleted'),
    State({'type': 'plot-menu-data-upload', 'index': MATCH}, 'fileNames'),
    State({'type': 'plot-menu-data-store', 'index': MATCH}, 'data')
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
    Input({'type': 'plot-menu-data-store', 'index': MATCH}, 'data'),
    Trigger('dash-layout', 'children')
)
def populate_checklist(data: dict):
    if data is None:
        raise PreventUpdate

    return list(data.keys())
