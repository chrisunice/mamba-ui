from dash import dcc
import dash_bootstrap_components as dbc


def dropdown_checklist(id_name: str, items: list | dict, menu_item_kwargs: dict = None, checklist_kwargs: dict = None):

    id_name = id_name.lower()

    # Handle keyword arguements
    if menu_item_kwargs is None:
        menu_item_kwargs = {'toggle': True}

    if checklist_kwargs is None:
        checklist_kwargs = {}

    # Styling component
    menu_item_style = {
        'background-color': 'transparent',
        'overflow-y': 'auto',
        'max-height': '250px'
    }

    checklist_style = {
        'display': 'flex',
        'flex-direction': 'column',
    }

    checklist_input_style = {
        'margin-right': '10px'
    }

    checklist_label_style = {
        'color': 'black',
        'font-size': 'large'
    }

    # Build component
    component = dbc.DropdownMenuItem(
        id=f'{id_name}-menu-item',
        children=[
            dcc.Checklist(
                id=f'{id_name}-checklist',
                options=items,
                style=checklist_style,
                inputStyle=checklist_input_style,
                labelStyle=checklist_label_style,
                **checklist_kwargs
            )
        ],
        style=menu_item_style,
        **menu_item_kwargs
    )

    return component
