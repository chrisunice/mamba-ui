from dash import html

from mamba_ui import config
from mamba_ui import STANDARD_WIDTH
from mamba_ui.components import HorizontalLine
from .container_title import container_title as ContainerTitle
from .dropdown_item import dropdown_item as DropdownItem
from .rangeslider_item import rangeslider_item as RangeSliderItem
from .input_item import input_item as InputItem

style = {
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'width': '50%',
    'max-width': STANDARD_WIDTH/2,
    'padding': '10px',
    'margin-right': '5px',
    'font-size': 'min(20px, 1.5vmax)',
}


InputContainer = html.Div(
    id='col-left',
    children=[
        ContainerTitle('Input'),
        HorizontalLine('lg'),
        DropdownItem('row-1', 'Platform Database'),
        DropdownItem('row-2', 'Air Vehicle Configuration', dropdown_kwargs=dict(multi=True)),
        DropdownItem('row-3', 'Air Vehicle Sub Configuration', dropdown_kwargs=dict(multi=True)),
        DropdownItem('row-4', 'Missions', dropdown_kwargs=dict(multi=True)),
        DropdownItem('row-5', 'Vector Groups', dropdown_kwargs=dict(multi=True)),
        HorizontalLine('sm'),
        RangeSliderItem('row-6', 'Look Range', slider_kwargs=dict(min=-180, max=180, step=30)),
        InputItem('row-7', 'Look Bin Width', input_kwargs=dict(min=0, max=180)),
        RangeSliderItem('row-8', 'Depression Range', slider_kwargs=dict(min=-90, max=90, step=15)),
        InputItem('row-9', 'Depression Bin Width', input_kwargs=dict(min=0, max=90)),
        HorizontalLine('sm'),
        InputItem('row-10', 'Minimum Hits/Bin', input_kwargs=dict(min=1)),
        InputItem('row-11', 'Minimum Missions/Bin', input_kwargs=dict(min=1)),
        HorizontalLine('sm'),
        DropdownItem(
            container_name='row-12',
            label_text='Compute Metric',
            dropdown_kwargs=dict(
                options=list(map(lambda x: x.capitalize(), config['missionplanning']['metrics'].split(', ')))
            )
        ),
        InputItem('row-13', 'Percentile', input_kwargs=dict(min=0, max=100))
    ],
    style=style
)

