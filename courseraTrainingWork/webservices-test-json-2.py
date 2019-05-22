#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:10:02 2017

@author: sksingh
"""




import urllib.request
import json



import urllib.parse



location = input("Enter the location : " )

serviceURL = 'http://python-data.dr-chuck.net/geojson?'

inputToService = 'sensor=false&address='+location

urlEncodedInput =  urllib.parse.urlencode({'sensor':'false', 'address':location})

completeURL = serviceURL+urlEncodedInput

data = urllib.request.urlopen(completeURL).read()



dictData = json.loads(data)



print(dictData["results"][0]["place_id"])