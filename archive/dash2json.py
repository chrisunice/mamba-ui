from dash import html, dcc
import dash_bootstrap_components as dbc


# def to_json_recursive(component):
#     if hasattr(component, 'children'):
#         if isinstance(component.children, list):
#             children = [to_json_recursive(child) for child in component.children]
#         else:
#             children = to_json_recursive(component.children)
#         return {**component.to_plotly_json(), 'children': children}
#     else:
#         return component.to_plotly_json()


def to_json_recursive(component):
    # Check if the component is a Dash component
    if component.__class__.__module__.startswith('dash'):
        if hasattr(component, 'children'):
            if isinstance(component.children, list):
                children = [to_json_recursive(child) for child in component.children]
            else:
                children = to_json_recursive(component.children)
            return {**component.to_plotly_json(), 'children': children}
        else:
            return component.to_plotly_json()
    else:
        return component  # or however you want to handle non-Dash components


if __name__ == '__main__':

    layout = html.Div(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem('Item 1'),
                    dbc.DropdownMenuItem('Item 2')
                ]
            ),
            html.I(),
            dcc.Graph(),
        ]
    )

    # json_layout_1 = to_json_recursive(layout)
    json_layout_2 = to_json_recursive_2(layout)