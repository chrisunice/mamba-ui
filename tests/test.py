from dash_extensions.enrich import Input, Output

import mamba_ui as mui


@mui.app.callback(
    Output('page-container', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/home':
        return mui.pages.home.layout
    elif pathname == '/data-vis':
        return mui.pages.datavis.layout
    elif pathname == '/imagery':
        return mui.pages.imagery.layout
    elif pathname == '/mission-planning':
        return mui.pages.missionplanning.layout
    else:
        # todo add an alert here
        return mui.pages.home.layout


# @mui.app.callback(
#     Output('menubar', 'is_open'),
#     Trigger('page-container', 'children')
# )
# def show_menu():
#     return True
#
#
# @mui.app.callback(
#     Output('settings-modal', 'is_open'),
#     Trigger('page-container', 'children')
# )
# def show_menu():
#     return True


@mui.app.callback(
    Output('mission-planning-download-modal', 'is_open'),
    Input('mission-planning-page', 'children')
)
def trigger_component(_):
    return True


@mui.app.callback(
    Output('mission-planning-download', 'data'),
    Input('mission-planning-download-button', 'n_clicks')
)
def download(click):
    if click is not None:
        return dict(content='hello', filename='hello.dbin')


if __name__ == '__main__':

    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8888)
