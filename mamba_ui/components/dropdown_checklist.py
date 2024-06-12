from dash import callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH, ALL

from mamba_ui import app
from mamba_ui.components.base import BaseComponent


class DropdownChecklistComponent(BaseComponent):
    def __init__(self, name: str, options: list = None, index: str = ''):
        super().__init__()
        self.name = name
        if options is None:
            options = []
        self.options = options

        self.id = {
            'parent-component': f'{self.name}-dropdown-checklist',
            'index': index
        }

    @property
    def _checklist(self):
        """ dbc.Checklist sub component """
        checklist_id = self.id.copy()
        checklist_id.update({'child-component': 'checklist'})
        return dbc.Checklist(
            id=checklist_id,
            options=self.options,
            className='dropdown-checklist-checklist'
        )

    @property
    def _dropdown_item(self):
        """ dbc.DropdownMenuItem sub component """

        style = {
            'overflowY': 'auto',
            'maxHeight': '250px',
            'width': '100%',
        }

        item_id = self.id.copy()
        item_id.update({'child-component': 'menu-item'})

        return dbc.DropdownMenuItem(
            className='dropdown-checklist-menu-item',
            id=item_id,
            children=[self._checklist],
            toggle=False,
            style=style
        )

    @property
    def component(self):

        toggle_style = {
            'display': 'flex',
            'justify-content': 'space-between',
            'alignItems': 'center',
            'width': '100%',
        }

        menu_id = self.id.copy()
        menu_id.update({'child-component': 'menu'})

        return dbc.DropdownMenu(
            id=menu_id,
            children=[
                self._dropdown_item
            ],
            label='Select...',
            color='secondary',
            toggle_style=toggle_style
        )


@app.callback(
    Output({'parent-component': ALL, 'child-component': 'menu', 'index': MATCH}, 'label'),
    Input({'parent-component': ALL, 'child-component': 'checklist', 'index': MATCH}, 'value')
)
def update_dropdown_label(updates: list) -> list:
    if callback_context.triggered_id is None:
        raise PreventUpdate

    default_value = 'Select...'
    new_updates = []
    for update in updates:
        try:
            num_selections = len(update)
        except TypeError:
            # update is None
            new_updates.append(default_value)
        else:
            if num_selections == 0:
                # zero items selected
                new_updates.append(default_value)
            else:
                # multiple items selected
                new_updates.append(f'{num_selections} selected')

    return new_updates
