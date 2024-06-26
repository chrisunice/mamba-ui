from mamba_ui.widgets.plots.base.menu import BasePlotMenuComponent


class LinearPlotMenuComponent(BasePlotMenuComponent):

    name = 'Linear Plot Menu'

    def __init__(self, index: str, name: str = None):
        super().__init__(index=index, name=name)
