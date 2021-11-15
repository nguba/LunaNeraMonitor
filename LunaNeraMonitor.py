#!/usr/bin/env python3
import logging

from flask import Flask, send_from_directory, jsonify

from PXU import PXU


class LunaNeraServer:

    def __init__(self) -> None:
        self.pxu = PXU('COM4', device_id=5)
        logging.getLogger('werkzeug').setLevel(logging.ERROR)

    def read_pv(self):
        return self.pxu.read_pv()

    def is_open(self):
        return self.pxu.is_open()


server = LunaNeraServer()
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def hello_world():  # put application's code here
    return send_from_directory('static', "index.html")


@app.route('/pxu')
def update_reading():
    if server.is_open():
        return jsonify(
            pv=server.read_pv()
        )
    else:
        return jsonify(
            pv=0
        )


if __name__ == '__main__':
    app.run()
