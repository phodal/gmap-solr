from flask import Flask
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
        query = 'geo%3A%22IsWithin(POLYGON((9.167648038864687+45.47779519240331%2C9.2129666423803+45.44432337237933%2C9.216399869919362+45.48501671903388%2C9.167648038864687+45.47779519240331)))+distErrPct%3D0%22+&wt=json&indent=true'
        result = requests.get((base_url + ('select?q=' + query)))
        return result.json(), 201, {'Access-Control-Allow-Origin': '*'}


api.add_resource(All, '/geo/')

@app.route('/')
def root():
    return app.send_static_file('google.html')

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)