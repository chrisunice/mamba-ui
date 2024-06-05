from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.template.component import TemplateExampleComponent
from mamba_ui.widgets.template.menu import TemplateExampleMenuComponent


class TemplateExampleWidget(BaseWidget):

    widget_name = 'Template Example'

    def __init__(self, index: str = ""):
        """

        :param index:
        """
        super().__init__(index)

    @property
    def component(self):
        return TemplateExampleComponent(self.index).component

    @property
    def menu(self):
        return TemplateExampleMenuComponent(self.index).component
