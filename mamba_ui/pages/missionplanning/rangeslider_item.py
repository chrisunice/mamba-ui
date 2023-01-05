from dash import html, dcc


def rangeslider_item(container_name: str, label_text: str, slider_kwargs: dict = None):

    # Handle keyword arguments
    if slider_kwargs is None:
        slider_kwargs = {}

    input_kwargs = {}
    if 'min' in slider_kwargs.keys():
        input_kwargs['min'] = slider_kwargs['min']

    if 'max' in slider_kwargs.keys():
        input_kwargs['max'] = slider_kwargs['max']

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
        'width': '12.5%',
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
                    dcc.Input(id=f'{id_name}-min-input', type='number', style=input_style, **input_kwargs),
                    html.Div([dcc.RangeSlider(id=f'{id_name}-slider', **slider_kwargs)], style=slider_container_style),
                    dcc.Input(id=f'{id_name}-max-input', type='number', style=input_style, **input_kwargs)
                ],
                style=input_container_style
            )
        ],
        style=item_style
    )
