import time
import requests
from flask import request
from multiprocessing import Process

import mamba_ui as mui


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def post_shutdown(ip, port):
    time.sleep(1)
    requests.post(f'{ip}:{port}/shutdown')


def test_app_launch():

    ip_address = '127.0.0.1'
    port = '8050'

    # Set up the app
    mui.app.layout = mui.serve_layout()

    @mui.app.server.route('/shutdown', methods=['POST'])
    def shutdown():
        shutdown_server()
        return 'Server shutting down...'

    # Process 1: Run application
    p1 = Process(target=mui.app.run, kwargs=dict(host=ip_address, port=port))
    p1.start()

    # Process 2:
    p2 = Process(target=post_shutdown, args=(ip_address, port))
    p2.start()

    assert True
