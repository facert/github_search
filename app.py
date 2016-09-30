# coding: utf-8
import json
from flask import Flask
from flask import render_template
from db import REDIS


app = Flask(__name__)


@app.route('/')
def index():
    repos = [(key, json.loads(value)) for key, value in REDIS.hgetall('repos').items()]
    return render_template('index.html', repos=repos)


if __name__ == '__main__':
    app.run()
