# from dash import html
# import dash_bootstrap_templates as dbt
# import dash_bootstrap_components as dbc
# from dash_draggable import DraggableDashboard
#
#
# def generate_grid_layout(rows, columns):
#
#     grid_style = {
#         'width': '100%',
#         'margin': '0px',
#         'padding': '0px'
#     }
#
#     row_style = {
#         'border': '1px solid green',
#         'margin': '0px',
#         'padding': '5px'
#     }
#
#     col_style = {
#         'border': '1px solid red',
#         'margin': '0px 5px 0px 5px',
#         'padding': '0px'
#     }
#
#     grid_children = []
#
#     for r in range(rows):
#         row_children = []
#         for c in range(columns):
#             row_children.append(
#                 dbc.Col(id=f'col-{c}', style=col_style)
#             )
#         grid_children.append(
#             dbc.Row(id=f'row-{r}', children=row_children, style=row_style)
#         )
#
#     grid = dbc.Row(id='grid-layout', children=grid_children, style=grid_style)
#     return grid
#
#
# # Define the number of rows and columns in the grid
# num_rows = 2
# num_columns = 2
#
# # Generate the grid layout
# layout = generate_grid_layout(num_rows, num_columns)
#
# # layout = dbc.Row(id='grid-layout', children=[
# #     dbc.Row(children=[
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #     ], style=dict(border='1px solid green', padding=0, margin=0)),
# #     dbc.Row(children=[
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #     ], style=dict(border='1px solid green', padding=0, margin=0)),
# #     dbc.Row(children=[
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #         dbc.Col(style=dict(border='1px solid red')),
# #     ], style=dict(border='1px solid green', padding=0, margin=0))
# # ], style=dict(width='100%', padding=0, margin=0))
