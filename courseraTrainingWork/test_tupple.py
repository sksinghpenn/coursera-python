#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:28:46 2017

@author: sksingh
"""

d = {'a':10,'b':1,'c':22}


x = d.items()


myList = list()
for key,value in x:
    myList.append((key,value))
    
myList.sort()
print(myList)