from mamba_ui.components.base import BaseComponent


class BasePlotComponent(BaseComponent):
    def __init__(self, _index: str = ""):
        super().__init__()
        self._index = _index

    @property
    def component(self):
        return None
