from dash import callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, MATCH, ALL

from mamba_ui import app
from mamba_ui.components.base import BaseComponent


class DropdownChecklistComponent(BaseComponent):

    name = 'Dropdown Checklist'

    def __init__(self, options: list, name: str = None, index: str = None, ):
        super().__init__(name, index)
        self.options = options

    @property
    def _checklist(self):
        """ dbc.Checklist sub component """

        return dbc.Checklist(
            id=self.get_child_id('checklist'),
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

        return dbc.DropdownMenuItem(
            className='dropdown-checklist-menu-item',
            id=self.get_child_id('menu-item'),
            children=[self._checklist],
            toggle=False,
            style=style
        )

    @property
    def component(self):

        toggle_style = {
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center',
            'width': '100%',
        }

        return dbc.DropdownMenu(
            id=self.get_child_id('menu'),
            children=[
                self._dropdown_item
            ],
            label='Select...',
            color='secondary',
            toggle_style=toggle_style
        )


@app.callback(
    Output({'name': ALL, 'type': 'menu', 'index': MATCH}, 'label'),
    Input({'name': ALL, 'type': 'checklist', 'index': MATCH}, 'value')
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
            elif num_selections == 1:
                # display the selection
                new_updates.append(update)
            else:
                # multiple items selected
                new_updates.append(f'{num_selections} selected')

    return new_updates
