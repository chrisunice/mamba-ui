import base64
from dash import html, dcc
import dash_bootstrap_components as dbc

from mamba_ui.pages.imagery.sidebar import Sidebar
from mamba_ui import PKG_DIR

page_style = {
    'display': 'flex',
    'flexDirection': 'column',
    'width': '100%',
    'justify-content': 'center',
    'align-items': 'center'
}

image_style = {
    'max-height': '480px',
    'max-width': '640px',
    'box-shadow': '0px 0px 10px #fff'
}

path_to_image = f'{PKG_DIR}/static/black_image.jpg'
encoded_image = base64.b64encode(open(path_to_image, 'rb').read())

layout = html.Div(
    id='imagery-page',
    children=[
        dcc.Store(id='imagery-store', storage_type='memory'),
        Sidebar,
        dbc.Carousel(
            id='imagery-carousel',
            items=[
                {
                    'key': '1',
                    'src': 'data:image/jpg;base64,{}'.format(encoded_image.decode()),
                }
            ],
            ride=False,
            style=image_style
        ),
        html.H6(id='carousel-caption', children=['Click the database icon to begin'], style={'margin': '10px'})
    ],
    style=page_style
)

