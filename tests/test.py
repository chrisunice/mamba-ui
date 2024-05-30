import dash
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Input, Output, Trigger, State, MATCH

import mamba_ui as mui
from mamba_ui.grid import widget_grid as WidgetGrid
from mamba_ui.pages.sandbox.layout import SandboxPageLayout
from mamba_ui.widgets import LinearPlotWidget
from mamba_ui.widgets import PolarPlotWidget


# @mui.app.callback(
#     Output('settings-window', 'is_open'),
#     Input('settings-icon', 'n_clicks'),
#     Trigger('dash-layout', 'children')
# )
# def open_settings(click):
#     if click is not None:
#         return True


@mui.app.callback(
    Output('external-stylesheet', 'href'),
    Input('theme-dropdown', 'value')
)
def change_theme(selected_theme):
    if selected_theme is not None:
        return selected_theme


@mui.app.callback(
    Output('page-container', 'children'),
    Input('grid-rows', 'value'),
    Input('grid-columns', 'value'),
    State('settings-window', 'is_open')
)
def update_grid_layout(nrows, ncols, settings_open):
    if settings_open:
        return WidgetGrid(nrows, ncols)
    else:
        raise PreventUpdate


@mui.app.callback(
    Output('page-container', 'children'),
    Input('url', 'pathname')
)
def go_to_sandbox_page(pathname):
    if pathname == '/sandbox':
        return SandboxPageLayout
    else:
        return WidgetGrid()


@mui.app.callback(
    Output({'type': 'widget-container', 'index': MATCH}, 'children'),
    [
        Input({'type': 'linear-plot-option', 'index': MATCH}, 'n_clicks'),
        Input({'type': 'polar-plot-option', 'index': MATCH}, 'n_clicks')
    ]

)
def display_widget(*widgets):
    if all(click is None for click in widgets):
        raise PreventUpdate
    else:
        widget_clicked_name = dash.callback_context.triggered_id['type']
        widget_clicked_uid = dash.callback_context.triggered_id['index']
        if widget_clicked_name == 'polar-plot-option':
            return PolarPlotWidget(widget_clicked_uid)
        elif widget_clicked_name == 'linear-plot-option':
            return LinearPlotWidget(widget_clicked_uid)
        else:
            raise PreventUpdate


@mui.app.callback(
    Output({'type': 'linear-plot', 'index': MATCH}, 'figure'),
    Input('theme-dropdown', 'value'),
    State({'type': 'linear-plot', 'index': MATCH}, 'figure'),
    State('theme-dropdown', 'options')

)
def update_linear_plot_style(theme_value, figure, theme_options):
    if theme_value is None:
        raise PreventUpdate
    else:
        theme_map = {option['value']: option['label'] for option in theme_options}
        theme_name = theme_map[theme_value]
        if theme_name in mui.config['themes']['light']:
            layout_updates = {
                'font': {'color': 'black'},
                'yaxis': {
                    'gridcolor': 'gray',
                    'zerolinecolor': 'black',
                    'zerolinewidth': 2,
                },
                'xaxis': {
                    'gridcolor': 'gray',
                    'zerolinecolor': 'black',
                    'zerolinewidth': 2,
                }
            }
        elif theme_name in mui.config['themes']['dark']:
            layout_updates = {
                'font': {'color': 'white'},
                'yaxis': {
                    'gridcolor': 'lightgray',
                    'zerolinecolor': 'white',
                    'zerolinewidth': 2

                },
                'xaxis': {
                    'gridcolor': 'lightgray',
                    'zerolinecolor': 'white',
                    'zerolinewidth': 2,

                }
            }
        else:
            layout_updates = {}
        figure['layout'].update(layout_updates)
        return figure


if __name__ == '__main__':

    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
