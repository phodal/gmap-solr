#!/usr/bin/env python
# coding=utf-8

import json
import urllib

with open(unicode('data/report.json')) as data_file:
    data = json.load(data_file)

for ip in data['hosts']:
    response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=' + ip['data'] + '&position=true').read()
    print response
