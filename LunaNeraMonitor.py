#!/usr/bin/env python3
import logging, signal, os
import time
from datetime import datetime

from flask import Flask, send_from_directory, jsonify
from flask.json import dump

from PXU import PXU


class LunaNeraServer:

    def __init__(self) -> None:
        self.pxu = PXU('COM4', device_id=3)
        self.pxu2 = PXU('COM4', device_id=5)
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        self.fermentationLog = open('fermentation.log', 'w')

    def read_pv(self):
        print(self.pxu2.read_pv())
        return self.pxu.read_pv()

    def is_open(self):
        return self.pxu.is_open()

    def close(self):
        self.fermentationLog.close()

    def get_fermentation_log(self):
        return self.fermentationLog

    def read_status(self):
        return self.pxu.status


server = LunaNeraServer()


def signal_handler(signum, frame):
    server.close()
    print('Server shutdown')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():  # put application's code here
    return send_from_directory('static', "index.html")


class Message(dict):
    def __init__(self, pv, timestamp, status) -> None:
        dict.__init__(self, k=timestamp, v=pv, s=status)


@app.route('/pxu')
def update_reading():
    msg = Message(server.read_pv(), time.time() * 1000, server.read_status())
    dump(msg, server.fermentationLog, indent=0)
    server.fermentationLog.flush()
    return jsonify(
        msg
    )


if __name__ == '__main__':
    app.run()
