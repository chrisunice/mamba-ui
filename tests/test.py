import mamba_ui as mui

# app
from backend.general.create_test_session import create_test_client

# grid
from backend.grid.toggle_sidebar import toggle_sidebar
from backend.grid.display_widgets import display_widget

# settings
from backend.settings.toggle_settings_window import toggle_settings_window
from backend.settings.update_grid_layout import update_grid_layout
from backend.settings.update_app_theme import update_app_theme, update_polar_plot_theme, update_linear_plot_theme

# plots
from backend.plots.populate_menu_display import populate_menu_display
from backend.plots.populate_menu_filters import populate_menu_filters
from backend.plots.plot_linear_data import plot_linear_data
from backend.plots.close_sidebar_on_submit import close_sidebar_on_submit
from backend.plots.reset_linear_plot import reset_linear_plot
from backend.plots.reset_plot_menu import reset_plot_menu

if __name__ == '__main__':

    # Serve dash app
    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
