#!/usr/bin/env python3
from random import random

from flask import Flask, send_from_directory, jsonify

from PXU import PXU

app = Flask(__name__, static_url_path='', static_folder='static')
pxu = PXU('COM4', device_id=5)


@app.route('/')
def hello_world():  # put application's code here
    return send_from_directory('static', "index.html")


@app.route('/pxu')
def update_reading():
    return jsonify(
        pv=random()
    )


if __name__ == '__main__':
    app.run()
