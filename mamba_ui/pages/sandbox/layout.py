from dash import html

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
        html.H6('This is the sandbox, build random things here!'),
    ],
    style=page_styles
)

