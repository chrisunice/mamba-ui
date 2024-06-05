import os
import shutil
import dash_uploader as du
from dash_extensions.enrich import Output, MATCH

from mamba_ui import config


@du.callback(
    Output({'type': 'widget-menu-data-checklist', 'index': MATCH}, 'options'),
    id={'type': 'widget-menu-data-upload', 'index': MATCH},
)
def populate_uploads(status):
    """ Moves uploaded files from app temp upload directory to client directory and populates data checklist """
    # Uploaded files in the temp upload directory
    uploaded_files = [str(upload) for upload in status.uploaded_files]

    # Make client an upload directory if one doesn't already exist
    username = 'ui_test_client'
    target_dir = f"{config['paths']['root_directory']}\\clients\\{username}\\uploads"
    os.makedirs(target_dir, exist_ok=True)

    # Move the files
    # Build the list of checklist options
    options = []
    for upload in uploaded_files:
        fname = os.path.basename(upload)
        target_fpath = os.path.join(target_dir, fname)
        shutil.move(upload, target_fpath)
        options.append(
            {'label': fname, 'value': target_fpath}
        )

    return options
