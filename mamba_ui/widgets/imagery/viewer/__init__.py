from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.imagery.viewer.menu import ImageryViewerMenuComponent
from mamba_ui.widgets.imagery.viewer.component import ImageryViewerComponent


class ImageryViewerWidget(BaseWidget):

    widget_name = 'Imagery Viewer'

    def __init__(self, index: str = ""):
        """

        :param index:
        """
        super().__init__(index)

    @property
    def component(self):
        return ImageryViewerComponent(self.index).component

    @property
    def menu(self):
        return ImageryViewerMenuComponent(self.index).component
