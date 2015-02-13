#!/usr/bin/env python
# coding=utf-8

import json
from pprint import pprint

json_data = open('data/report.json')

data = json.load(json_data)
pprint(data)
json_data.close()