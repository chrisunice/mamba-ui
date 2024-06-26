from dash import html, dcc
import dash_bootstrap_components as dbc


modal_style = {
    'font-size': 'larger'
}

header_style = {
    'display': 'flex',
    'justify-content': 'center'
}

footer_style = {
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
                dbc.Progress(id='mission-planning-download-progress', striped=True)
            ]
        ),
        dbc.ModalFooter(
            children=[
                dbc.Button(
                    children=[
                        html.I(className='fa-solid fa-file-arrow-down', style={'margin-right': '10px'}),
                        'Download'
                    ],
                    id='mission-planning-download-button',
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
            style=footer_style
        )
    ],
    size='md',
    is_open=False,
    centered=True,
    style=modal_style
)
