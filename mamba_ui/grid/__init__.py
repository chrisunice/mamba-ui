import numpy as np
from dash import html
import dash_bootstrap_components as dbc

from mamba_ui.grid.base import WidgetGridComponentBase
from mamba_ui.grid.tile import WidgetGridTileComponent


class WidgetGridComponent(WidgetGridComponentBase):

    def __init__(self, shape: tuple = (1, 1), widgets: list[dict] = None):
        super().__init__()

        # Handle arguments
        self.shape = shape
        self.size = np.product(self.shape)
        if widgets is None:
            widgets = [WidgetGridTileComponent().json]
        self.widgets = widgets

        # Add or remove widgets
        if self.size > len(self.widgets):
            self.widgets = self.add_widgets()
        elif self.size < len(self.widgets):
            self.widgets = self.remove_widgets()
        else:
            pass    # Do nothing

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
        num_widgets_under = self.size - len(self.widgets)
        for i in range(num_widgets_under):
            self.widgets.append(WidgetGridTileComponent().json)
        return self.widgets

    def remove_widgets(self) -> list:
        num_widgets_over = len(self.widgets) - self.size
        return self.widgets[:-num_widgets_over]

    def reshape_widgets(self) -> list:
        widget_array = np.array(self.widgets)
        widget_array = widget_array.reshape(self.shape)
        return widget_array.tolist()

    def update_index(self, obj, index):
        """
        Updates all the id['index'] values down the component tree assuming that the tree is all json
        """
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'id' and 'index' in v:
                    v['index'] = index
                elif isinstance(v, (dict, list)):
                    self.update_index(v, index)
        elif isinstance(obj, list):
            for item in obj:
                self.update_index(item, index)
