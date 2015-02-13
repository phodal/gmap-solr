#!/usr/bin/env python
# coding=utf-8

from flask import Flask, request
from flask.ext import restful
from flask_restful import Resource
import requests

app = Flask(__name__, static_url_path='')
app.secret_key = 'why would I tell you my secret key?'

api = restful.Api(app)


class All(Resource):
    @staticmethod
    def get():
        base_url = ''
        url = (base_url + 'select?q=' + request.query_string + '+&wt=json&indent=true')
        result = requests.get(url)
        return (result.json()['response']['docs']), 201, {'Access-Control-Allow-Origin': '*'}


api.add_resource(All, '/geo/')


@app.route('/google')
def google():
    return app.send_static_file('google.html')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True)