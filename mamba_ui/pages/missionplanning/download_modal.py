from dash import html, dcc
import dash_bootstrap_components as dbc


modal_style = {
    'font-size': 'larger'
}

header_style = {
    'display': 'flex',
    'justify-content': 'center'
}

body_style = {
    'display': 'flex',
    'justify-content': 'space-between'
}

DownloadModal = dbc.Modal(
    id='mission-planning-download-modal',
    children=[
        dbc.ModalHeader(
            html.H4('Mission Planning File Complete!'),
            close_button=False,
            style=header_style
        ),
        dbc.ModalBody(
            children=[
                dbc.Button(
                    id='mission-planning-download-button',
                    children=[
                        html.I(className='fa-solid fa-file-arrow-down', style={'margin-right': '10px'}),
                        'Download',
                    ],
                    color='success',
                    size='lg',
                    style=dict(width='65%')
                ),
                dbc.Button(
                    'Close',
                    id='mission-planning-close-button',
                    color='danger',
                    size='lg',
                    style=dict(width='30%')
                ),
                dcc.Download(id='mission-planning-download')
            ],
            style=body_style
        )
    ],
    size='md',
    is_open=False,
    centered=True,
    style=modal_style
)
