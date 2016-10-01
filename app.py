# coding: utf-8
import json
from flask import Flask, jsonify, request
from flask import render_template
from db import REDIS


app = Flask(__name__)


@app.route('/')
def index():
    repos = [(key, json.loads(value)) for key, value in REDIS.hgetall('repos').items()]
    return render_template('index.html', repos=repos, keywords=REDIS.get('keywords').decode('utf-8'))


@app.route('/del_repo', methods=['DELETE'])
def del_repo():
    if request.method == 'DELETE':
        repo = request.args.get('repo', None)
        if repo:
            desc = REDIS.hget('repos', repo)
            desc = json.loads(desc)
            desc.update(is_show='0')
            REDIS.hset('repos', repo, json.dumps(desc))
            return jsonify({"status": True})


if __name__ == '__main__':
    app.run()
