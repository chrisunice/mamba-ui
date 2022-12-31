from dash import html, dcc


def dropdown_item(container_name: str, label_text: str, dropdown_kwargs: dict = None):

    if dropdown_kwargs is None:
        dropdown_kwargs = {}

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
        'justify-content': 'left',
        'width': '50%'
    }

    dropdown_style = {
        'display': 'block',
        'width': '100%',
    }

    dropdown_id = '-'.join(label_text.split(' ')).lower()

    return html.Div(
        id=container_name,
        children=[
            html.Label(label_text, style=label_style),
            html.Div(
                dcc.Dropdown(
                    id=dropdown_id,
                    style=dropdown_style,
                    **dropdown_kwargs
                ),
                style={'width': '50%'}
            )

        ],
        style=item_style
    )
