import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

sidebar = dbc.Offcanvas(
    [
        html.Div(
            [html.H3("Sidebar", className="display-4")],
            style={"background-color": "#f8f9fa"},
        ),
        html.Hr(),
        html.P(
            "This is an example of a sidebar",
            className="lead",
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
                dbc.NavLink("Contact", href="/contact", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="offcanvas",
    is_open=False,
    title="",
)

content = html.Div(id="page-content", children=[])

app.layout = html.Div(
    [
        dbc.Button(
            "Toggle sidebar",
            id="sidebar-toggle",
            color="primary",
            className="mb-3",
        ),
        dbc.Container(
            [
                sidebar,
                content,
            ],
            fluid=True,
        ),
    ]
)

@app.callback(
    Output("offcanvas", "is_open"),
    [Input("sidebar-toggle", "n_clicks")],
    [dash.dependencies.State("offcanvas", "is_open")],
)
def toggle_offcanvas(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(port=8081, debug=True)
