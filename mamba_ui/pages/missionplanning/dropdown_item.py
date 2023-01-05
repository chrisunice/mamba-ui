from dash import html, dcc
import dash_bootstrap_components as dbc

from mamba_ui.components import DropdownChecklist


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
        'width': 'auto'
    }

    dropdown_container_style = {
        'width': '40%'
    }

    dropdown_menu_style = {
        'display': 'flex',
        'justify-content': 'space-between',
        'align-items': 'center',
        'width': '100%',
        'color': 'black',
        'background': 'white',
    }

    dropdown_checklist_id = '-'.join(label_text.split(' ')).lower() + '-dropdown'

    return html.Div(
        id=container_name,
        children=[
            html.Label(label_text, style=label_style),
            DropdownChecklist(dropdown_checklist_id, style=dropdown_container_style)
        ],
        style=item_style
    )
