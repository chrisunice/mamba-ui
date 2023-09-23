import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(
        id='my-input',
        type='number',
        style={'width': '100%'},
        persistence=True,
        persistence_type='session',
    ),
    html.Div(id='output-div')
])


@app.callback(
    Output('output-div', 'children'),
    Input('my-input', 'value')
)
def update_output(value):
    return f'Input value: {value}'


if __name__ == '__main__':
    app.run_server(debug=True)