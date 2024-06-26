from dash import html


def container_title(name: str):
    title_style = {'margin': '0px'}

    return html.H3(
        children=[name],
        style=title_style
    )
