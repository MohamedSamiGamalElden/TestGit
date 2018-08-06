# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:59:41 2018

@author: Mohamed Gamaleldin
"""

import requests
import json
import urllib.request  as urllib2 




url = 'http://18.220.55.195/jreq/' # my website


payload={"name":"Ahmed","payload":"230"}

headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)



print(response.text)

