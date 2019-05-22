#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:38:21 2017

@author: sksingh
"""

import urllib.request
from bs4 import BeautifulSoup
import re

url = input('Enter - ')

cnt = 1

while(cnt <= 7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')

    urlList = list()
    for tag in tags:
   
        urlList.append(tag.get('href', None))
    
    url = urlList[17]
    # slpi on dot
    
    words = re.findall("[\S]+_by_(\S+).html", url)
    print(words[0])
    
    
    cnt = cnt +1
    
    

 
        
    