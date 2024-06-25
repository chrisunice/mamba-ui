from mamba_ui.widgets.base import BaseWidget

from mamba_ui.widgets.template.component import TemplateExampleComponent
from mamba_ui.widgets.template.menu import TemplateExampleMenuComponent


class TemplateExampleWidget(BaseWidget):

    widget_name = 'Template Example'

    def __init__(self, index: str = ""):
        """
        Template Example Component is essentially a wrapper for a component and a menu. Together they make up a widget.

        :param index: a unique index to identify which tile in the widget grid the component belongs to.
            Typically, `r0c0` notation is used to correspond to the tile in the first row and first column
        """
        super().__init__(index)

    @property
    def component(self):
        return TemplateExampleComponent(self.index).component

    @property
    def menu(self):
        return TemplateExampleMenuComponent(self.index).component
