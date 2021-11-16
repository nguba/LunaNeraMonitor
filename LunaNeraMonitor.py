#!/usr/bin/env python3
import logging, signal, os
import time
from datetime import datetime

from flask import Flask, send_from_directory, jsonify
from flask.json import dump

from PXU import PXU


class LunaNeraServer:

    def __init__(self) -> None:
        self.pxu = PXU('COM4', device_id=5)
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        self.fermentationLog = open('fermentation.json', 'w')

    def read_pv(self):
        return self.pxu.read_pv()

    def is_open(self):
        return self.pxu.is_open()

    def close(self):
        self.fermentationLog.close()

    def get_fermentation_log(self):
        return self.fermentationLog


server = LunaNeraServer()


def signal_handler(signum, frame):
    server.close()
    print('Server shutdown')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def hello_world():  # put application's code here
    return send_from_directory('static', "index.html")


class Message(dict):
    def __init__(self, pv, timestamp) -> None:
        dict.__init__(self, k=timestamp, v=pv)


@app.route('/pxu')
def update_reading():
    msg = Message(server.read_pv(), time.time() * 1000)
    json = jsonify(
        msg
    )
    print(json.json)
    dump(msg, server.fermentationLog, indent=0)
    server.fermentationLog.flush()
    return json


if __name__ == '__main__':
    app.run()
