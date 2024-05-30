from dash import html

from mamba_ui.grid.icon import build_widget_icon as WidgetIcon


class WidgetContainerComponent:
    def __init__(self, row_id: int = 0, column_id: int = 0):
        self.row_id = row_id
        self.column_id = column_id

    @property
    def component(self) -> html.Div:
        style = {
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
            id={'type': 'widget-container', 'index': f'r{self.row_id}c{self.column_id}'},
            className='bg-transparent border border-secondary',
            children=[WidgetIcon(self.row_id, self.column_id)],
            style=style
        )

    @property
    def json(self) -> dict:
        return self.component.to_plotly_json()
