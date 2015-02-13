#!/usr/bin/env python
# coding=utf-8

import json
from pprint import pprint

with open(unicode('data/report.json')) as data_file:
    print data_file
    data = json.load(data_file)
pprint(data)