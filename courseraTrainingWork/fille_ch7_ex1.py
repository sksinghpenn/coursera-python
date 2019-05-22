#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:37:26 2017

@author: sksingh
"""

fileName = input("Input the file name: " )

total = 0.0
cnt = 0
try:
    fhandle = open(fileName)
    
    for line in fhandle:
        if "X-DSPAM-Confidence" in line:
            cnt = cnt +1 
            total  = total + float(line.split()[1])
            
           
    avg = total/cnt
    print("Average spam confidence : " + str(avg))
except:
    print("File does not exist")
