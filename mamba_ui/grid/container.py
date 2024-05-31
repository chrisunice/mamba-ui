from dash import html

from mamba_ui.grid.base import WidgetGridBase
from mamba_ui.grid.icon import WidgetIconComponent


class WidgetContainerComponent(WidgetGridBase):
    def __init__(self, row_id: int = 0, column_id: int = 0):
        super().__init__()
        self.row_id = row_id
        self.column_id = column_id

    @property
    def component(self) -> html.Div:

        uid = f'r{self.row_id}c{self.column_id}'

        container_style = {
            'display': 'flex',
            'flexGrow': '1',
            'flexDirection': 'column',
            'justifyContent': 'center',
            'alignItems': 'center',
            'margin': '0px 5px 0px 5px',
            'padding': '0px',
            'borderRadius': '5px',
            'backgroundColor': 'rgba(0, 0, 0, 0)',
            'boxShadow': '0px 0px 10px gray'
        }

        return html.Div(
            id={'type': 'widget-container', 'index': uid},
            className='bg-transparent border border-secondary',
            children=[WidgetIconComponent(self.row_id, self.column_id).json],
            style=container_style
        )
