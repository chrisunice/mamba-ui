from mamba_ui.widgets.plots.base.menu import BasePlotMenuComponent


class PolarPlotMenuComponent(BasePlotMenuComponent):

    name = 'Polar Plot Menu'

    def __init__(self, index: str, name: str = None):
        super().__init__(name=name, index=index)
