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
        print request.query_string
        base_url = ''
        query = request.query_string
        result = requests.get((base_url + ('select?q=' + query)))
        return (result.json()), 201, {'Access-Control-Allow-Origin': '*'}


api.add_resource(All, '/geo/')


@app.route('/')
def root():
    return app.send_static_file('google.html')


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True)