import math
import numpy as np
import pandas as pd
from dash import callback_context
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, State, MATCH, ALL

import mamba_ui as mui
from mamba_ui.widgets.plots.two_dimensional.menu.filter import TwoDimensionalPlotMenuFilterItemComponent


def is_categorical(series, threshold=0.05):
    """ Note this should probably be part of lodat.utils """
    # If the column is of object type or category type, it's categorical
    if series.dtype == 'object' or pd.api.types.is_categorical_dtype(series):
        return True

    # Calculate the number of unique values
    unique_values = series.nunique()

    # Determine if unique values are less than threshold of total values
    if unique_values / len(series) < threshold:
        return True

    return False


@mui.app.callback(
    Output({'name': ALL, 'type': 'filter-container', 'index': MATCH}, 'children'),
    [
        Input(
            component_id={'name': '2d-plot-menu-display', 'type': 'independent-dropdown', 'index': MATCH},
            component_property='value'
        ),
        Input(
            component_id={'name': '2d-plot-menu-display', 'type': 'dependent-dropdown', 'index': MATCH},
            component_property='value'
        ),
    ],
    [
        State(
            component_id={'name': '2d-plot-menu-display', 'type': 'independent-dropdown', 'index': MATCH},
            component_property='options'
        ),
        State(
            component_id={'name': '2d-plot-menu-data', 'type': 'data-store', 'index': MATCH},
            component_property='data'
        ),
        State(
            component_id={'name': '2d-plot-menu-data-checklist', 'index': MATCH},
            component_property='value'
        ),
    ]
)
def populate_menu_filters(i_var, d_var, options, data, selected_files):
    """ Populates the plot menu filters based on the user selected variables for plotting """

    # Prevent any updates until dropdowns get actual values
    no_values = np.logical_or(i_var is None, d_var is None)
    no_action = callback_context.triggered_id is None
    if no_action or no_values:
        raise PreventUpdate

    other_columns = [option['value'] for option in options if option['value'] not in [i_var, d_var]]

    # Build filters
    cat_filters = {}
    num_filters = {}

    # Step over every other column not being actively displayed
    for col_name in other_columns:

        # Step through each selected file
        for file_name in selected_files:

            # Get the column data
            col_data = data[file_name][col_name]

            if is_categorical(col_data):
                # Handle categorical columns
                new_options = list(np.unique(col_data))

                try:
                    existing_options = cat_filters[col_name]
                except KeyError:
                    # This column name hasn't been created yet so insert new options
                    cat_filters[col_name] = new_options
                else:
                    # No error, column exists, insert any new options to existing ones
                    cat_filters[col_name] += [option for option in new_options if option not in existing_options]

            else:
                # Handle numerical columns
                new_options = {'minimum': math.floor(col_data.min()), 'maximum': math.ceil(col_data.max()), 'step': 1}

                try:
                    existing_options = num_filters[col_name]
                except KeyError:
                    # This column name hasn't been created yet so insert new options
                    num_filters[col_name] = new_options
                else:
                    # No error, column exists
                    # Update with new minimum if it's smaller than the existing
                    if new_options['minimum'] < existing_options['minimum']:
                        existing_options['minimum'] = new_options['minimum']

                    # Update with new maximum if it's larger than existing
                    if new_options['maximum'] > existing_options['maximum']:
                        existing_options['maximum'] = new_options['maximum']

    return [
        TwoDimensionalPlotMenuFilterItemComponent(
            categorical_filters=cat_filters,
            numerical_filters=num_filters,
            index=callback_context.triggered_id.index
        ).component
    ]