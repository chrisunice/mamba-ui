import numpy as np
from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.components.base import BaseComponent
from mamba_ui.grid.tile import WidgetGridTileComponent
from mamba_ui.utils.component2json import component2json


class WidgetGridComponent(BaseComponent):

    def __init__(self, shape: tuple = (1, 1), widgets: list[dict] = None):
        super().__init__()

        # Handle arguments
        self.shape = shape
        self.size = np.product(self.shape)
        if widgets is None:
            widgets = []
        self.widgets = widgets

        # Add or remove widgets
        if self.size > len(self.widgets):
            self.widgets = self.add_widgets()
        elif self.size < len(self.widgets):
            self.widgets = self.remove_widgets()
        else:
            pass    # Do nothing

        # Resize widgets
        self.widgets = self.resize_widgets()

        # Reshape widget list to desired shape
        self.widgets = self.reshape_widgets()

    @property
    def component(self) -> dbc.Row:

        # Styling
        grid_style = {
            'display': 'flex',
            'flexGrow': '1',
            'width': '100%',
            'margin': '0px',
            'padding': '0px'
        }

        row_style = {
            'display': 'flex',
            'height': f'{100/self.shape[0]}%',
            'margin': '0px',
            'padding': '5px'
        }

        # Component
        grid_children = []
        for i in range(self.shape[0]):
            row_children = []
            for j in range(self.shape[1]):
                # Grab the widget by grid position
                widget = self.widgets[i][j]

                # Update index based on grid position
                self.update_index(widget, f'r{i}c{j}')

                # Store in row
                row_children.append(widget)

            # Store in grid
            grid_children.append(html.Div(id=f'grid-row-{i}', children=row_children, style=row_style))

        # Store in layout
        grid = dbc.Row(id='grid-layout', children=grid_children, style=grid_style)
        return grid

    def add_widgets(self) -> list:
        """ Appending more widgets to the list of existing widgets """
        num_widgets_under = self.size - len(self.widgets)
        return self.widgets + [WidgetGridTileComponent().component for _ in range(num_widgets_under)]

    def remove_widgets(self) -> list:
        """ Removing widgets in reverse order of creation """
        num_widgets_over = len(self.widgets) - self.size
        return self.widgets[:-num_widgets_over]

    def resize_widgets(self) -> list[dict]:
        """ Resizing widget width; height is resized at the grid row level """
        new_width = {'width': f'{100/self.shape[1]}%'}

        resized_widgets = []
        for widget in self.widgets:
            widget_json = component2json(widget)
            widget_json['props']['style'].update(new_width)
            resized_widgets.append(widget_json)

        return resized_widgets

    def reshape_widgets(self):
        """ List version of np.array.reshape because of complex elements in list """
        if len(self.widgets) != self.size:
            raise ValueError(f"Cannot reshape a {self.size} widgets into shape {self.shape}")
        n, m = self.shape
        return [self.widgets[i * m:(i + 1) * m] for i in range(n)]

    def update_index(self, obj: list | dict, index: str):
        """ Updates all the id['index'] values down the component tree assuming that the tree is all json """
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'id' and 'index' in v:
                    v['index'] = index
                elif isinstance(v, (dict, list)):
                    self.update_index(v, index)
        elif isinstance(obj, list):
            for item in obj:
                self.update_index(item, index)
