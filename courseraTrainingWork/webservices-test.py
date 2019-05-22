#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:10:02 2017

@author: sksingh
"""




import urllib.request
import xml.etree.ElementTree as ET

xmlString =  urllib.request.urlopen('http://python-data.dr-chuck.net/comments_375262.xml').read() 

#print(xmlString)

root = ET.fromstring(xmlString)

allComments = root.find('comments')

countList = list()

for comment in allComments:
    count = comment.find('count').text
    countList.append (int(count))

total = sum(countList)
print(total)
