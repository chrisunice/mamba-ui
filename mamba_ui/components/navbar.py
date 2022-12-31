from dash import html
import dash_bootstrap_components as dbc

NAVBAR_HEIGHT = '50px'

NavBar = dbc.Navbar(
    id='nav-bar',
    children=[
        html.I(
            id='menu-icon',
            className='fa-solid fa-bars fa-2xl',
            style=dict(
                position='absolute',
                left='10px',
                color='white'
            )
        ),
        html.Div(
            html.H5(
                'Mamba',
                style=dict(
                    margin='0px',
                    fontSize=NAVBAR_HEIGHT
                )
            ),
            style=dict(
                position='absolute',
                left='50%',
                width='500px',
                marginLeft='-250px',
                textAlign='center'
            )
        ),
        html.I(
            id='filter-icon',
            className='fa-solid fa-filter fa-2xl',
            style={
                'position': 'absolute',
                'right': '10px',
                'color': 'white',
                'display': 'none'
            }
        ),
        html.I(
            id='database-icon',
            className='fa-solid fa-database fa-2xl',
            style={
                'position': 'absolute',
                'right': '10px',
                'color': 'white',
                'display': 'none'
            }
        )
    ],
    style={'height': NAVBAR_HEIGHT, 'padding': '5px'}
)


