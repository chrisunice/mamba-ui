from dash import html

from mamba_ui import STANDARD_WIDTH
from mamba_ui.components import HorizontalLine, SubmitButtonGroup
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
    'font-size': 'min(24px, 1.5vmax)',
}

marks = {val: str(val) for val in [-180, 0, 180]}

InputContainer = html.Div(
    id='col-left',
    children=[
        ContainerTitle('Input'),
        HorizontalLine('lg'),
        DropdownItem('Platform Database'),
        DropdownItem('Air Vehicle Configuration'),
        DropdownItem('Air Vehicle Sub Configuration'),
        DropdownItem('Missions'),
        DropdownItem('Vector Groups'),
        HorizontalLine('sm'),
        RangeSliderItem('Look Range', -180, 180),
        InputItem('Look Bin Width', input_kwargs=dict(min=0, max=180)),
        RangeSliderItem('Depression Range', -90, 90),
        InputItem('Depression Bin Width', input_kwargs=dict(min=0, max=90)),
        HorizontalLine('sm'),
        InputItem('Minimum Hits/Bin', input_kwargs=dict(min=1)),
        InputItem('Minimum Missions/Bin', input_kwargs=dict(min=1)),
        HorizontalLine('sm'),
        DropdownItem('Compute Metric'),
        InputItem('Percentile', input_kwargs=dict(min=0, max=100)),
        HorizontalLine('sm'),
        html.Div(
            SubmitButtonGroup('mission-planning-page'),
            style=dict(width='min(100%, 750px)')
        )
    ],
    style=style
)

