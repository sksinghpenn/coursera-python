#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:08:30 2017

@author: sksingh
"""

import re

fhandle = open("regex_sum_375260.txt");
numberList = list()
for line in fhandle:
    allNumbers = re.findall("[0-9]+", line)
    if len(allNumbers) > 0:
        for myNumber in allNumbers:
            numberList.append(int(myNumber))

total = sum(numberList)
print (total)
        


              
