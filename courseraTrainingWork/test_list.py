#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:37:53 2017

@author: sksingh
"""

numberList = list()

while True:
    
    myNumber = input("Please input a number ")
    
    try:
        if myNumber == 'done':
        
            break
        numberConvertedToInt = int(myNumber)
       
        numberList.append(numberConvertedToInt)
    except:
        print("Wrong input")
        
        
print(max(numberList))
print(min(numberList))
    