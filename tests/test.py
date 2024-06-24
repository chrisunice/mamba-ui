import mamba_ui as mui

from backend.create_test_session import create_test_client
from backend.display_widgets import display_widget
from backend.populate_menu_filters import populate_menu_filters
from backend.populate_menu_display import populate_menu_display
from backend.plot_linear_data import plot_linear_data
from backend.close_sidebar_on_submit import close_sidebar_on_submit

if __name__ == '__main__':

    # Serve dash app
    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
