# TODO break this out into its own file (i.e. grid.py)
from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.grid.icon import build_widget_icon as WidgetIcon


def widget_grid(nrows: int = 1, ncols: int = 1) -> dbc.Row:
    """
    Creates a grid layout

    :param nrows: number of rows in the grid; default is 1
    :param ncols: number of columns in the grid; default is 1

    :return: dbc.Row consisting of the desired number of dbc.Rows and dbc.Cols
    """

    grid_style = {
        'display': 'flex',
        'flexGrow': '1',
        'width': '100%',
        'margin': '0px',
        'padding': '0px'
    }

    row_style = {
        'display': 'flex',
        'margin': '0px',
        'padding': '5px'
    }

    col_style = {
        'display': 'flex',
        'flexGrow': '1',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'alignItems': 'center',
        'margin': '0px 5px 0px 5px',
        'padding': '0px',
        'borderRadius': '5px',
        'backgroundColor': 'rgba(0, 0, 0, 0)',
        'boxShadow': '0px 0px 10px gray'
    }

    grid_children = []

    for r in range(nrows):
        row_children = []
        for c in range(ncols):
            row_children.append(
                html.Div(
                    id={'type': 'widget-container', 'index': f'r{r}c{c}'},
                    className='bg-transparent border border-secondary',
                    children=[WidgetIcon(r, c)],
                    style=col_style
                )
            )
        grid_children.append(
            html.Div(id=f'grid-row-{r}', children=row_children, style=row_style)
        )

    grid = dbc.Row(id='grid-layout', children=grid_children, style=grid_style)
    return grid
