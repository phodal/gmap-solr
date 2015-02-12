import json
import logging
import uuid
from wsgiref import simple_server

import falcon
import requests

class SinkAdapter(object):
    def __call__(self, req, resp):
        params = {'q': req.get_param('q', True)}
        print params
        resp.body = "something"

app = falcon.API()

sink = SinkAdapter()
app.add_sink(sink, r'/search/geo')

# Useful for debugging problems in your API; works with pdb.set_trace()
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()