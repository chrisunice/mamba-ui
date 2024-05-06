import dash_bootstrap_components as dbc


def widget_grid(nrows: int = 1, ncols: int = 1) -> dbc.Row:
    """
    Creates a grid layout

    :param nrows: number of rows in the grid; default is 1
    :param ncols: number of columns in the grid; default is 1

    :return: dbc.Row consisting of the desired number of dbc.Rows and dbc.Cols
    """

    grid_style = {
        'display': 'flex',
        'flex': 1,
        'width': '100%',
        'margin': '0px',
        'padding': '0px'
    }

    row_style = {
        'border': '1px solid green',
        'margin': '0px',
        'padding': '5px'
    }

    col_style = {
        'border': '1px solid red',
        'margin': '0px 5px 0px 5px',
        'padding': '0px'
    }

    grid_children = []

    for r in range(nrows):
        row_children = []
        for c in range(ncols):
            row_children.append(
                dbc.Col(id=f'col-{c}', style=col_style)
            )
        grid_children.append(
            dbc.Row(id=f'row-{r}', children=row_children, style=row_style)
        )

    grid = dbc.Row(id='grid-layout', children=grid_children, style=grid_style)
    return grid
