from dash import html


def container_title(name: str):
    title_style = {
        'font-size': 'min(36px, 3vmax)',
        'margin': '0px'
    }

    return html.Span(
        children=[name],
        style=title_style
    )
