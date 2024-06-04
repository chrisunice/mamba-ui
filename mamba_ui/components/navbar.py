from dash import html
from dash_extensions.enrich import Input, Output, Trigger

from mamba_ui import app
from mamba_ui.components.base import BaseComponent
from mamba_ui.settings.window import SettingsWindow


class NavBar(BaseComponent):
    def __init__(self):
        super().__init__()

    @property
    def _title(self) -> html.H1:
        title_style = {
            'fontStyle': 'oblique',
            'margin': '5px 0px',
            'cursor': 'pointer'
        }

        return html.H1(
            children=['D\u2074'],
        title='Denmar Data analysis Dashboard and Database',
        style=title_style,
        className='text-light'
    )

    @property
    def _settings_icon(self) -> html.I:
        return html.I(
            id='settings-icon',
            className='fa-solid fa-gear fa-2xl text-light',
        )

    @property
    def component(self) -> html.Div:
        navbar_style = {
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center',
            'padding': '0px 20px'
        }
        return html.Div(
            id='navbar',
            className='bg-primary',
            children=[
                self._title,
                self._settings_icon,
                SettingsWindow().component
            ],
            style=navbar_style
        )


@app.callback(
    Output('settings-window', 'is_open'),
    Input('settings-icon', 'n_clicks'),
    Trigger('dash-layout', 'children')
)
def open_settings(click):
    if click is not None:
        return True
