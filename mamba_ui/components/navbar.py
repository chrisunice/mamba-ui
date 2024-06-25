from dash import html, Input, Output

from mamba_ui.components.base import BaseComponent
from mamba_ui.settings.window import SettingsWindow


class NavbarComponent(BaseComponent):

    name = 'Navbar'

    def __init__(self, name: str = None, index: str = None):
        super().__init__(name, index)

    @property
    def _title(self) -> html.H1:

        title_style = {
            'fontStyle': 'oblique',
            'margin': '5px 0px',
            'cursor': 'pointer'
        }

        return html.H1(
            id=self.get_child_id('title'),
            children=['D\u2074'],
            title='Denmar Data analysis Dashboard and Database',
            style=title_style,
            className='text-light'
        )

    @property
    def _settings_icon(self) -> html.I:
        return html.I(
            id=self.get_child_id('settings-icon'),
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
            id=self.id,
            className='bg-primary',
            children=[
                self._title,
                self._settings_icon,
                SettingsWindow().component
            ],
            style=navbar_style
        )
