from dash import html, dcc


def input_item(container_name: str, label_text: str, input_kwargs: dict = None):

    if input_kwargs is None:
        input_kwargs = {}

    input_id = '-'.join(label_text.split(' ')).lower()

    item_style = {
        'display': 'flex',
        'flex-direction': 'row',
        'width': '100%',
        'justify-content': 'space-between',
        'align-items': 'center',
        'margin-top': '5px',
        'margin-bottom': '5px'
    }

    label_style = {
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'left',
        'width': 'auto',
    }

    input_container_style = {
        'display': 'flex',
        'justify-content': 'left',
        'width': '50%'
    }

    input_style = {
        'width': '25%',
        'text-align': 'center'
    }

    return html.Div(
        id=container_name,
        children=[
            html.Label(label_text, style=label_style),
            html.Div(
                children=[
                    dcc.Input(
                        id=input_id,
                        type='number',
                        style=input_style,
                        **input_kwargs
                    )
                ],
                style=input_container_style
            )
        ],
        style=item_style
    )
