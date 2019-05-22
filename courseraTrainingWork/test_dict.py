#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:28:46 2017

@author: sksingh
"""

fhandle = open('romeo-and-juliet.txt')

wordDict = dict()

for line in fhandle:
    
   
    words = line.split()
    for word in words:
        wordDict[word] = wordDict.get(word,0) +1 
    
print (wordDict)
    