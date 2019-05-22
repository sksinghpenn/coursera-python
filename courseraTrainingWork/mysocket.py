#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 20:16:31 2017

@author: sksingh
"""



import urllib
import BeautifulSoup

html = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_42.html").read()



soup = BeautifulSoup(html)

tags = soup.find_all('span')

for tag in tags:
    print (tag)