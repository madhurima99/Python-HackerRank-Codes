# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:42:21 2020

@author: MADHURIMA
"""

def minMaxSum(a):
    a= sorted(a)
    min1=sum(a[:4])
    max1=sum(a[1:])
    print(min1,max1)
    
a=[int(i) for i in input().split(" ")][:5]
minMaxSum(a)