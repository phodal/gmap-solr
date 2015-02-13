#!/usr/bin/env python
# coding=utf-8

import json

with open(unicode('data/report.json')) as data_file:
    print data_file
    data = json.load(data_file)

for ip in data['hosts']:
    print ip['data']