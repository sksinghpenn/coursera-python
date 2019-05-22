#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 10:42:54 2017

@author: sksingh
"""

while True:
    
    line = input('Please enter a line: ')
    
    """
    if (len(line) > 0) and  (line[0] == '#'):
        continue
    """
    
    if (line.startwith("#")):
        continue
    elif line == 'done':
        break
    
    print(line)
    
    #A tupple is sequence of comma seperated values inside bracket.