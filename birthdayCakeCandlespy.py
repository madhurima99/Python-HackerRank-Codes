# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:55:32 2020

@author: MADHURIMA
"""

def birthdayCakeCandles(a) :
    
    max1=max(a)
    total = a.count(max1)
    print(total)

n=int(input())
a=[int(i) for i in input().split(" ")][:n]
birthdayCakeCandles(a)
