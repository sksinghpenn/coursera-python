#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:38:21 2017

@author: sksingh
"""




import urllib
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_375265.html").read()



soup = BeautifulSoup(html)

tags = soup.find_all('a')

listOfNum = list()
for tag in tags:
    href = tag.get("href", None)
    listOfNum.append(int(spanContent))

sumOfNums = sum(listOfNum)
print(sumOfNums)