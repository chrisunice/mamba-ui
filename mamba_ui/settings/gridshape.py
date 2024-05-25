from dash import html, dcc
import dash_bootstrap_components as dbc

label = html.Label('Widget Grid:', style={'fontWeight': 'bold'})


def input_item(name: str) -> dcc.Input:
    return dcc.Input(
        id=f'grid-{name}',
        type='number',
        placeholder=f'{name.capitalize()}',
        value=1,
        min=1,
        max=4,
        required=True,
        debounce=True,
        style={
            'maxWidth': '100%'
        }
    )


GridShapeRow = dbc.Row(
    [
        dbc.Col(label, width=6),
        dbc.Col(
            dbc.Row(
                [
                    dbc.Col(html.Label('Rows:'),  width=3),
                    dbc.Col(input_item('rows'), width=3),
                    dbc.Col(html.Label('Columns:'), width=3),
                    dbc.Col(input_item('columns'), width=3)
                ],
                justify='around'
            ),
            width=6
        )
    ],
    align='center'
)
