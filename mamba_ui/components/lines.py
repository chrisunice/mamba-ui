from dash import html

VALID_WEIGHTS = {'sm': '1px', 'md': '2.5px', 'lg': '4px'}


def horizontal_line(weight: str):
    assert weight in VALID_WEIGHTS.keys()
    return html.Hr(
        style={
            'width': '100%',
            'height': VALID_WEIGHTS[weight],
            'color': 'white'
        }
    )


def vertical_line(weight: str):
    assert weight in VALID_WEIGHTS.keys()
    return html.Hr(
        style={
            'width': VALID_WEIGHTS[weight],
            'height': 'auto',
        }
    )
