from dash import html, dcc
import dash_bootstrap_components as dbc

from .upload import Upload
from .lines import horizontal_line as HorizontalLine


def menu_item(id_name: str, icon_name: str, text: str, link: bool = True):
    """ Creates a menu row item with icon and text """
    container_style = dict(display='flex', width='100%')
    button_style = dict(alignItems='center')
    icon_style = dict(color='white')
    text_style = dict(color='white', marginLeft='10px', fontSize='min(24px, 1.5vmax)')

    button = dbc.Button(
        [
            html.I(className=f"fa-solid fa-{icon_name} fa-xl", style=icon_style),
            html.Span(text, style=text_style)
        ],
        id=id_name,
        color='link',
        className='text-decoration-none',
        style=button_style
    )

    if not link:
        return html.Div(button, style=container_style)
    else:
        page_name = f"/{'-'.join(text.lower().split( ))}"
        return dcc.Link(button, href=page_name, style=container_style, className='text-decoration-none')


menubar_style = {
    'display': 'flex',
    'marginTop': '75px',
    'width': 'auto',
    'padding': '0px'
}

menu_item_container = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center'
}


MenuBar = dbc.Offcanvas(
    children=[
        html.Div(
            children=[
                html.H2('Menu', style=dict(margin='0px')),
                HorizontalLine('md'),
                menu_item('menu-upload', 'upload', 'Upload', link=False),
                Upload,
                HorizontalLine('md'),
                menu_item(id_name='menu-home', icon_name='home', text='Home', link=True),
                HorizontalLine('md'),
                menu_item(id_name='menu-data-vis', icon_name='chart-area', text='Data Visualization', link=True),
                HorizontalLine('md'),
                menu_item(id_name='menu-imagery', icon_name='images', text='Imagery', link=True),
                HorizontalLine('md'),
                menu_item(id_name='menu-mission-planning', icon_name='route', text='Mission Planning', link=True)
            ],
            style=menu_item_container
        )
    ],
    id="menubar",
    scrollable=True,
    is_open=False,
    close_button=False,
    style=menubar_style
)
