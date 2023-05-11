from dash import html, dcc

page_styles = {
    'display': 'flex',
    'flex': '1',
    'flex-direction': 'column',
    'justify-content': 'center',
    'align-items': 'center',
    'width': '100%',
}

layout = html.Div(
    id='sandbox-page',
    children=[
        dcc.Store(id='server-store'),
        html.H6('This is the sandbox, build random things here!'),
    ],
    style=page_styles
)

