from dash import html
from dash_extensions import DeferScript

# MyCustomDiv = html.Div(
#     className='my-custom-div',  # Added class name
#     children=['Drag me!'],
#     style={
#         'resize': 'both',
#         'overflow': 'auto',
#         'cursor': 'move',
#         'width': '250px',
#         'height': '500px',
#         'border': '1px solid green'
#     }
# )
#
# SandboxPageLayout = html.Div(
#     id='sandbox-layout',
#     children=[
#         html.H1('Welcome to the sandbox!'),
#         html.Div(MyCustomDiv, style={
#             'display': 'flex',
#             'height': '100%',
#             'alignItems': 'center',
#             'justifyContent': 'center',
#             'width': '100%'
#         })
#     ],
#     style={
#         'display': 'flex',
#         'flexDirection': 'column',
#         'alignItems': 'center',
#         'width': '100%'
#     }
# )

SandboxPageLayout = html.Div(
    className='grid-stack',
    children=[
        html.Div(
            className='grid-stack-item',
            **{'data-gs-locked': 'true'},
            children=[
                html.Div(
                    className='grid-stack-item-content',
                    children='Bigger Block 1'
                )
            ],
            style=dict(border='1px solid black')
        ),
        html.Div(
            className='grid-stack-item',
            **{'data-gs-w': "4", 'data-gs-h': "2", 'data-gs-x': "4", 'data-gs-y': "0"},
            children=[
                html.Div(
                    className='grid-stack-item-content',
                    children='Block 2')
            ],
            style=dict(border='1px solid black')
        ),
        DeferScript(src='../../assets/gridstack/gridstack-init.js'),
        html.Div('some words', **{'data-a': '1'})
    ],
    style=dict(width='100%', height='100%')
)
