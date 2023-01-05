from dash import html, dcc
import dash_bootstrap_components as dbc


def dropdown_checklist(
        id_name: str,
        options: list | dict = None,
        style: dict = None,
        menu_item_kwargs: dict = None,
        checklist_kwargs: dict = None
):
    id_name = id_name.lower()

    # Handle keyword arguements
    if style is None:
        style = {}

    if menu_item_kwargs is None:
        menu_item_kwargs = {'toggle': True}

    if checklist_kwargs is None:
        checklist_kwargs = {}

    # Styling component
    menu_style = {
        'display': 'flex',
        'justify-content': 'space-between',
        'align-items': 'center',
        'width': '100%',
        'color': 'black',
        'background': 'white',
    }

    menu_item_style = {'background-color': 'transparent', 'overflow-y': 'auto', 'max-height': '250px'}

    checklist_style = {'display': 'flex', 'flex-direction': 'column'}

    checklist_input_style = {'margin-right': '10px'}

    checklist_label_style = {'color': 'black', 'font-size': 'large'}

    # Handle if no items are passed to the dropdown component
    if options is None:
        options = ['No results found']
        checklist_input_style['display'] = 'none'

    # Build component
    component = html.Div(
        id=id_name,
        children=[
            dbc.DropdownMenu(
                id=f'{id_name}-menu',
                label='Select...',
                children=[
                    dbc.DropdownMenuItem(
                        id=f'{id_name}-menu-item',
                        children=[
                            dcc.Checklist(
                                id=f'{id_name}-checklist',
                                options=options,
                                style=checklist_style,
                                inputStyle=checklist_input_style,
                                labelStyle=checklist_label_style,
                                **checklist_kwargs
                            )
                        ],
                        style=menu_item_style,
                        **menu_item_kwargs
                    )
                ],
                toggle_style=menu_style
            )
        ],
        style=style
    )

    return component
