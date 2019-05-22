#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:10:02 2017

@author: sksingh
"""




import urllib.request
import json

jsonData =  urllib.request.urlopen('http://python-data.dr-chuck.net/comments_375266.json').read() 

jsonObjectAsDict = json.loads(jsonData)

commentsDict = jsonObjectAsDict["comments"]


numList = list()

for comment in commentsDict:
    count = comment["count"]
    numList.append(int(count))
    
print (sum(numList))