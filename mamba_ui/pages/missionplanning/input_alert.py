import dash_bootstrap_components as dbc

InputAlert = dbc.Modal(
    id='mission-planning-input-alert',
    children=[
        dbc.ModalBody(
            children=[
                dbc.Alert(
                    children=["A value for all input fields must be provided"],
                    color='danger',
                    style=dict(
                        width='100%',
                        margin='0px',
                        textAlign='center',
                        fontSize='larger'
                    )
                )
            ],
        ),
    ],
    centered=True,
    fade=True
)

