import mamba_ui as mui

from backend.display_widgets import display_widget
from backend.create_test_session import create_test_client
from backend.populate_uploads import populate_uploads
from backend.populate_menu_filters import populate_menu_filters


if __name__ == '__main__':

    # Serve dash app
    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
