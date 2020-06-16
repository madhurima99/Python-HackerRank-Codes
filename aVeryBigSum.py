# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 09:22:06 2020

@author: MADHURIMA
"""

def aVeryBigSum(ar):
    return sum(ar)
n= int(input())
ar=[ int(i) for i in input().split(" ") ]
r=aVeryBigSum(ar)
print(r)