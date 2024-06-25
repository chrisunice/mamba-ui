import mamba_ui as mui

from backend.general.create_test_session import create_test_client
# from backend.general.display_widgets import display_widget
# from backend.general.close_sidebar_on_submit import close_sidebar_on_submit

from backend.settings.toggle_settings_window import toggle_settings_window
from backend.settings.update_grid_layout import update_grid_layout
from backend.settings.update_app_theme import update_app_theme, update_polar_plot_theme, update_linear_plot_theme

# from backend.plots.populate_menu_filters import populate_menu_filters
# from backend.plots.populate_menu_display import populate_menu_display
# from backend.plots.plot_linear_data import plot_linear_data
# from backend.plots.reset_linear_plot import reset_linear_plot

if __name__ == '__main__':

    # Serve dash app
    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
