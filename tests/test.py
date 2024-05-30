import mamba_ui as mui
from backend_callbacks import *


if __name__ == '__main__':

    mui.app.layout = mui.serve_layout()
    mui.app.run(debug=True, port=8050)
