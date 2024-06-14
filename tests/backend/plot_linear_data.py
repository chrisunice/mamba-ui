import json
import numpy as np
from itertools import product
import plotly.graph_objects as go

from dash import Output
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, MATCH, State

import mamba_ui as mui


# @mui.app.callback(
@mui.app.callback(
    Output({'type': 'linear-plot', 'index': MATCH}, 'figure', allow_duplicate=True),
    Input({'type': 'widget-submit-button', 'index': MATCH}, 'n_clicks'),
    [
        State({'type': 'plot-menu-data-store', 'index': MATCH}, 'data'),        # data stored on the server
        State({'type': 'plot-menu-data-checklist', 'index': MATCH}, 'value'),   # user selected data
        State({'type': 'plot-menu-display-store', 'index': MATCH}, 'data'),     # parameters to display
        State({'type': 'plot-menu-filter-store', 'index': MATCH}, 'data'),      # filters to apply to data
        State({'type': 'linear-plot', 'index': MATCH}, 'figure'),               # existing figure to update
    ],
    prevent_initial_call=True
)
def plot_linear_data(
        submit_click: int,
        serverside_data: dict,
        selected_files: list,
        parameters: str,
        filters: str,
        figure: dict
):
    if submit_click is None:
        raise PreventUpdate

    # Convert JSON to dictionary
    parameters = json.loads(parameters)
    filters = json.loads(filters)

    # Apply the numerical filter to all the loaded data
    numerical_filters = {name: value for name, value in filters.items() if isinstance(value, dict)}
    filtered_dfs = []
    for file in selected_files:
        df = serverside_data[file]
        df.columns = df.columns.str.lower()

        # all numerical filters get applied to every dataframe
        for filter_name, filter_values in numerical_filters.items():
            lower_bound = filter_values['min']
            upper_bound = filter_values['max']
            lower_mask = np.logical_or(df[filter_name] >= lower_bound, lower_bound is None)
            upper_mask = np.logical_or(df[filter_name] <= upper_bound, upper_bound is None)
            if filter_values['inclusive']:
                operator = np.logical_and
            else:
                operator = np.logical_or
            mask = operator(lower_mask, upper_mask)
            df = df[mask]

        # Store filtered dataframe for each file
        filtered_dfs.append(df)

    # Create traces for each of the categorical filters
    categorical_filters = {name: value for name, value in filters.items() if isinstance(value, list)}
    keys, values = zip(*categorical_filters.items())
    iterables = product(*values)
    traces = []
    for df in filtered_dfs:
        for params in iterables:

            trace_name = ' '.join(map(str, params))
            tmp = df.copy()

            for idx, param in enumerate(params):
                col_name = keys[idx]
                tmp = tmp[tmp[col_name] == param]

            # add data to figure
            traces.append(
                go.Scatter(
                    x=tmp[parameters['independent'].lower()],
                    y=tmp[parameters['dependent'].lower()],
                    name=trace_name
                ).to_plotly_json()
            )

    figure['data'] = traces
    return figure
