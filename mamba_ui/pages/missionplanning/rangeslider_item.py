import numpy as np
from dash import html, dcc


def _create_marks(min_: int, max_: int):
    marks = {int(i): '' for i in np.arange(min_, max_ + 1, 1)}
    for i in np.linspace(min_, max_, num=5):
        marks[int(i)] = f"{i:.0f}"
    return marks


def rangeslider_item(container_name: str, label_text: str, minimum: int | float, maximum: int | float):

    id_name = '-'.join(label_text.split(' ')).lower()

    item_style = {
        'display': 'flex',
        'flex-direction': 'row',
        'width': '100%',
        'justify-content': 'space-between',
        'align-items': 'center',
        'margin-top': '5px',
        'margin-bottom': '5px',
    }

    label_style = {
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'center',
        'width': 'auto'
    }

    input_container_style = {
        'display': 'flex',
        'flex-direction': 'row',
        'align-items': 'center',
        'width': '75%'
    }

    input_style = {
        'width': '20%',
        'text-align': 'center'
    }

    slider_container_style = {
        'width': '100%'
    }

    return html.Div(
        id=container_name,
        children=[
            html.Label(label_text, style=label_style),
            html.Div(
                children=[
                    dcc.Input(id=f'{id_name}-min-input', min=minimum, type='number', style=input_style),
                    html.Div(
                        children=[
                            dcc.RangeSlider(
                                id=f'{id_name}-slider',
                                min=minimum,
                                max=maximum,
                                marks=_create_marks(minimum, maximum),
                                pushable=True,
                                allowCross=False,
                                tooltip={'placement': 'bottom', 'always_visible': True}
                            )
                        ],
                        style=slider_container_style),
                    dcc.Input(id=f'{id_name}-max-input', max=maximum, type='number', style=input_style)
                ],
                style=input_container_style
            )
        ],
        style=item_style
    )
