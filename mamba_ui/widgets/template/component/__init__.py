from dash.exceptions import PreventUpdate
from dash import html, Input, Output, MATCH

from mamba_ui import app
from mamba_ui.components.base import BaseComponent


class TemplateExampleComponent(BaseComponent):

    name = 'Template Example'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)

    @property
    def component(self) -> html.Div:

        component_style = {
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'border': '1px solid black',
            'padding': '10px'
        }

        return html.Div(
            id=self.get_child_id('component'),
            children=[
                html.H1('Template Widget Component'),
                html.Button(
                    'Click Me!',
                    id=self.get_child_id('button')
                ),
                html.Span(
                    [html.Label('Number of button clicks: '), html.Span(id=self.get_child_id('output'))]
                )
            ],
            style=component_style
        )


@app.callback(
    Output(
        component_id={'name': 'template-example', 'type': 'output', 'index': MATCH},
        component_property='children'
    ),
    Input(
        component_id={'name': 'template-example', 'type': 'button', 'index': MATCH},
        component_property='n_clicks'
    )
)
def display_click_count(btn_click: int) -> str:
    """
    Callbacks within the component definition file are only acceptable if the input and output components are contained
    within the component itself. If the input or output component belongs to another widget or component then the
    callback should be defined in the backend.
    """
    if btn_click is None:
        raise PreventUpdate

    return str(btn_click)
