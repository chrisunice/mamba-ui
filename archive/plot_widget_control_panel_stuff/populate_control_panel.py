# from dash.exceptions import PreventUpdate
# from dash import Input, Output, State, MATCH, callback_context, ALL
#
# import mamba_ui as mui
#
#
# @mui.app.callback(
#     Output({'parent-component': 'plot-control-panel', 'child-component': 'dropdown', 'index': MATCH}, 'options'),
#     Input({'type': 'widget-submit-button', 'index': MATCH}, 'n_clicks'),
#     State({'parent-component': ALL, 'child-component': 'checklist', 'index': MATCH}, 'options')
# )
# def populate_control_panel(submit_click: int, _: str):
#     if callback_context.triggered_id is None or submit_click is None:
#         raise PreventUpdate
#
#     def get_names(lst):
#         """ Recursive helper function to get the names from the state variables """
#         names = []
#         for item in lst:
#             if isinstance(item, list):
#                 names.extend(get_names(item))
#             elif isinstance(item, dict):
#                 name = item['id']['parent-component'].split('-')[0]
#                 names.append(name)
#         return names
#
#     categorical_names = get_names(callback_context.states_list)
#     return list(map(lambda x: x.capitalize(), categorical_names))
