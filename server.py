from flask import Flask
from flask.ext import restful
from flask_restful import Resource

app = Flask(__name__, static_url_path='')
app.secret_key = 'why would I tell you my secret key?'

api = restful.Api(app)


class All(Resource):
    @staticmethod
    def get():
        return "", 201, {'Access-Control-Allow-Origin': '*'}


@app.route('/')
def root():
    return app.send_static_file('google.html')

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)