import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Button("Open Sidebar", id="sidebar-toggle", color="primary", className="mb-3"),
    html.Div(id="sidebar-content"),
    html.Div(id="page-content", className="p-5")
])


@app.callback(
    Output("sidebar-content", "children"),
    [Input("sidebar-toggle", "n_clicks")],
)
def toggle_sidebar(n_clicks):
    if n_clicks and n_clicks % 2 == 1:
        return dbc.Card([
            dbc.CardBody([
                dbc.Nav([
                    dbc.NavLink("Option 1", href="#"),
                    dbc.NavLink("Option 2", href="#"),
                    dbc.NavLink("Option 3", href="#"),
                ], vertical=True, className="mr-auto"),
            ])
        ], style={"width": "250px", "position": "absolute", "left": "0", "top": "0", "height": "100vh", "padding": "10px"})

    return ""


@app.callback(
    Output("page-content", "children"),
    [Input("sidebar-content", "children")]
)
def render_content(sidebar_content):
    if sidebar_content:
        return "This is the main content with the sidebar open."

    return "This is the main content with the sidebar closed."


if __name__ == "__main__":
    app.run(debug=True, port=8080)
