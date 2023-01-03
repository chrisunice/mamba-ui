from dash import Input, Output

import mamba_ui as mui


@mui.app.callback(
    Output('page-container', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/home':
        return mui.pages.home.layout
    elif pathname == '/data-vis':
        return mui.pages.data_vis.layout
    elif pathname == '/imagery':
        return mui.pages.imagery.layout
    elif pathname == '/mission-planning':
        return mui.pages.missionplanning.layout
    else:
        # todo add an alert here
        return mui.pages.home.layout


@mui.app.callback(
    Output('menubar', 'is_open'),
    Input('navbar', 'children')
)
def show_sidebar(_):
    return True


if __name__ == '__main__':

    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8888)
