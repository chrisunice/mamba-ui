from dash import html, dcc
import dash_bootstrap_components as dbc

from mamba_ui.components import DropdownChecklist


def dropdown_item(label_text: str, dropdown_checklist_kwargs: dict = None):

    if dropdown_checklist_kwargs is None:
        dropdown_checklist_kwargs = {}

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

    id_name = '-'.join(label_text.split(' ')).lower()
    container_id = f'{id_name}-row'
    dropdown_checklist_id = f'{id_name}-dropdown'

    return html.Div(
        id=container_id,
        children=[
            html.Label(label_text, style=label_style),
            DropdownChecklist(dropdown_checklist_id, style=dropdown_container_style, **dropdown_checklist_kwargs)
        ],
        style=item_style
    )
