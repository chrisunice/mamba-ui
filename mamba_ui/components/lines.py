from dash import html

_VALID_WEIGHTS = {'sm': '1px', 'md': '2.5px', 'lg': '4px'}


def horizontal_line(weight: str):
    assert weight in _VALID_WEIGHTS.keys()
    return html.Hr(
        style={
            'width': '100%',
            'height': _VALID_WEIGHTS[weight],
        }
    )


def vertical_line(weight: str):
    assert weight in _VALID_WEIGHTS.keys()
    return html.Hr(
        style={
            'width': _VALID_WEIGHTS[weight],
            'height': 'auto',
        }
    )
