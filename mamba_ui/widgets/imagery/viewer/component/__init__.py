import base64
from dash import html

from mamba_ui import PKG_DIR
from mamba_ui.components.base import BaseComponent


class ImageryViewerComponent(BaseComponent):
    def __init__(self, _index: str = ""):
        super().__init__()
        self._index = _index

    @staticmethod
    def get_default_image() -> str:
        # path_to_image = f'{PKG_DIR}/static/black_image.jpg'
        path_to_image = r"C:\Gadiva\f35synth\f35synth\output\xvv-311m000-f35a.X.baseupper.withovl.png"
        encoded_image = base64.b64encode(open(path_to_image, 'rb').read())
        image_string = 'data:image/jpg;base64,{}'.format(encoded_image.decode())
        return image_string

    @property
    def component(self) -> html.Div:

        container_style = {
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'width': '100%',
            'height': '100%',
            'padding': '10px'
        }

        image_style = {
            'width': 'auto',
            'maxWidth': '100%',
            'height': '100%',
            'objectFit': 'contain'
        }

        return html.Div(
            children=[
                html.Img(
                    id={'type': 'imagery-viewer', 'index': self._index},
                    src=self.get_default_image(),
                    style=image_style
                )
            ],
            style=container_style
        )
